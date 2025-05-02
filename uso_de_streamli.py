import streamlit as st

def main ():
    
    st.title("curso de streamlit")
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






if __name__ == '__main__':
    main ()

## para ejecutar (streamlit run app.py)