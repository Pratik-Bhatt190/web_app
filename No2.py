import streamlit as st
import leafmap.foliumap as leafmap
import ee
import geemap

st.title("Welcome to my app")

st.write("NO2_Consentration")
def app():

        Map = geemap.Map()
        data = ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_NO2").filterDate('2022-01-01','2022-11-01').select('tropospheric_NO2_column_number_density')
        # data = data.first()
        # print(data.size().getInfo())
        vis_params = {
            'min':0.0,
            'max':0.00004,
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
        Map.addLayer(data, vis_params, "No2")
        Map.setCenter(88.30,26.30,6)
        Map.to_streamlit()
