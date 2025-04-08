#Paso 1: Instalar y Cargar Librerías
import pandas as pd
import plotly.express as px
import streamlit as st


pd.options.display.max_columns= None

# Cargar el CSV (asegúrate de cambiar 'datos.csv' por el nombre de tu archivo)
DATA = ('https://docs.google.com/spreadsheets/d/e/2PACX-1vT4GG7D9PKkctFY9qO1j-P0hmqeiRiGH99kJ18jrg1un3Kv66jpsPHCACItBW-srw/pub?gid=407726589&single=true&output=csv')
locations=pd.read_csv(DATA)

# Separamos la latitud y longitud en columnas diferentes.
# Suponiendo que la columna se llama "coordenadas" y está en formato "lat, lon"
locations[['lon', 'lat']] = locations['Coordenades\n(longitud, latitud)'].str.split(',', expand=True)

# Convertimos latitud y longitud a valores numéricos
locations['lat'] = locations['lat'].astype(float)
locations['lon'] =locations['lon'].astype(float)

#Agrupamos por la columna de coordenadas para obtener la suma
gr_locations =locations.groupby(['lon','lat','Tipo'],as_index=False)['Cantidad'].sum()
gr_locations.head(10)


# Datos con latitud/longitud y valores

fig = px.scatter_map(gr_locations,
                      lat = 'lat', lon = 'lon',
                        size = 'Cantidad',
                        color= 'Tipo',
                        zoom = 4,
                        map_style = 'carto-positron',
                        color_discrete_sequence=px.colors.qualitative.Plotly
                        )

fig.update_layout(
    title="Mapa de Jeringuillas y Restos de Consumo (Intravenoso / Fumado)",
    title_x=0.5,  # Centrado del título
    title_font=dict(size=24, color="black", family="Verdana"),
    height=800,  # Altura personalizada
    width=1200 # anchura personalizada
)


                        
fig.show()
                        

st.plotly_chart(fig,use_container_width=True)
