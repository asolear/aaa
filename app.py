import sys
import os
import shutil

from types import SimpleNamespace  # Importación global

import pandas as pd
import io
import yaml
import pandas as pd
import time
import subprocess
import json
import PyPDF2
from pdfrw import PdfReader, PdfWriter, PdfName, PdfString
import inspect
from PyPDF2.generic import ArrayObject, IndirectObject
import fitz  # PyMuPDF
import pikepdf
import requests
import abc
import csv
from bs4 import BeautifulSoup
from datetime import date, timedelta
from unidecode import unidecode


class mm:
    def mostrar_opciones(self):
        return self.generar_menu()

    def generar_menu(self):
        # Filtrar todas las funciones que no sean métodos de la clase base 'mm'
        opciones = {}
        numero = 1  # Inicializamos el número de las opciones
        for atributo in dir(self):
            # Excluir métodos de la clase base 'mm' y métodos internos
            if (
                callable(getattr(self, atributo))
                and not atributo.startswith("__")
                and atributo not in ["mostrar_opciones", "generar_menu", "mostrar_menu"]
            ):
                opciones[str(numero)] = getattr(self, atributo)
                numero += 1
        opciones["0"] = None  # Opción para regresar al supermenú
        return opciones

    def mostrar_menu(self, menu):
        while True:
            print("\n--- Menú ---")
            for opcion, funcion in menu.items():
                if opcion == "0":
                    print(f"{opcion}. Regresar al supermenú")
                else:
                    print(
                        f"{opcion}. {funcion.__name__.replace('_', ' ').capitalize()}"
                    )  # Mostrar la opción como texto

            opcion = input("Seleccione una opción: ")

            if opcion in menu:
                funcion = menu[opcion]
                if funcion is None:
                    break  # Regresar al supermenú
                funcion()  # Ejecutar la función
            else:
                print("Opción no válida. Intente de nuevo.")


def mostrar_supermenu(clase_padre):
    while True:
        # Detectar las clases anidadas dinámicamente, excluyendo la clase 'mm'
        clases = [
            attr
            for attr in dir(clase_padre)
            if isinstance(getattr(clase_padre, attr), type)
            and getattr(clase_padre, attr) is not mm
        ]

        print("\n--- Menú de Submenús ---")
        # Mostramos la opción 0 para salir
        print("0. Salir")
        for i, clase in enumerate(clases, 1):
            print(f"{i}. {clase.replace('_', ' ').capitalize()}")

        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            print("Saliendo del programa.")
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= len(clases):
            clase_seleccionada = clases[int(opcion) - 1]
            # Instanciamos la clase seleccionada
            instancia_clase = getattr(clase_padre, clase_seleccionada)()
            # Llamamos al método mostrar_menu de la clase base
            instancia_clase.mostrar_menu(
                instancia_clase.generar_menu()
            )  # Correcto aquí
        else:
            print("Opción no válida. Intente de nuevo.")


def mostrar_super_supermenu():
    while True:
        print("\n--- Super Supermenú ---")
        print("0. Salir")

        # Obtener las clases contenedoras SUPERMENU_A y SUPERMENU_B
        superclases = []
        for cls_name, cls_obj in globals().items():
            # Verificamos si el objeto es una clase que contiene otras clases
            if isinstance(cls_obj, type) and cls_name.startswith("_"):
                superclases.append(cls_obj)

        superclases.sort(key=lambda x: x.__name__)

        # Mostramos las opciones de las superclases
        for i, superclase in enumerate(superclases, 1):
            print(f"{i}. {superclase.__name__.replace('_', ' ').capitalize()}")

        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            print("Saliendo del programa.")
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= len(superclases):
            clase_seleccionada = superclases[int(opcion) - 1]
            # Mostrar el supermenú de la clase seleccionada
            mostrar_supermenu(clase_seleccionada)
        else:
            print("Opción no válida. Intente de nuevo.")


