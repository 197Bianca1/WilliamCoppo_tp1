import json
import os
import sys
from PySide6.QtWidgets import QLabel, QTableWidget, QLineEdit, QApplication,QTableWidgetItem,QVBoxLayout,QWidget
from PySide6.QtCore import Qt

#mettre le chemin du fichier JSON à charger
file_name = input("Entrez le nom du fichier JSON à charger: ")

try:
    # lit le fichier JSON et decode les données tout en les stockant dans la variable data
    with open(file_name, 'r', encoding='utf-8') as file:
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
table = QTableWidget()

# mise en place des élément dans le tableau
table.setRowCount(len(data))
table.setColumnCount(len(data[0]))
table.setHorizontalHeaderLabels(data[0].keys())

#construction du tableau avec les données du fichier JSON
for i, item in enumerate(data):
    for j, col in enumerate(data[0].keys()):
        value = item.get(col, "")
        table.setItem(i, j, QTableWidgetItem(str(value)))

table.setSortingEnabled(True)



table.show()
sys.exit(app.exec())