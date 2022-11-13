import streamlit as st
import leafmap.foliumap as leafmap
import ee
import geemap


def app():

    st.title("NO2_Consentration")
    m = geemap.Map()
    data = ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_NO2").filterDate('2022-01-01','2022-11-01')
    vis_params = {
        'min':0.0,
        'max':0.05,
        'palette':[
            "black",
            "blue",
            "purple",
            "cyan",
            "green",
            "yellow",
            "red"
        ]
    }
    m = m.addLayer(data, vis_params, "No2")
    m.to_streamlit(height=700)
