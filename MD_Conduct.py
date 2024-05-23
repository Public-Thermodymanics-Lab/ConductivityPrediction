import math
import matplotlib.pyplot as plt
#constants
e = 1.60217663 * 10**(-19)
k = 1.380649 * 10**(-23)
F = 96485
e_0 = 8.85418782 * 10**(-12)
def condInf(Vol, Temp):
    N_cat = 4
    N_an = 4
    z_cat = 2
    z_an = 2
    D_cat = 2.8e-5
    D_an = 2.8e-5
    return (e**2/(Vol*k*Temp))*(N_cat*z_cat**2*D_cat+N_an*z_an**2*D_an)
#FOHFJ Formalism
def FOHFJ(c,solv,T):
    volume = 5
    dielectric_coeff = 78.39#From tabulated values
    viscosity = 0.01 #poise - From tabulated values
    cond_inf = condInf(1,T)#From MD Simulations
    alpha = 90 #degree of dissasociation
    a = 3.5 #the closest distance of opposite ion approach. From MD Simulation
    z = 2 #charge number
    
    #S
    alpha_S= 82.0460e4 * (z**3)/(dielectric_coeff*T)**(3/2)
    beta_S = 82.487*(z**3)/(viscosity*(dielectric_coeff*T)**(1/2))
    S =  alpha_S*cond_inf+beta_S

    #E
    ab = 16.7099e4*(z**2)/(dielectric_coeff*T)
    b = ab/a #a is closest ion approac
    kappa = 50.2916*z*math.sqrt(c)/math.sqrt(dielectric_coeff*T)#reciprocal radius
    E1 = 2.94257e12*(z**6)/(dielectric_coeff*T)**3
    E2 = 4.33244e7*(z**5)/(dielectric_coeff*T)**2
    E = E1*cond_inf - E2

    #J
    delta_1 = 1/(b**3)*(2*b**2+2*b-1) + 0.90735
    delta_2 = 22/(3*b)+0.0142
    delta_3 = 0.9571/(b**3)+1.1187/(b**2)+0.1523/(b**2)
    delta_4 = 1/(b**3)*(0.5786*b**2+7.0572*b-2/3)-0.6461
    delta_5 = E2*beta_S/cond_inf * (4/(3*b)-2.2194)
    J1 = 2*E1*cond_inf*(math.log(kappa*a/math.sqrt(c))+delta_1) + 2*E2*(delta_2-math.log(kappa*a/math.sqrt(c)))
    J2 = kappa*ab/math.sqrt(c)*(4*E1*cond_inf*delta_3+2*E2*delta_4) - delta_5
    J = J1*c-J2*(c**(3/2)) 

    K_a = (1-alpha)/(alpha**2*c)

    gamma = math.exp(z**2*kappa*ab/(2*(1+kappa*a)))

    return (cond_inf - S*math.sqrt(alpha*c) + E*(alpha*c)*math.log10(alpha*c) + J) /(1+ K_a*gamma**2*(alpha*c))
x=  [0.001,0.0001,0.002,0.003,0.004,0.005,0.1,0.2,0.3,0.4,0.5,1,2,3,4,5,6,7,10]
y =  [FOHFJ(x/10,"hey",270)*x/10 for x in x]
plt.plot(x,y)
plt.show()
