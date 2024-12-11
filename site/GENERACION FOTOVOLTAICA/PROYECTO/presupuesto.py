class presupuesto:
    def presupuesto():
        """"""
        presupuesto.Proyecto07PRESUPUESTO()

    def Proyecto07PRESUPUESTO():
        tt = []
        if 1:
            # nombre='Presupuesto Tareas'
            df = o.presupuesto.copy()
            print(df)
            # exit()
            # df=df.T

            df.set_index([0, 1, 2], inplace=True)

            df.columns = df.iloc[0]
            new_header = df.iloc[1]
            df = df[1:]

            df.columns = pd.MultiIndex.from_tuples(
                [(col, new_header.iloc[i]) for i, col in enumerate(df.columns)]
            )

            new_header = df.iloc[1]
            df = df[2:]
            df.columns = pd.MultiIndex.from_tuples(
                [(col, new_header.iloc[i]) for i, col in enumerate(df.columns)]
            )

            # elimino la fila con los valores unitarios
            ud = df.iloc[0]
            df = df.drop(df.index[0])
            df.drop([df.columns[0], df.columns[-1]], axis=1, inplace=True)

        if 1:
            tt.append(r"\documentclass{article}")
            tt.append(r"\input{../../../assets/settings/usepackage.tex}")
            tt.append(r"\begin{document}")
            gs = df.groupby(0, sort=False)

            for g, dfg in gs:
                tt.append(rf"\subsection*{{{g} }}")

                sgs = dfg.groupby(1, sort=False)
                for sg, dfsg in sgs:
                    tt.append(rf"\subsubsection*{{{sg}.}} ")

                    ssgs = dfsg.groupby(2, sort=False)
                    for ssg, dfssg in ssgs:

                        dfssg = dfssg.T
                        dfssg.columns = [None] * len(dfssg.columns)
                        dfssg.columns = ["Eur"]
                        dfssg["UD"] = list(ud)[1:-1]
                        dfssg["Eur/UD"] = dfssg["Eur"] / dfssg["UD"]
                        dfssg = dfssg[["UD", "Eur/UD", "Eur"]]

                        dfssg = dfssg.dropna()
                        tt.append(rf"\begin{{center}}")
                        tt.append(rf"\underline{{{ssg}.  }}")
                        tt.append(rf"\newline")
                        tt.append(f"\n{dfssg.to_latex(float_format='{:0.1f}'.format)}")
                        tt.append(rf"\newline")
                        tt.append(rf"\end{{center}}")
                        tt.append(rf"\begin{{flushright}}")
                        tt.append(rf" Parcial {ssg} {dfssg['Eur'].sum()} Eur. ")
                        tt.append(rf"\end{{flushright}}")

                    tt.append(rf"\begin{{flushright}}")
                    tt.append(rf"\textbf{{ Subtotal {sg} {dfsg.sum().sum()} Eur}}")
                    tt.append(rf"\end{{flushright}}")

                tt.append(rf"\begin{{flushright}}")
                tt.append(rf"\textbf{{ Total {g} {dfg.sum().sum()} Eur}}")
                tt.append(rf"\end{{flushright}}")

            tt.append(rf"\begin{{flushright}}")
            tt.append(rf"\textbf{{ TOTAL PRESUPUESTO {df.sum().sum()} Eur}}")
            tt.append(rf"\end{{flushright}}")

            # tt.append(r"\end{document}")
            # with open(f'{sys._getframe().f_code.co_name}.tex', "w") as archivo:
            #     # Escribir el contenido de la variable en el archivo
            #     archivo.write("".join(tt))

        # def PROYECTO07PRESUPUESTO01recursos():
        # tt = []
        if 1:
            nombre = "Presupuesto Tareas"
            df = o.presupuesto.copy()
            df = df.T

            df.set_index([0, 1, 2], inplace=True)

            df.columns = df.iloc[0]
            new_header = df.iloc[1]
            df = df[1:]
            df.columns = pd.MultiIndex.from_tuples(
                [(col, new_header.iloc[i]) for i, col in enumerate(df.columns)]
            )

            new_header = df.iloc[1]
            df = df[2:]
            df.columns = pd.MultiIndex.from_tuples(
                [(col, new_header.iloc[i]) for i, col in enumerate(df.columns)]
            )

            # elimino la fila con los valores unitarios
            ud = df.iloc[0]
            df = df.drop(df.index[0])
            df.drop([df.columns[0], df.columns[-1]], axis=1, inplace=True)

        if 1:
            # tt.append(r"\documentclass{article}")
            # tt.append(r"\input{../../../assets/settings/usepackage.tex}")
            # tt.append(r"\begin{document}")

            gs = df.groupby(0, sort=False)

            for g, dfg in gs:
                tt.append(rf"\subsection*{{{g} }}")

                sgs = dfg.groupby(1, sort=False)
                for sg, dfsg in sgs:
                    tt.append(rf"\subsubsection*{{{sg}.}} ")

                    ssgs = dfsg.groupby(2, sort=False)
                    for ssg, dfssg in ssgs:

                        dfssg = dfssg.T
                        dfssg.columns = [None] * len(dfssg.columns)
                        dfssg.columns = ["Eur"]
                        dfssg["UD"] = list(ud)[1:-1]
                        dfssg["Eur/UD"] = dfssg["Eur"] / dfssg["UD"]
                        dfssg = dfssg[["UD", "Eur/UD", "Eur"]]
                        dfssg = dfssg.dropna()
                        tt.append(rf"\begin{{center}}")
                        tt.append(rf"\underline{{{ssg}.  }}")
                        tt.append(rf"\newline")
                        tt.append(f"\n{dfssg.to_latex(float_format='{:0.1f}'.format)}")
                        tt.append(rf"\newline")
                        tt.append(rf"\end{{center}}")
                        tt.append(rf"\begin{{flushright}}")
                        tt.append(rf" Parcial {ssg} {dfssg['Eur'].sum()} Eur. ")
                        tt.append(rf"\end{{flushright}}")

                    tt.append(rf"\begin{{flushright}}")
                    tt.append(rf"\textbf{{ Subtotal {sg} {dfsg.sum().sum()} Eur}}")
                    tt.append(rf"\end{{flushright}}")

                tt.append(rf"\begin{{flushright}}")
                tt.append(rf"\textbf{{ Total {g} {dfg.sum().sum()} Eur}}")
                tt.append(rf"\end{{flushright}}")

            tt.append(rf"\begin{{flushright}}")
            tt.append(rf"\textbf{{ TOTAL PRESUPUESTO {df.sum().sum()} Eur}}")
            tt.append(rf"\end{{flushright}}")

            tt.append(r"\end{document}")

            with open(f"Proyecto. 07 PRESUPUESTO.tex", "w") as archivo:
                # Escribir el contenido de la variable en el archivo
                archivo.write("".join(tt))


