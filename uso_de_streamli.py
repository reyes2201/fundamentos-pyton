import streamlit as st
from PIL import Image 

img = Image.open("icono.png")

st.set_page_config(page_title="primeros pasos de streamlit", page_icon=img, layout="wide", initial_sidebar_state="collapsed")

def main ():

    
    st.title("curso de streamlit")
    st.sidebar.header("navegacion")
    st.header("esto es un encabezado")
    st.subheader("esto es un sub titulo")
    st.text("esto es un texto")
    nombre = "hugo"
    st.text(f"hola {nombre}, esto es un texto")
    st.markdown("##esto es un markdown")
    ##mensajes 
    st.success("exito")
    st.warning("advertencia")
    st.info("informacion")
    st.error("mensaje de error")
    st.exception("mensaje de exepcion")
#caja de seleccion
    opcion = st.selectbox(
        "elije la opcion",
        [1,2,3]
    )
    st.write(f'tu opcion es:  {opcion}')
#multiselect
    opciones = st.multiselect(
    "seleciona las operaciones",
    ["suma","resta","division","multiplicacion"]
)
    st.write('escogistes:'  ,opciones)
#slider
    edad = st.slider (
        'selecciona tu edad',
        min_value=0,
        max_value=100,
        value=25,   
        step=1
    )
    st.write('tu edad es',edad)
#select_slider
    nivel = st.select_slider(
        'selecciona tu nivel de satisfaccion',
        options =['muy bajo','bajo','medio','alto','muy alto'],
        value='medio'
    )
    st.write('tu nivel de satisfaccion es: ',nivel)
#imput
    nombre=st.text_input("ingresa tu nombre")
    st.write(nombre)
    numero=st.number_input('ingresa un nummero',1,25,step=1)
    st.write(numero)
    cita=st.date_input("selecciona una fecha")
    st.write(cita)
    hora=st.time_input("seleccione la hora")
    st.write(hora)
    color=st.color_picker("seleccione el color")
    st.write(color)
#mensaje
    mensaje=st.text_area("ingresa tu mensaje", height=300)
    st.write(mensaje)

if __name__ == '__main__':
    main ()

## para ejecutar (streamlit run app.py)