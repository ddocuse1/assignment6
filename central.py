import matplotlib.pyplot as plt
import numpy as np

k = 8.987e9
q1 = -1.602e-19
q2 = 1.602e-19
x1 = -0.05
x2 = -x1
xlim = 0.1
ylim = 0.1
dx = dy = 0.001
rows = cols = int(1+ 2*xlim/dx)

#quiver
xquiver = yquiver = 25
rquiver = np.zeros((xquiver,yquiver))
dquiv = 2*xlim/xquiver
Xquiv, Yquiv  = np.meshgrid(np.arange(-xlim,xlim+dquiv,dquiv),np.arange(-ylim,ylim+dquiv,dquiv))
Rquiv1 = np.sqrt((Xquiv-x1)**2+Yquiv**2)
Rquiv2 = np.sqrt((Xquiv-x2)**2+Yquiv**2)
Rquiv1[Rquiv2 < 0.1] = 0.1
Rquiv1[Rquiv2 < 0.1] =0.1
Exq1 = -k*q1*(Xquiv-x1)*Rquiv1**(-3)
Eyq1 = -k*q1*Yquiv*Rquiv1**(-3)
Exq2 = -k*q2*(Xquiv-x2)*Rquiv2**(-3)
Eyq2 = -k*q2*Yquiv*Rquiv2**(-3)
Exq = Exq1 + Exq2
Eyq = Eyq1 + Eyq2
Eq = np.sqrt(Exq**2+Eyq**2)
Eqmax = np.percentile(Eq, 85)  
maskq = Eq > Eqmax
Exq[maskq] = np.nan
Eyq[maskq] = np.nan

#contour
r_array = np.zeros((rows,cols))
x = np.arange(-xlim,xlim+dx, dx)
y = np.arange(-ylim,ylim+dx, dx)
X, Y = np.meshgrid(x,y)
R1 = np.sqrt((X-x1)**2+Y**2)
R2 = np.sqrt((X-x2)**2+Y**2)
R1[R1 < 0.001] = 0.001
R2[R2 < 0.001] =0.001
V1 = k*q1/R1
V2 = k*q2/R2
V = V1 + V2
Ex1 = k*q1*(X-x1)*R1**(-3)
Ey1 = k*q1*Y*R1**(-3)
Ex2 = k*q2*(X-x2)*R2**(-3)
Ey2 = k*q2*Y*R2**(-3)
Ex = Ex1 + Ex2
Ey = Ey1 + Ey2
E = np.sqrt(Ex**2 + Ey**2)
Emax = np.percentile(E, 99)  
mask = E > Emax
Ex[mask] = np.nan
Ey[mask] = np.nan
print(V1,V2)

#plotting
fig, ax = plt.subplots(figsize=(6,5))  

cf = ax.contourf(X, Y, V, levels=100, cmap='coolwarm')
plt.colorbar(cf, ax=ax, label="Electric Potential (V)")
ax.axis('equal')
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Electric Potential")
plt.savefig('potential.png')
q = ax.quiver(Xquiv, Yquiv, Exq, Eyq, scale=1.8e-5, color='black')
ax.quiverkey(q, .9, -.1,1.1e-6,r'$E = 10^{-6} V/m$',labelpos='W')
ax.set_title("Electric Potential + Field")
plt.savefig('efield.png')



plt.show()