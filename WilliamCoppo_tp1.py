import json
import os
import sys
from PySide6.QtWidgets import QLabel, QTableWidget, QLineEdit, QApplication,QTableWidgetItem,QVBoxLayout,QWidget
from PySide6.QtCore import Qt

#mettre le chemin du fichier JSON à charger
nom_fichier = input("Entrez le nom du fichier JSON à charger: ")

try:
    # lit le fichier JSON et decode les données tout en les stockant dans la variable data
    with open(nom_fichier, 'r', encoding='utf-8') as file:
        data = json.load(file)

# exception en cas d'erreure de nom de fichier
except FileNotFoundError:
    print("fichier introuvable")
    sys.exit(1)

# exception en cas d'erreure de codage JSON
except json.JSONDecodeError as e:
    print("Erreur de decodage JSON:", e)
    sys.exit(1)

# Crée l'application PySide6
app = QApplication(sys.argv)

# crée un tableau