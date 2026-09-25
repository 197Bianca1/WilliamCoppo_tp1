import json
import os
import sys
from PySide6.QtWidgets import QLabel, QTableWidget, QLineEdit, QApplication,QTableWidgetItem,QVBoxLayout,QWidget
from PySide6.QtCore import Qt

# récupère le fichier JSON resut en paramètre
file_name = sys.argv[1]

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

# permet de mettre le tableau en ordre croissant et decroissant
table.setSortingEnabled(True)

# permet davoir la taille du fichier JSON
size_file = os.path.getsize(file_name)

#nombre d'élément dans la liste
number_of_items = len(data)

# variable qui contient l,affichage
information_label = QLabel(f"nom du fichier: {file_name} |" f" Taille du fichier : {size_file} octets |" f"Nombre d'éléments : {number_of_items}" )

# edition d'une seule ligne de texte
query = QLineEdit()

# eddition du texte a l'intérieur de la ligne
query.setPlaceholderText("Recherche...")

#fonction four la recherche
def search(text):

    # il vérifie l'élément recherché
    item = table.findItems(text,Qt.MatchContains)

    # si l'élément est trouvé
    if item:

        # il donne le premier élément trouver 
        item = item[0]

        # sélectionne l'élément trouver dans le tableau 
        table.setCurrentItem(item)

# appel la fonction a achaque recherche
query.textChanged.connect(search)

# créé un layout verticale
layout = QVBoxLayout()

# ajoute les information dans le layout
layout.addWidget(information_label)

layout.addWidget(query)

# ajoute le layout dans le tableau
layout.addWidget(table)

# créé une fenêtre
window = QWidget()

# associe le layout a la fenêtre
window.setLayout(layout)

#affiche la fenêtre
window.show()

#permet la sortie du programme
sys.exit(app.exec())