class _00_MKDOCS:

    class _02_Crear_md_para_cada_pdf(mm):

        def crea_md(
            ss,
            nombre="pp",
            carpeta="/home/pk/Desktop/caes07/docs/pp/",
        ):
            """"""
            # https://www.miteco.gob.es/es/energia/eficiencia/cae/catalogo-de-fichas/catalogo-vigente-de-fichas.html
            # df = pd.read_csv(StringIO(fichas))

            path = f"{carpeta}/{nombre}.pdf"
            # para importar los formlariopdf
            formlariopdf = "".join(carpeta.split("/")[1:]) + "".join(
                nombre.split(" ")[:3]
            ).replace(" ", "").replace(",", "").replace("-", "")
            print(nombre)
            tipodoc = carpeta.split("/")[-2]

            try:
                """"""
                pdf = PdfReader(path)
            except:
                """"""
                print(f"{path}  corrupto")
                return

            tt = []
            tt.append(
                rf"""
# {nombre}

<iframe src="../{nombre}.pdf" width="100%" height="1500px"></iframe>

"""
            )

            # quitarlo del try para sobreescribirlos todos
            archivo_path = os.path.join(carpeta, f"{nombre}.md")

            # Intenta abrir el archivo en modo "x" (solo si no existe)
            with open(archivo_path, "w") as archivo:
                archivo.write("\n".join(tt))
                print(f"Archivo {archivo_path} creado correctamente.")

        def _01_crear_todos_los_md_para_cada_pdf(
            ss,
        ):
            """"""
            print("crando un componente react generico para cada formulario pdf")

            # directorio = "src/Estandarizada"

            # Iterar sobre las carpetas (y archivos) en el directorio
            for root, dirs, files in os.walk("docs/"):
                for directorio in dirs:
                    print(directorio)
                    # continue
                    # if directorio[
                    #     0
                    # ].islower():  # Verificar si la primera letra es mayúscula
                    #     continue

                    archivos_pdf = []
                    for root, dirs, files in os.walk(f"docs/{directorio}"):
                        for file in files:
                            if file.endswith(".pdf"):
                                archivos_pdf.append(
                                    (file, root)
                                )  # Almacena una tupla con el nombre del archivo y la carpeta

                    for formulario in archivos_pdf:
                        nombre = formulario[0].split(".")[0]
                        carpeta = formulario[1]
                        ss.crea_md(nombre, carpeta)

            # los formlariopdf los he sacado del los componetes para poder editarlos mas facil en u mismo archivo

            # ss._03_crear_el_catalogo_json_que_genera_el_menu_de_react()
            # ss._03_crear_el_catalogo_json_que_genera_el_menu_de_react()

        def _09_eliminartodosloscomponetesdefichas_en_Ahorro(ss):
            """"""
            import os

            # os.system("clear")
            print(99999999999999999999999)

            def eliminar_archivos_jsx(carpeta):
                # Recorrer la carpeta y sus subcarpetas
                for root, dirs, files in os.walk(carpeta):
                    for file in files:
                        print(file)
                        if not file.endswith((".pdf", ".tex")):

                            print(f"eliminado {file}")

                            file_path = os.path.join(
                                root, file
                            )  # Obtener la ruta completa del archivo

                            with open(file_path, "r") as f:
                                contenido = f.read()

                            if "noborrar" in contenido:
                                continue

                            os.remove(file_path)  # Eliminar el archivo
                            print(f"Archivo eliminado: {file_path}")

            # Especificar la carpeta donde se encuentran los archivos a eliminar

            carpetas = [
                d
                for d in os.listdir("docs/")
                if os.path.isdir(os.path.join("docs/", d))
            ]

            # solo para asegurar que no se borra componentes jsx del sitio
            carpetas = [item for item in carpetas if not "js" in item]
            # carpetas = [item for item in carpetas if "Estudios" in item]

            for carpeta in carpetas:
                # para que solo borre las qwue empiece poir mayuscula
                if 1:
                    carpeta = f"docs/{carpeta}"
                    eliminar_archivos_jsx(carpeta)


