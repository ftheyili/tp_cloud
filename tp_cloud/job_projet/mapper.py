#!/usr/bin/env python
"""mapper.py"""

import sys
from datetime import datetime
import csv

# filtre sur annees et departements
date_debut = 2008
date_fin = 2015
index_departement = {'53', '61', '28'}

csv_reader = csv.reader(sys.stdin)

# Ignorer la première ligne (en-tête)
next(csv_reader, None)

# input comes from STDIN (standard input)
for ligne in csv_reader:
    cpcli = ligne[4][:2] # passe str pour garde que 2 premiers caracteres du code postal
    nom_ville = ligne[5]
    datcde = ligne[7][:4]
    qte = ligne[15]
    timbrecde = ligne[9]
    nom_client = ligne[2]
    prenom_client = ligne[3]
    # cpcli = str(ligne[4])[:2] # passe str pour garde que 2 premiers caracteres du code postal
    # nom_ville = ligne[5]
    # datetime.strptime(ligne[7], '%Y-%m-%d %H:%M:%S')
    # qte = int(ligne[15])
    # timbrecde = float(ligne[9])
    # nom_client = ligne[2]
    # prenom_client = ligne[3]
    
    if date_debut <= int(datcde) and int(datcde) < date_fin:
        if cpcli in {'53', '61', '28'}:
            print(timbrecde + ";" + qte + ";" + nom_client + ";"+ prenom_client + ";" + nom_ville + ";" + cpcli)


    # # split the line into words
    # words = line.split() # le séparateur par défaut
    # # increase counters
    # for word in words:
    #     # write the results to STDOUT (standard output);
    #     # what we output here will be the input for the
    #     # Reduce step, i.e. the input for reducer.py
    #     #
    #     # tab-delimited; the trivial word count is 1
    #     print('%s;%i' % (word, 1))

'''
hadoop jar hadoop-streaming-2.7.2.jar -file mapper.py -mapper "python3 mapper.py" -file reducer.py -reducer "python3 reducer.py" -input input/dataw_fro03.csv -output output01
'''