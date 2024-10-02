import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import plotly.express as px
import time

# Configuración de la conexión
user = 'root'
password = 'Yairon04042003'
host = 'localhost'
database = 'Delitos'
connection_string = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'
engine = create_engine(connection_string)


# Función para cargar datos
def load_data():
    return pd.read_sql('SELECT * FROM `delitos`', con=engine)

# Título de la aplicación
st.title('Análisis de Datos de delitos en la ciudad de Cali')

# Contenedor para la tabla y gráficos
table_placeholder = st.empty()
chart_placeholder = st.empty()

# Función para dibujar gráficos
def draw_charts(df):
    chart_placeholder.empty()  # Limpiar el contenedor de gráficos
    
    # Gráfico de distribución de edades
    with chart_placeholder.container():
        st.subheader('Frecuencia de delitos por dia')
        fig1, ax1 = plt.subplots()
        ax1.hist(df['Dia'].dropna(), bins=30, color='skyblue', edgecolor='black')
        ax1.set_title('Días')
        ax1.set_xlabel('Días')
        ax1.set_ylabel('Frecuencia')
        st.pyplot(fig1)

        # Gráfico de supervivencia por género
        st.subheader('Frecuencia de delitos por mes')
        fig2 = px.histogram(df, x='Mes', color= 'Estrato', barmode='group',
                             title='Supervivencia por Género')
        st.plotly_chart(fig2)

        # Gráfico de sobrevivientes por clase
        st.subheader('Sobrevivientes por Clase')
        fig3 = px.histogram(df, x='Mes', color='Estrato', barmode='group',
                             title='Sobrevivientes por Clase')
        st.plotly_chart(fig3)

        # Gráfico de supervivencia en función de la edad
        st.subheader('Supervivencia en función de la Edad')
        fig4 = px.box(df, x='Mes', y='Estrato', title='Supervivencia en función de la Edad')
        st.plotly_chart(fig4)

# Función para mostrar la tabla
def show_table(df):
    table_placeholder.empty()  # Limpiar el contenedor de la tabla
    with table_placeholder.container():
        st.subheader('Datos de la Tabla')
        st.write(f'Cantidad de registros: {len(df)}')  # Mostrar cantidad de datos
        st.write(df.head())  # Mostrar los primeros registros

# Botón para actualizar los datos
if st.button('Actualizar gráficos y tabla'):
    df = load_data()  # Cargar los datos actualizados
    show_table(df)  # Mostrar la tabla actualizada
    draw_charts(df)  # Dibujar gráficos actualizados

# Refresco automático
while True:
    df = load_data()
    show_table(df)  # Mostrar la tabla actualizada
    draw_charts(df)  # Dibujar gráficos actualizados
    time.sleep(10)  # Esperar 10 segundos antes de actualizar