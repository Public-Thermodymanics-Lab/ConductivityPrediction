import math

e = 1.60217663 * 10**(-19)
k = 1.380649 * 10**(-23)
F = 96485
e_0 = 8.85418782 * 10**(-12)

def S_symmetric(z, dielectric_coeff, viscosity, T, Lambda_0):
    alpha_S = 82.0460e4 * (z**3) / (dielectric_coeff * T)**(3/2)
    beta_S = 82.487 * (z**3) / (viscosity * (dielectric_coeff * T)**(1/2))
    return alpha_S * Lambda_0 + beta_S
def E(z, dielectric_coeff, viscosity, T, Lambda_0):
    E1 = 2.94257e12 * (z**6) / (dielectric_coeff * T)**3
    E2 = 4.33244e7 * (z**5) / (dielectric_coeff * T)**2 * viscosity
    return E1 * Lambda_0 - E2
def J1(z, dielectric_coeff, viscosity, T, Lambda_0, c, a):
    ab = 16.7099e4 * (z**2) / (dielectric_coeff * T)
    b = ab / a
    kappa = 50.2916 * z * math.sqrt(c) / math.sqrt(dielectric_coeff * T)
    E1 = 2.94257e12 * (z**6) / (dielectric_coeff * T)**3
    E2 = 4.33244e7 * (z**5) / (dielectric_coeff * T)**2 * viscosity
    delta_1 = 1 / (b**3) * (2 * b**2 + 2 * b - 1) + 0.90735
    delta_2 = 22 / (3 * b) + 0.0142
    return 2 * E1 * Lambda_0 * (math.log(kappa * a / math.sqrt(c)) + delta_1) + 2 * E2 * (delta_2 - math.log(kappa * a / math.sqrt(c)))
def J2(z, dielectric_coeff, viscosity, T, Lambda_0, c, a):
    ab = 16.7099e4 * (z**2) / (dielectric_coeff * T)
    b = ab / a
    kappa = 50.2916 * z * math.sqrt(c) / math.sqrt(dielectric_coeff * T)
    E1 = 2.94257e12 * (z**6) / (dielectric_coeff * T)**3
    E2 = 4.33244e7 * (z**5) / (dielectric_coeff * T)**2 * viscosity
    delta_3 = 0.9571 / (b**3) + 1.1187 / (b**2) + 0.1523 / (b)
    delta_4 = 1 / (b**3) * (0.5786 * b**2 + 7.0572 * b - 2/3) - 0.6461
    beta_S = 82.487 * (z**3) / (viscosity * (dielectric_coeff * T)**(1/2))
    delta_5 = E2 * beta_S/Lambda_0 *(4 / (3 * b) - 2.2194)
    return kappa * ab / math.sqrt(c) * (4 * E1 * Lambda_0 * delta_3 + 2 * E2 * delta_4) - delta_5
def Ka(c,alpha):
    return (1-alpha)/(alpha**2*c)
def gamma(z,c,dielectric_coeff,a,T):
    kappa = 50.2916 * z * math.sqrt(c) / math.sqrt(dielectric_coeff * T)
    ab = 16.7099e4 * (z**2) / (dielectric_coeff * T)
    return math.exp(z**2*kappa*ab/(2*(1+kappa*a)))
def func(z, dielectric_coeff, viscosity, T, Lambda_0, c, a):
    alpha = 0.9999 # degree of dissociation
    Ss = S_symmetric(z, dielectric_coeff, viscosity, T, Lambda_0)
    E_val = E(z, dielectric_coeff, viscosity, T, Lambda_0)
    J1_val = J1(z, dielectric_coeff, viscosity, T, Lambda_0, c, a)
    J2_val = J2(z, dielectric_coeff, viscosity, T, Lambda_0, c, a)
    Ka_val = Ka(c,alpha)
    gamma_val = gamma(z,c,dielectric_coeff,a,T)
    x =  Lambda_0 - Ss * math.sqrt(c * alpha) + E_val * c * math.log10(c * alpha) + J1_val * c * alpha - J2_val * (c*alpha)**(3/2)
    return x/(Ka_val*gamma_val**2*c + 1)
    #return  Lambda_0 - Ss * math.sqrt(c * alpha)+ E_val * c * math.log10(c * alpha)+ J1_val * c * alpha - J2_val * (c*alpha)**(3/2)