from datetime import datetime

import ddbb
import libros_ddbb

import flet as ft


def main(page: ft.Page, abrir_selector=None, crear_arbol=None, seleccionar_fecha=None):
    page.title = "CONTROL DE JARDIN"

    def abrir_selector(e):
        date_picker.open = True
        page.update()

    def seleccionar_fecha(e):
        fecha_txt.value = f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}"

    def get_tipos():
        lista_tipos = []
        lista_tipos.append(ft.dropdown.Option(text="Perenne", key="Perenne"))
        lista_tipos.append(ft.dropdown.Option(text="Caduca", key="Caduca"))
        return lista_tipos

    def crear_arbol(e):
        nombre = nombre_tf.value
        tipo = tipos_drop.value
        altura = altura_tf.value
        fecha = date_picker.value
        ddbb.insertar_arbol(nombre, tipo, altura, fecha)

    # objetos
    nombre_tf = ft.TextField(label="Nombre", width=300)
    tipos_drop = ft.Dropdown(label="Tipo", width=300, options=get_tipos())
    altura_tf = ft.TextField(label="Altura", width=300)

    date_picker = ft.DatePicker(on_change=seleccionar_fecha, value=datetime.datetime.now())
    fecha_txt = ft.Text(f"{date_picker.value.month}/{date_picker.value.day}/{date_picker.value.year}")
    volver_btn = ft.ElevatedButton(text="Volver", on_click=volver)

    columna_datos = ft.Column(
        controls=[ft.Text("ARBOLES", size=40),
                  nombre_tf,
                  tipos_drop,
                  altura_tf,
                  fecha_txt,
                  ft.FilledButton("SELECCIONAR FECHA", onclick=abrir_selector),
                  ft.FilledButton("CREAR ARBOL", on_click=crear_arbol)
                  volver_btn,
                  ],

    )
    page.overlay.append(date_picker)
    #page.add(columna_datos)
    return  columna_datos