class _01_EXCEL:
    class _01_xx(mm):

        def _01_rr(ss, archivoexcel="assets/settings/0_datos.xlsx"):
            """
            leo el excel y paso cada hoja a un df accesible con el namespaces
            """
            archivo_excel = pd.ExcelFile(archivoexcel)
            dff = archivo_excel.sheet_names
            # Itera a través de las hojas del archivo Excel
            for nombre_hoja in archivo_excel.sheet_names:
                # Lee los datos de la hoja actual
                setattr(
                    x,
                    nombre_hoja,
                    archivo_excel.parse(nombre_hoja, header=0, index_col=0),
                )
                # setattr(x, nombre_hoja, archivo_excel.parse(nombre_hoja))

        def ww(archivoexcel):
            """
            # Guardar en un archivo Excel con dos hojas


            """
            excel = pd.ExcelFile(archivoexcel)
            dff = excel.sheet_names
            # print('escribiendo >>>>',dff)
            # x.o = x.x.reset_index(drop=True)
            with pd.ExcelWriter(archivoexcel, engine="xlsxwriter") as writer:
                for hoja in dff:
                    contenidohoja = getattr(x, hoja)
                    contenidohoja.to_excel(
                        writer, sheet_name=hoja, index=True, header=True
                    )
            return ""

        def dd():
            """"""
            print(f"\n {80*'.'} { __class__.__name__}.{sys._getframe().f_code.co_name}")

            if 1:
                try:
                    x.o = gpd.GeoDataFrame(
                        x.o, geometry=gpd.GeoSeries.from_wkt(x.o["geometry"])
                    )
                except:
                    """ya es geopandas"""
                gdf = x.x.copy()
                # solo los poligonos a dxf, los puntos dan error
                gdf = gdf[gdf["geometry"].apply(lambda geom: geom.type != "Point")]

                Layers = gdf["Layer"].astype(str).unique().tolist()

            if 1:
                gdf = gdf[["Layer", "geometry"]]
                gdf = gdf[~gdf["geometry"].is_empty]
                gdf = gdf.set_crs("EPSG:25830", allow_override=True, inplace=True)

            if 1:
                """para exportatlo a dxfr"""
                salidadxf = f"assets/DXFs/{x.Ubicacion['v'].RC}/ConsultaMasiva_FV.dxf"
                gdf["geometry"] = gdf["geometry"].boundary
                gdf[["Layer", "geometry"]].to_file(salidadxf, driver="DXF")

            if 1:
                """para ponerle color a las capas"""
                # Abrir un archivo DXF existente
                doc = ezdxf.readfile(salidadxf)

                # Obtener una referencia a la capa existente por su nombre
                colores = [1, 2, 3, 4, 5, 6, 7, 8, 9] * 111
                ic = 0
                for i, r in gdf.iterrows():
                    """"""
                    doc.layers.get(r.Layer).color = colores[ic]
                    ic = ic + 1
                doc.save()
            return ""

        def g():
            # creo nuevas variables reagrupadas a partir de las leidas
            # juntando todos los gen en una df gen
            # esto es solo consecuencia de facilitar la entrada de datos con el excel

            #  anadiendoles los campos de unidades
            dfm = x.m.copy()
            dfm = dfm.dropna(subset=["Codigo"], how="any", inplace=False)
            dfm = dfm.set_index("Codigo")
            # dfm.loc["genist"]["Uds"]

            partidas = [elemento for elemento in dir(x) if "gen" in elemento]
            # return
            gg = pd.DataFrame()
            for partida in partidas:
                df = getattr(x, partida).copy()
                df["Apartado"] = dfm.loc[partida]["Apartado"]
                df["Inst"] = dfm.loc[partida]["Inst"]
                df["Partida"] = dfm.loc[partida]["Partida"]
                df["UDS_a"] = dfm.loc[partida]["v"]
                df["cod_partida"] = partida
                gg = pd.concat([gg, df])
            # gg["€"] = 1
            # gg["€_a"] = 2

            return gg


