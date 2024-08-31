import streamlit as st
import folium
from streamlit_folium import st_folium

# Menghilangkan padding default di Streamlit
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .main .block-container {
        padding: 0;
        margin: 0;
    }

    .css-18e3th9 { visibility: hidden !important;
    }

    .css-1d391kg { visibility: hidden !important;
    }
    
    .css-1rs6os { display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Mengambil ukuran layar
width = 2400  # Misalkan Anda menggunakan lebar layar 1200 px
height = 800  # Misalkan Anda menggunakan tinggi layar 800 px

# Membuat peta dengan lokasi Jakarta
m = folium.Map(location=[-6.200000, 106.816666], zoom_start=12, tiles=None)

folium.TileLayer('Esri.WorldImagery').add_to(m)
folium.Marker([-6.200000, 106.816666], popup="Jakarta").add_to(m)

# Menampilkan peta fullscreen
st_folium(m, width=width, height=height)
