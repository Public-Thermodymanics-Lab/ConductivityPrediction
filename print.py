from Simple_conduct import func
from assym_conduct import funct
import matplotlib.pyplot as plt
import csv
import numpy as np
# Input parameters
dielectric_coeff = 80.103  #From tabulated values
viscosity = 0.009  #poise - From tabulated values
Lambda_0 = 126.39
solutes = [{"cat":"Cu","z_cat":1,"v_cat":1/2,"an":"SO4","z_an":-1,"v_an":1/2,"lambda_cat":53.6,"lambda_an":80.0},
           {"cat":"Mg","z_cat":1/2,"v_cat":1/2,"an":"Cl","z_an":-1,"v_an":1,"lambda_cat":53.0,"lambda_an":76.31},
           {"cat":"Na","z_cat":1,"v_cat":1,"an":"Cl","z_an":-1,"v_an":1,"lambda_cat":50.08,"lambda_an":76.31}]
solvent = {"name":"H2O","dc":80.103,"visc": 0.009 }
a = 3.5 #the closest distance of opposite ion approach. From MD Simulation
z = 1  #charge number
data = []
error = []
legeng = []
with open('infinity.csv', newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        data.append(row)
x_vals = [0.0005, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1]
ys = ["CuSO4","1/2MgCl2"]
for row in data:
    x = []
    y_data = []
    y_form = []
    error.append([row[0]])
    error[-1].append(0)
    for i in range(2,len(row)):
        if row[i] != ' â€”':
            x.append(x_vals[i-2])
            y_data.append(float(row[i])*x_vals[i-2])
            y_form.append(funct(solutes,solvent,x,300)*x_vals[i-2])
            error[-1][1] += abs((y_data[-1] - y_form[-1])**2)
    y_form = []
    for i in range(len(x_vals)):
        y_form.append(func(z, dielectric_coeff, viscosity, 300, float(row[1]), x_vals[i], a)*x_vals[i])
    error[-1][1] /= len(y_data)
    if (row[0] in ys):
        legeng.append(row[0] + " tab")
        #legeng.append(row[0] + " theo")
        plt.plot(x, y_data,'*')
        #plt.plot(x_vals,y_form)
x_lab = [0.0005,0.001,0.005,0.01,0.02,0.05,0.1,0.5,1.0]
y_lab = np.array([65.0,128.5,620.0,1206.8,2363.6,5604.5,10814.1,45586.9,85247.7])/1000
plt.plot(x_lab,y_lab,"*")
legeng.append("NaCl lab")
plt.xlabel('Concentration (M)')
plt.ylabel('Conductivity 10^–1 S/m')
plt.title('Conductivity vs Concentration')
error = sorted(error, key=lambda tup: tup[1])
for e in error:
    print(f"{e[0]} error : {e[1]:0.6f}")


x = [0.0005, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y = [funct(solutes,solvent,x,300)*x for x in x_vals]
plt.plot(x_vals,y,"-")
legeng.append("CuSO4 new")
y = [funct([solutes[1]],solvent,x,300)*x for x in x_vals]
plt.plot(x_vals,y,"-")
legeng.append("MgCl2 new")
y = [funct([solutes[2]],solvent,x,300)*x for x in x]
plt.plot(x,y,"-")
legeng.append("Nacl new")
plt.legend(legeng)
plt.show()