from assym_conduct import funct
import matplotlib.pyplot as plt
import numpy as np
solutes = [{"cat":"Na","z_cat":1,"v_cat":1,"an":"Cl","z_an":-1,"v_an":1,"lambda_cat":50.08,"lambda_an":72.31},
           {"cat":"K","z_cat":1,"v_cat":3,"an":"Fe(CN)6","z_an":-1,"v_an":3,"lambda_cat":73.48,"lambda_an":100.9}]
solvent = {"name":"H2O","dc":81.103,"visc": 0.01 }

# x = np.linspace(0.00001,1.5,100)
# y = [funct(solutes[0],solvent,x,300)*x for x in x]
# plt.plot(x,y)
# y = [funct(solutes[1],solvent,x,300)*x for x in x]
# plt.plot(x,y)
legeng = []

#Lab data NaCl
x_lab = [0.0005,0.001,0.005,0.01,0.02,0.05,0.1,0.5,1.0]
y_lab = np.array([65.0,128.5,620.0,1206.8,2363.6,5604.5,10814.1,45586.9,85247.7])/1000
plt.plot(x_lab,y_lab,"*")
legeng.append("NaCl lab")
#Lab data K3Fe(CN)6
x_lab2 = [0.05,0.1,0.5,1.0]
y_lab2 = np.array([14635.2,27070.9,115919,203401])/1000
plt.plot(x_lab2,y_lab2,"*")
legeng.append("K3Fe(CN)6 lab")
x_theo = []
y_theo = []
for i in x_lab:
    if i in x_lab2:
        x_theo.append(i)
        y_theo.append((y_lab2[x_lab2.index(i)] + y_lab[x_lab.index(i)])/2)
plt.plot(x_theo,y_theo,"*")
legeng.append("combo theo")
#Lab data NaCl + K3Fe(CN)6
x_lab3 = np.array([1/2,1/4,1/40])*2
y_lab3 = np.array([146301,82523.8,10396.4])/1000
plt.plot(x_lab3,y_lab3,"*")
legeng.append("combo lab")
##Lab data Na2CO3
# x_lab = [0.2,0.5,1,2]
# y_lab = np.array([26790.4,52602.7,80969.3,104585])/1000
# plt.plot(x_lab,y_lab,"*")

plt.legend(legeng)
plt.show()