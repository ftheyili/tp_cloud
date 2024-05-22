import sys
import happybase
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

current_word = None
current_count = 0
word = None
index = 0
table = None
connection = happybase.Connection('127.0.0.1', 9090)
connection.open()
table = connection.table('maTable')

data = []

# Initialise variables pour current order, total quantity (qte), collected orders, index HBase et department
current_timbrecde = None
department_counts = {'53': 0, '61': 0, '28': 0}

# input comes from STDIN
for line in sys.stdin:
    print(line.split(';'))
    # line = line.strip()
    timbrecde, qte, nom_client, nom_ville, prenom_client, cpcli = line.split(';')

    # convert qte and timbrecde (currently a string) to int and float
    qte = int(qte)
    timbrecde = float(timbrecde)
    cpcli = cpcli[:2] #fix /n que je sais pas d'ou il sort

    data.append((timbrecde, qte, nom_client, prenom_client, nom_ville, cpcli))

print(data)

connection.close() #####################

# Convert orders to DataFrame and sort by
df = pd.DataFrame(data, columns=['TimbreCde', 'Qte', 'NomClient', 'PrenomClient', 'NomVille', 'CodeDep'])
# on recup les 100 premieres lignes sortby TimbreCde
df = df.sort_values(by='TimbreCde').head(100)
print(df)

# Export the df to an Excel file
output_excel_file = '/datavolume1/resultat.xlsx'
df.to_excel(output_excel_file, index=False)


df_graph = df.groupby('CodeDep')['Qte'].sum().reset_index()
print(df_graph)

# data = department_counts
# Créer une nouvelle figure
plt.figure()

# Créer le graphe en Camembert :)
plt.pie(df_graph['Qte'], labels=df_graph['CodeDep'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title("Répartition des commandes par département")

# Enregistrer le graphe au format PDF
output_pdf_file = '/datavolume1/resultat.pdf'
with PdfPages(output_pdf_file) as pdf:
    pdf.savefig()  # Sauvegarder le graphe dans le fichier PDF
