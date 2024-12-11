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


if __name__ == "__main__":
    """el codigo tiene que estar en superclase/clase/funcion con los nombres en mayuscula y se ira ijecutando en orden"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    x = SimpleNamespace()
    _01_EXCEL._01_xx._01_rr("../../assets/settings/0_datos.xlsx")
    _03_EXCEL2LATEX._01_NEWCOMMAND.indice()
    _03_EXCEL2LATEX._02_CSNAMES._00_csnames()
