import cmath, math
## link for data ## http://niremf.ifac.cnr.it/docs/DIELECTRIC/AppendixC.html#FF
### Blood Glucose Conversion link https://www.bbraun.co.uk/en/patients/diabetes-care-for-patients/blood-glucose-measurement/conversion-tables.html
### Diabetes Level https://www.diabetes.co.uk/diabetes_care/blood-sugar-level-ranges.html
def mgdL_to_mmolL(x):
    mmolL = 0.0555 * x;
    return mmolL;
def mmolL_to_mgdL(x):
    mgdL = 18.018 * x;
    return mgdL;
x = 0 ; y = 1;
z = complex(x,y);
resonant_frequency = 60.72;
Epsilon_infinity_high_frequency_permittivity = 4.00 ;
Del_epsilon_magnitude_of_the_dispersion= 56.00  ;
Tau_relaxation_time_constant = 8.377e-12;
Alpha_Dispersion_broadening_parameter = 0.1 ;
Sigma_Conductivity = 0.7;
omega_Angular_frequency=2*3.14*resonant_frequency ;
Epsilon_zero = 8.854e-12 ;
Epsilon_permitivity_1 = Epsilon_infinity_high_frequency_permittivity;
Epsilon_permitivity_2 = (Del_epsilon_magnitude_of_the_dispersion/((1+ ((z * omega_Angular_frequency*Tau_relaxation_time_constant)**(1-Alpha_Dispersion_broadening_parameter)))));
Epsilon_permitivity_3 =(Sigma_Conductivity)/(z * omega_Angular_frequency * Epsilon_zero);
Epsilon_permitivity = Epsilon_permitivity_1 + Epsilon_permitivity_2 + Epsilon_permitivity_3 ;
# print("Epsilon_permitivity_1: ",Epsilon_permitivity_1)
# print("Epsilon_permitivity_2: ",Epsilon_permitivity_2)
# print("Epsilon_permitivity_3: ",Epsilon_permitivity_3)
# print("Epsilon_permitivity: ",Epsilon_permitivity)
# print("Epsilon_permitivity: ", ((Epsilon_permitivity.real**2) + (Epsilon_permitivity.imag**2))**0.5)
X = input("Give Value for Glucose Concentration in mg/dL: ");
X = int(X)
Epsilon_Infinity =(0.99e-2*(X**2))+((0.47e-1)*X)+(2.3);
Del_epsilon = (0.93e-2*(X**2))+(-0.21*X)+(71.0);
Tau = (0.12e-2*(X**2))+(0.23*X)+(8.7);
sigma = (0.63e-2*(X**2))+(-0.14*X)+(2.0);
print("Epsilon_Infinity: ",Epsilon_Infinity)
print("Del_epsilon: ",Del_epsilon)
print("Tau: ",Tau)
print("sigma: ",sigma)
x = 0 ; y = 1;
z = complex(x,y);
resonant_frequency = 60.72;
Epsilon_infinity_high_frequency_permittivity = 4.00 ;
Del_epsilon_magnitude_of_the_dispersion= 56.00  ;
Tau_relaxation_time_constant = 8.377e-12;
Alpha_Dispersion_broadening_parameter = 0.1 ;
Sigma_Conductivity = 0.7;
omega_Angular_frequency=2*3.14*resonant_frequency ;
Epsilon_zero = 8.854e-12 ;
Epsilon_permitivity_4 = Epsilon_Infinity;
Epsilon_permitivity_5 = (Del_epsilon/((1+ ((z * omega_Angular_frequency*Tau)**(1-Alpha_Dispersion_broadening_parameter)))));
Epsilon_permitivity_6 =(sigma)/(z * omega_Angular_frequency * Epsilon_zero);
Epsilon_permitivity11 = Epsilon_permitivity_4 + Epsilon_permitivity_5 + Epsilon_permitivity_6 ;
# print("Epsilon_permitivity_4: ", Epsilon_permitivity_4)
# print("Epsilon_permitivity_5: ",Epsilon_permitivity_5)
# print("Epsilon_permitivity_6: ",Epsilon_permitivity_6)
# print("Epsilon_permitivity11: ",Epsilon_permitivity11)
print("Epsilon_permitivity: ", Epsilon_permitivity11.real)
#print("mgdL: ",mmolL_to_mgdL(10))
#print("mmoL: ",mgdL_to_mmolL(10))
