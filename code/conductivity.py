from assym_conduct import funct
import matplotlib.pyplot as plt
import numpy as np
solutes = [{"cat":"Na","z_cat":1,"v_cat":1,"an":"Cl","z_an":-1,"v_an":1,"lambda_cat":50.08,"lambda_an":72.31},
           {"cat":"K","z_cat":1,"v_cat":3,"an":"Fe(CN)6","z_an":-1,"v_an":3,"lambda_cat":73.48,"lambda_an":100.9}]
solvent = {"name":"H2O","dc":81.103,"visc": 0.01 }


legend = []

#Lab data NaCl
x_lab = [0.0005,0.001,0.005,0.01,0.02,0.05,0.1,0.5,1.0]
y_lab = np.array([65.0,128.5,620.0,1206.8,2363.6,5604.5,10814.1,45586.9,85247.7])/1000
plt.plot(x_lab,y_lab,"*")
legend.append("NaCl lab")
#Lab data K3Fe(CN)6
x_lab2 = [0.05,0.1,0.5,1.0]
y_lab2 = np.array([14635.2,27070.9,115919,203401])/1000
plt.plot(x_lab2,y_lab2,"*")
legend.append("K3Fe(CN)6 lab")

#Lab data NaCl + K3Fe(CN)6
x_lab3 = np.array([1/2,1/4,1/40])*2
y_lab3 = np.array([146301,82523.8,10396.4])/1000
plt.plot(x_lab3,y_lab3,"*")
legend.append("combo lab")
##Lab data Na2CO3
# x_lab = [0.2,0.5,1,2]
# y_lab = np.array([26790.4,52602.7,80969.3,104585])/1000
# plt.plot(x_lab,y_lab,"*")
plt.legend(legend)
plt.show()