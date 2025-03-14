import flet as ft

import ddbb


def main(page: ft.Page):
    page.title=("Consultas")
    def consultar_arboles():
        arboles = ddbb.consultar_arboles_por_nombre()
        cargar_tabla(arboles)
        page.update()
    def cargar_tabla(datos):
        tabla.row=[]
        for fila in datos:
            tabla.row.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(fila[0]))),
                ft.DataCell(ft.Text(fila[1])),
                ft.DataCell(ft.Text(fila[2])),
                ft.DataCell(ft.Text(str(fila[3]))),
                ft.DataCell(ft.Text(str(fila[4]))),
            ]))

    def buscar_arboles(e):
        lista_arboles = ddbb.consultar_arboles()
        cargar_tabla(lista_arboles)
        page.update()


    nombre_tf = ft.TextField("Nombre", width=300)
    buscar_btn = ft.ElevatedButton("Buscar", on_click=buscar_arboles, width=300)
    tabla=ft.DataTable(bgcolor="yellow",
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("NOMBRE")),
            ft.DataColumn(ft.Text("TIPO")),
            ft.DataColumn(ft.Text("ALTURA")),
            ft.DataColumn(ft.Text("FECHA")),
        ]
    )

    clomuna_datos =ft.column(
        controls=[
            ft.Text("CONSULTAS", size=40)
        ]
    )
    #page.add(columna_datos)
    consultar_arboles()
    return columa_datos
