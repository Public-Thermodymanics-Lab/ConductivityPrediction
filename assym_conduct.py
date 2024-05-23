from math import sqrt
from math import log as ln
from math import log10 as log
e = 1.60217663e-19
k = 1.380649e-23
F = 96485
e_0 = 8.85418782 * 10**(-12)
def cond(solutes,solvent,c,T): # returns the conductance for the given solvent
    z1 = solutes["z_cat"]
    z2 = solutes["z_an"]
    v_cat = solutes["v_cat"]
    v_an = solutes["v_an"]
    lambda_pos_0 = solutes["lambda_cat"]
    lambda_neg_0 = solutes["lambda_an"]
    dielectric_coeff = solvent["dc"]
    viscosity = solvent["visc"]

    #Made up parameters
    alpha = 0.9999 # degree of dissociation
    a = 3.5

    I = 1/2*(abs(z1) + abs(z2))*c
    Lambda_0 = v_cat*lambda_pos_0 + v_an*lambda_neg_0
    kappa= 50.2901/sqrt(dielectric_coeff*T)* sqrt(I)
    bd = abs(z1*z2)*16.7102e4/(dielectric_coeff*T)
    d=abs(z1*z2)*16.7102e4/(2*dielectric_coeff*T)
    b = bd/d
    q = abs(z2*z1)*Lambda_0/((abs(z2)+abs(z1))*(abs(z1)*lambda_neg_0+abs(z2)*lambda_pos_0))
    D = ((q**3-q**2+5*q-1)*ln(1+sqrt(q))+q*(1-q)*(q-4)*ln(2+sqrt(q))-4*q*ln(2))/(2*q*(1-q)) + \
     0.3456 + \
     (6+19*sqrt(q)-5*q-6*sqrt(q**3))/(12*sqrt(q)*(1+sqrt(q))) - \
     (abs(z1)*z1 + abs(z2)*z2)*(z1+z2)/(q*abs(z1*z2)*(abs(z1)+abs(z2)))*2.5407
    B = ((1-q)**3*ln(1+sqrt(q))+q*(q**2-q+2)*ln(2+sqrt(q)) + 2*q*(1-2*q)*ln(1+2*sqrt(q)))/(2*q*(1-q)) +\
    0.5772 - \
    (6+15*sqrt(q)+30*q+23*sqrt(q**3)-6*q**2)/(12*sqrt(q)*(1+sqrt(q))**2)
    A = 1 + (z1 + z2)*(abs(z1)*z1 + abs(z2)*z2)/(q*(z1*z2)*(abs(z1)+abs(z2)))
    alpha_S = 2.8012e6 * abs(z1*z2) / ((dielectric_coeff * T)**(3/2))* q/(1+sqrt(q))
    beta_S = 4.1243 * (abs(z1) + abs(z2)) / (viscosity * sqrt(dielectric_coeff * T))
    S = alpha_S * Lambda_0 + beta_S
    E1 = 5.8850e12 * q * (z1*z2)**2 / (dielectric_coeff * T)**3
    E2 = 2.1662e6 * (2*q*A) * (abs(z1*z2)*(abs(z1) + abs(z2))) / (dielectric_coeff * T)**2 / viscosity
    E = E1 * Lambda_0 - E2
    delta_1 = (2*b**2 + 2*b -1)/(b**3) + B
    delta_2 = D + (6*q + (24-13*q)*b)/(6*q*b**2)
    E2_prime = E2*I/(2*q*A)
    sigma_1 = 2*E1*(delta_1 + ln(kappa*d/sqrt(I)))/I
    sigma_2 = 4*E2_prime*q*(delta_2 - 2*A*ln(kappa*d/sqrt(I)))/I
    J1 = sigma_1*Lambda_0 + sigma_2
    delta_3 = 0.9571/b**3 + 1.1187/b**2 + 0.1523/b 
    delta_4 = 1/b**3*(0.5738*b**2+7.057*b-2/3)-0.6461
    delta_5 = (4/3/b - 2.2194)
    sigma_3 = 4*kappa*bd*E1*delta_3/sqrt(I**3)
    sigma_4 = (2*kappa*bd*E2_prime*delta_4 - delta_5*E2_prime*beta_S/Lambda_0)/sqrt(I**3)
    J2 = sigma_3*Lambda_0 + sigma_4
    x =  Lambda_0 - S * sqrt(I * alpha) # E * I * ln(I * alpha) #+ J1 * I * alpha - J2 * (I*alpha)**(3/2)
    return x