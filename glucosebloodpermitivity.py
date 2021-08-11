import numpy as np, cmath, math, csv, matplotlib.pyplot as plt, scipy
from scipy import optimize
# %%
def permittivity(X):
    Epsilon_Infinity =(0.99e-2*(X**2))+((0.47e-1)*X)+(2.3);
    Del_epsilon = (0.93e-2*(X**2))+(-0.21*X)+(71.0);
    Tau = (0.12e-2*(X**2))+(0.23*X)+(8.7);
    sigma = (0.63e-2*(X**2))+(-0.14*X)+(2.0);
    x = 0 ; y = 1;
    z = complex(x,y);   
    resonant_frequency = 60.72;
    Epsilon_infinity_high_frequency_permittivity = 4.00 ;
    Del_epsilon_magnitude_of_the_dispersion= 56.00  ;
    Tau_relaxation_time_constant = 8.377e-12;
    Alpha_Dispersion_broadening_parameter = 0.1 ;
    omega_Angular_frequency=2*3.14*resonant_frequency ;
    Epsilon_zero = 8.854e-12 ;
    Epsilon_permitivity_4 = Epsilon_Infinity;
    Epsilon_permitivity_5 = (Del_epsilon/((1+ ((z * omega_Angular_frequency*Tau)**(1-Alpha_Dispersion_broadening_parameter)))));
    Epsilon_permitivity_6 =(sigma)/(z * omega_Angular_frequency * Epsilon_zero);
    Epsilon_permitivity = Epsilon_permitivity_4 + Epsilon_permitivity_5 + Epsilon_permitivity_6 ;
    return Epsilon_permitivity;

# %%
glucose_level_mgdL = np.linspace(297,347,num=50)
#glucose_level_mgdL = [70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
Blood_permittivity = []
for i in range(0,len(glucose_level_mgdL)):
    Blood_permittivity.append(permittivity(glucose_level_mgdL[i]).real)
print(len(glucose_level_mgdL),len(Blood_permittivity))
# %%
f1 = open("BloodPermitivitty.csv", "w")
for i in range(len(glucose_level_mgdL)):
    f1.write("{},{}\n".format(glucose_level_mgdL[i], Blood_permittivity[i]))
f1.close()

# %%
def func(glucose_level_mgdL,a,b,c):
    return ((a*(glucose_level_mgdL**2))+(b*glucose_level_mgdL)+c)
popt,pconv = scipy.optimize.curve_fit(func,glucose_level_mgdL,Blood_permittivity)
print("\n")
print ("popt:",popt)
#print ("pconv:",pconv)
print("\n")
# %%
Equation=[]
for i in range(0,len(glucose_level_mgdL)):
    output = 0.00990002*(glucose_level_mgdL[i]**2)+(0.04700495*glucose_level_mgdL[i])+2.30284159
    Equation.append(output)
print("Equation Estimation",Equation)
print("Length of Equation: ", len(Equation))
# %%
error_correction_before=[]
Difference_btw_correction_before=[]
for i in range(0,len(glucose_level_mgdL)):
    if (Blood_permittivity[i]-Equation[i]) < 0.001:
        error_correction_before.append(-1)
        Difference_btw_correction_before.append(Blood_permittivity[i]-Equation[i])
    elif (Equation[i]-Blood_permittivity[i])>0.0001:
        error_correction_before.append(1)
        Difference_btw_correction_before.append(Equation[i]-Blood_permittivity[i])
    else:
        error_correction_before.append(0)
        Difference_btw_correction_before.append(0)
Blood_permittivity_round = [round(num,3) for num in Blood_permittivity]
Equation_round = [round(num,3) for num in Equation]
print("\n")
print("Blood_permittivity:",Blood_permittivity)
print("Equation:",Equation)
print("error_correction_before1: ",error_correction_before)
print("Difference_btw_correction_before: ",Difference_btw_correction_before)
print("\n")
print("Blood_permittivity_round:",Blood_permittivity_round)
print("Equation_round:",Equation_round)
# %%
error_correction_after=[]
diff=[]
for i in range(0,len(glucose_level_mgdL)):
    if Equation_round[i]<Blood_permittivity_round[i]:
        error_correction_after.append(-1)
        diff.append(Blood_permittivity_round[i]-Equation_round[i])
    elif Equation_round[i]>Blood_permittivity_round[i]:
        error_correction_after.append(1)
        diff.append(Equation_round[i]-Blood_permittivity_round[i])
    else:
        error_correction_after.append(0)
        diff.append(0)
        print("The Curve Fit is Equal to the Blood Permittivity equation")
print("error_correction_after: ",error_correction_after)
print("Difference: ",diff)
print("\n")
print(Blood_permittivity)
# %%
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Curve fitting Equation is (0.00990002*X^2)+(0.04700495*X)+2.30284159 ')
ax1.plot(glucose_level_mgdL,Blood_permittivity_round)
ax1.set(xlabel='glucose_level_mgdL', ylabel='Blood_permittivity')
ax2.plot(glucose_level_mgdL,Equation_round)
ax2.set(xlabel='glucose_level_mgdL', ylabel='Curve Fitting')
plt.show()