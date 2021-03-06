import geopandas
import leafmap.foliumap as leafmap
import streamlit as st
from PIL import Image
from request_ukraine import russian_occupies
from request_ukraine import coflicts

# Page Config
st.set_page_config(f'Ukraine', layout="wide", page_icon='gizlogo.png')

# Page Layout
space1, map_display, space2 = st.columns((1, 5, 1))


def show_map() -> None:
    map_display.header('Ukraine Map - Relive Supplies')

    gizlogo = Image.open('gizlogo.png')
    space1.image(gizlogo)

    # Import the layers
    faf_zone = geopandas.GeoDataFrame()
    file_path = "https://github.com/shi093/Leafmap-FAF/raw/main/faf4_zone2.json"
    faf_zone = geopandas.read_file(file_path)

    # Create Leaf Map with the layers
    m = leafmap.Map(center=[48.383022, 31.1828699],
                    zoom=6,
                    height=600,
                    layers_control=False,
                    measure_control=False,
                    attribution_control=False,
                    draw_control=False,
                    fullscreen_control=False, )
    m.add_basemap('OpenStreetMap.DE')
    m.add_geojson('ukraine-geojson.json', layer_name='Ukraine Territory', fill_colors=['blue'])
    m.add_geojson(russian_occupies(), layer_name='Russian Occupies', fill_colors=['red'], )

    df = coflicts()
    m.add_points_from_xy(
        coflicts(),
        x="Latitude",
        y="Longitude",
        spin=True
    )

    m.add_legend(title='LEGEND', labels=['Ukraine Territory', 'Russian Occupies'], colors=['#787DEA', '#DC5D7D'])

    # Map to Streamlit
    with map_display:
        map_display.empty()
        m.to_streamlit()


show_map()
update = map_display.button('update')
if update:
    st.spinner(text="Map loading...")
    st.experimental_rerun()
    st.success('Map updated!')
