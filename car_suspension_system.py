from scipy.integrate import solve_ivp
import matplotlib.pylab as plt
import numpy as np
#speed is 100 km/h
def mercedes_benz_suspension(t,z,k1,m1,c1):
    x, v=z
    if 3<t<10:
        x_road=0.1*np.sin(((np.pi*27)/0.2)*(t-3))
    else:
        x_road=0
    dxdt=v
    dvdt=-((c1*v)+(k1*(x-x_road)))/m1
    return [dxdt,dvdt]
k1=20000 #N/m
m1=520 #Kg
c1=1900 #N.s/m
def Rolls_Royce_suspension(t,z,k2,m2,c2):
    x, v=z
    if 3<t<10:
        x_road=0.1*np.sin(((np.pi*27)/0.2)*(t-3))
    else:
        x_road=0
    dxdt=v
    dvdt=-((c2*v)+(k2*(x-x_road)))/m2
    return [dxdt,dvdt]
k2=16000 #N/m
m2=600 #Kg
c2=1500 #N.s/m
z0=[0,0]
t_span=(0,10)
sol=solve_ivp(mercedes_benz_suspension,t_span,z0,args=(k1,m1,c1))
mol=solve_ivp(Rolls_Royce_suspension,t_span,z0,args=(k2,m2,c2))
plt.plot(sol.t,sol.y[0],'r-',label='mercedes benz suspension system')
plt.plot(mol.t,mol.y[0],'k-',label='Rolls Royce suspension system')
plt.xlabel('t axis')
plt.ylabel('y axis')
plt.legend()
plt.show()