class _03_EXCEL2LATEX:
    class _01_NEWCOMMAND(mm):

        def indice(ss):
            newcommand = "assets/settings/newcommand.tex"
            _03_EXCEL2LATEX._01_NEWCOMMAND.newcommand(newcommand)
            _03_EXCEL2LATEX._01_NEWCOMMAND.newcommandvariables(newcommand)
            _03_EXCEL2LATEX._01_NEWCOMMAND.newcommandtablas(newcommand)

        def newcommand(newcommand):
            """
            para pasar algunas hojas del excel a variables y a tablas enteras
            """
            if 1:
                with open(newcommand, "w") as archivo:
                    archivo.write(f'% {date.today().strftime("%Y-%m-%d")}\n')

        def newcommandvariables(newcommand):
            if 1:
                """las tablaVariable del excel como newcommand"""
                dff = pd.DataFrame()
                hojas = [
                    "Proyecto",
                    "Instalacion",
                    "Proyectista",
                    "Localizacion",
                    "Promotor",
                    "Instalador",
                ]
                dff = pd.DataFrame()
                # hojas=['Proyecto','Instalacion','Proyectista','Localizacion','Promotor','Instalador']
                # hojas=list(vars(x).keys())
                # hojas.remove(['incentivos','CUPS'])

                for hoja in hojas:
                    print(hoja)
                    df = getattr(x, hoja)

                    # # Usar la primera fila como nombres de las columnas
                    # df.columns = df.iloc[0]
                    # # Eliminar la primera fila del DataFrame
                    # df = df.drop(df.index[0])
                    df["Variable"] = hoja + df.index.map(str)
                    df["Variable"] = df["Variable"].str.lower()
                    df["Variable"] = df["Variable"].str.replace(" ", "")
                    df["Variable"] = df["Variable"].str.replace("{", "")
                    df["Variable"] = df["Variable"].str.replace("}", "")
                    df["Variable"] = df["Variable"].str.replace("(", "")
                    df["Variable"] = df["Variable"].str.replace(")", "")
                    df["Variable"] = df["Variable"].str.replace("_", "")
                    df["Variable"] = df["Variable"].str.replace("$", "")
                    df["Variable"] = df["Variable"].str.replace("%", "")
                    df["Variable"] = df["Variable"].str.replace("*", "")
                    df["Variable"] = df["Variable"].str.replace("\\", "")
                    df["Variable"] = df["Variable"].str.replace("/", "")
                    df["Variable"] = df["Variable"].str.replace(".", "")
                    df["Variable"] = df["Variable"].str.replace(",", "")
                    df["Variable"] = df["Variable"].str.replace("-", "")
                    df["Variable"] = df["Variable"].apply(unidecode)

                    # Resetear el índice
                    df.set_index("Variable", inplace=True)
                    df = df.iloc[:, 0]
                    dff = pd.concat([dff, df])
                    # dff.drop_duplicates(inplace=True)
                    # Eliminar las filas con índices duplicados
                    dff = dff[~dff.index.duplicated(keep="first")]
                    dff = dff.fillna(0)

                # Abre el archivo .tex en modo escritura
                with open(newcommand, "a") as archivo:
                    archivo.write(f"% {hojas}\n%\n%\n")
                    # Recorre cada fila del DataFrame
                    for indice, row in dff.iterrows():
                        # Escribe la línea en formato LaTeX
                        archivo.write(f'\\newcommand{{\\{indice}}}{{{row["Valor"]}}}\n')

                ###########################################################
                hojas = ["PlacaFV", "Bateria", "Inversor", "Soporte", "Cable"]
                dff = pd.DataFrame()
                for hoja in hojas:
                    print(hoja)
                    df = getattr(x, hoja)

                    # # Usar la primera fila como nombres de las columnas
                    # df.columns = df.iloc[0]
                    # # Eliminar la primera fila del DataFrame
                    # df = df.drop(df.index[0])
                    df["Variable"] = hoja + df.index.map(str)
                    df["Variable"] = df["Variable"].str.lower()
                    df["Variable"] = df["Variable"].str.replace(" ", "")
                    df["Variable"] = df["Variable"].str.replace("{", "")
                    df["Variable"] = df["Variable"].str.replace("}", "")
                    df["Variable"] = df["Variable"].str.replace("(", "")
                    df["Variable"] = df["Variable"].str.replace(")", "")
                    df["Variable"] = df["Variable"].str.replace("_", "")
                    df["Variable"] = df["Variable"].str.replace("$", "")
                    df["Variable"] = df["Variable"].str.replace("%", "")
                    df["Variable"] = df["Variable"].str.replace("*", "")
                    df["Variable"] = df["Variable"].str.replace("\\", "")
                    df["Variable"] = df["Variable"].str.replace("/", "")
                    df["Variable"] = df["Variable"].str.replace(".", "")
                    df["Variable"] = df["Variable"].str.replace(",", "")
                    df["Variable"] = df["Variable"].str.replace("-", "")
                    df["Variable"] = df["Variable"].apply(unidecode)

                    # Resetear el índice
                    df.set_index("Variable", inplace=True)
                    df = df.iloc[:, 0]
                    dff = pd.concat([dff, df])
                    # dff.drop_duplicates(inplace=True)
                    # Eliminar las filas con índices duplicados
                    dff = dff[~dff.index.duplicated(keep="first")]
                    dff = dff.fillna(0)

                # Abre el archivo .tex en modo escritura
                with open(newcommand, "a") as archivo:
                    archivo.write(f"% {hojas}\n%\n%\n")
                    # Recorre cada fila del DataFrame
                    for indice, row in dff.iterrows():
                        # Escribe la línea en formato LaTeX
                        archivo.write(f'\\newcommand{{\\{indice}}}{{{row["Valor"]}}}\n')

        def newcommandtablas(newcommand):
            if 1:
                """las tablas completas"""
                #  Abre el archivo .tex en modo escritura
                with open(newcommand, "a") as archivo:
                    # Recorre cada fila del DataFrame

                    hojas = [
                        "Proyecto",
                        "Instalacion",
                        "Proyectista",
                        "Localizacion",
                        "Promotor",
                        "Instalador",
                        "PlacaFV",
                        "Bateria",
                        "Inversor",
                        "Soporte",
                        "Cable",
                    ]
                    archivo.write(
                        f"% hojas completas del excel a latex {hojas}\n%\n%\n"
                    )

                    # hojas=['Proyecto','PlacaFV']
                    for hoja in hojas:
                        df = getattr(x, hoja)
                        # df.columns = df.iloc[0]
                        # Eliminar la primera fila del DataFrame
                        df = df.drop(df.index[0])
                        # Resetear el índice
                        # df.set_index('Descripcion', inplace=True)
                        df.index.name = None
                        df = df.dropna()
                        df = df.replace("#", "", regex=True)
                        df = df.replace("$", "", regex=True)

                        archivo.write(
                            f"""\\newcommand{{\\{hoja}}}{{{df.to_latex(
                        position="H"
                        ) }}}\n"""
                        )

    class _02_CSNAMES:
        def _00_csnames():
            """"""
            print("kkkkkkkkkkk")


if __name__ == "__main__":
    """el codigo tiene que estar en superclase/clase/funcion con los nombres en mayuscula y se ira ijecutando en orden"""

    x = SimpleNamespace()

    _01_EXCEL._01_xx._01_rr("assets/settings/0_datos.xlsx")
    # print(o)

    try:
        print(dev)

    except:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        mostrar_super_supermenu()