class xx:
    def rr(archivoexcel):
        """
        leo el excel y paso cada hoja a un df accesible con el namespaces
        """
        archivo_excel = pd.ExcelFile(archivoexcel)
        dff = archivo_excel.sheet_names
        # Itera a través de las hojas del archivo Excel
        for nombre_hoja in archivo_excel.sheet_names:
            # Lee los datos de la hoja actual
            setattr(
                o, nombre_hoja, archivo_excel.parse(nombre_hoja, header=0, index_col=0)
            )
            # setattr(o, nombre_hoja, archivo_excel.parse(nombre_hoja))

    def ww(archivoexcel):
        """
        # Guardar en un archivo Excel con dos hojas


        """
        excel = pd.ExcelFile(archivoexcel)
        dff = excel.sheet_names
        # print('escribiendo >>>>',dff)
        # o.o = o.o.reset_index(drop=True)
        with pd.ExcelWriter(archivoexcel, engine="xlsxwriter") as writer:
            for hoja in dff:
                contenidohoja = getattr(o, hoja)
                contenidohoja.to_excel(writer, sheet_name=hoja, index=True, header=True)
        return ""

    def dd():
        """"""
        print(f"\n {80*'.'} { __class__.__name__}.{sys._getframe().f_code.co_name}")

        if 1:
            try:
                o.o = gpd.GeoDataFrame(
                    o.o, geometry=gpd.GeoSeries.from_wkt(o.o["geometry"])
                )
            except:
                """ya es geopandas"""
            gdf = o.o.copy()
            # solo los poligonos a dxf, los puntos dan error
            gdf = gdf[gdf["geometry"].apply(lambda geom: geom.type != "Point")]

            Layers = gdf["Layer"].astype(str).unique().tolist()

        if 1:
            gdf = gdf[["Layer", "geometry"]]
            gdf = gdf[~gdf["geometry"].is_empty]
            gdf = gdf.set_crs("EPSG:25830", allow_override=True, inplace=True)

        if 1:
            """para exportatlo a dxfr"""
            salidadxf = f"assets/DXFs/{o.Ubicacion['v'].RC}/ConsultaMasiva_FV.dxf"
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
        dfm = o.m.copy()
        dfm = dfm.dropna(subset=["Codigo"], how="any", inplace=False)
        dfm = dfm.set_index("Codigo")
        # dfm.loc["genist"]["Uds"]

        partidas = [elemento for elemento in dir(o) if "gen" in elemento]
        # return
        gg = pd.DataFrame()
        for partida in partidas:
            df = getattr(o, partida).copy()
            df["Apartado"] = dfm.loc[partida]["Apartado"]
            df["Inst"] = dfm.loc[partida]["Inst"]
            df["Partida"] = dfm.loc[partida]["Partida"]
            df["UDS_a"] = dfm.loc[partida]["v"]
            df["cod_partida"] = partida
            gg = pd.concat([gg, df])
        # gg["€"] = 1
        # gg["€_a"] = 2

        return gg


if 1:
    import os, glob, sys, shutil
    import pandas as pd
    from types import SimpleNamespace
    from datetime import date, timedelta
    from unidecode import unidecode
    from PyQt5.QtWidgets import (
        QApplication,
        QMainWindow,
        QPushButton,
        QVBoxLayout,
        QWidget,
        QMessageBox,
    )


if __name__ == "__main__":
    """ """
    o = SimpleNamespace()
    xx.rr("assets/0_datos.xlsx")
    if 0:
        MKDOCS.bblog()
        exit()

    # print(o.i)
    # dev='comentar esta linea para que haga el menu GUI'
    try:
        """
        # para cuando lo importo desde un notebook
        """
        print(dev)
        caes.generaTEX()
    except:
        """
        GUI Qt
        """

        # os.chdir(os.path.dirname(os.path.abspath(__file__)))
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
        # indice.indice()
        # # memoria.memoria()
        # # # mediciones.mediciones()
        # # presupuesto.presupuesto()
        # figuras.perfil()
