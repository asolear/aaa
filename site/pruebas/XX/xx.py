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
from unidecode import unidecode
from datetime import date, timedelta


class _03_EXCEL2LATEX:
    class _01_NEWCOMMAND:

        def indice():
            newcommand = "../../assets/settings/newcommand.tex"
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
                        df.columns = df.iloc[0]
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
                        position="H", 
                        header=False,
                        index=False
                        ) }}}\n"""
                        )

    class _02_CSNAMES:
        def _00_csnames():
            """"""
            print("kkkkkkkkkkk")


class _01_EXCEL:
    class _01_xx:

        def _01_rr(archivoexcel="0_datos.xlsx"):
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


if __name__ == "__main__":
    """el codigo tiene que estar en superclase/clase/funcion con los nombres en mayuscula y se ira ijecutando en orden"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    x = SimpleNamespace()
    _01_EXCEL._01_xx._01_rr("../../assets/settings/0_datos.xlsx")
    _03_EXCEL2LATEX._01_NEWCOMMAND.indice()
    _03_EXCEL2LATEX._02_CSNAMES._00_csnames()
