#Paso 1: Instalar y Cargar Librerías
import pandas as pd
import plotly.express as px
import streamlit as st


pd.options.display.max_columns= None


# Cargar el CSV (asegúrate de cambiar 'datos.csv' por el nombre de tu archivo)
DATA = ("https://raw.githubusercontent.com/MikiLeon/interactivos_streamlit/refs/heads/main/mapa.csv")
locations=pd.read_excel(DATA) #sheet_name= 'mapa_localitzacions'

# Ver las primeras filas para comprobar que se cargó bien
locations.head(10)

# Separamos la latitud y longitud en columnas diferentes.
# Suponiendo que la columna se llama "coordenadas" y está en formato "lat, lon"
locations[['lon', 'lat']] = locations['Coordenades\n(longitud, latitud)'].str.split(',', expand=True)

# Convertimos latitud y longitud a valores numéricos
locations['lat'] = locations['lat'].astype(float)
locations['lon'] =locations['lon'].astype(float)

locations['Xeringues'] = locations['Xeringues'].fillna(0)



# Datos con latitud/longitud y valores

fig = px.scatter_map(locations, lat = 'lat', lon = 'lon', size = 'Xeringues',
                        zoom = 4, map_style = 'open-street-map')
                        
fig.show()

st.plotly_chart(fig)
