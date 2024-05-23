from assym_conduct import cond
import matplotlib.pyplot as plt
import numpy as np
from extras import format
import csv
solutes = [{"cat":"Na","z_cat":1,"v_cat":1,"an":"Cl","z_an":-1,"v_an":1,"lambda_cat":50.08,"lambda_an":72.31},
           {"cat":"K","z_cat":1,"v_cat":3,"an":"Fe(CN)6","z_an":-1,"v_an":3,"lambda_cat":73.48,"lambda_an":100.9}]
solvent = {"name":"H2O","dc":81.103,"visc": 0.01 }
#read the lab data
data = []
with open('data/lab.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        floated_row = [x for x in row[1:]]
        data.append(floated_row)
#legend names
legend = []

#print the conductivity of NaCl as predicted by assym_conduct.py
x = np.linspace(0,2,100)[1:]
y = [cond(solutes[0],solvent,i,300)*i for i in x]
plt.plot(x,y)
legend.append("NaCl theoretical")

#read data and print the conductivity of NaCl as found in lab
x = data[0][1:]
y = data[1][1:]
x,y = format(x,y)#get rid of missing data points and make everything floats
plt.plot(x,y,"*")
legend.append("NaCl Lab")

#plot things
plt.xlabel("Molarity")
plt.ylabel("Conductivity")
plt.legend(legend)
plt.show()