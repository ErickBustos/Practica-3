
import matplotlib.pyplot as plt
import numpy as np
from random import randint, uniform
from math import sqrt
import time

cuadro= 5000
radio=cuadro/2
assert radio <= (cuadro/2)
centro=cuadro/2


####trazar circulo

theta= np.linspace(0,2*np.pi,100)
circ_x=centro + radio* np.cos(theta)
circ_y=centro + radio* np.sin(theta)

inicio=time.time()
n=100000
puntos_x=[round(uniform(0,cuadro),2) for i in range (0,n)]
puntos_y=[round(uniform(0,cuadro),2) for i in range (0,n)]
print(puntos_x)



x_in, y_in= [], []
x_out, y_out= [], []
for i in range (0,n):
    distancia= sqrt ((puntos_x[i]-centro)**2 + (puntos_y[i]-centro)**2)
    if distancia<= radio:
        x_in.append(puntos_x[i])
        y_in.append(puntos_y[i])
    else:
        x_out.append(puntos_x[i])
        y_out.append(puntos_y[i])

final=time.time()
print('el tiempo fue:', round((final-inicio),4),'segundos')
PI= 4*(len(x_in)/n)
print(PI)
cuadro_x, cuadro_y=[0,0,cuadro,cuadro,0], [0,cuadro,cuadro,0,0]
plt.plot(cuadro_x,cuadro_y)
plt.plot(circ_x,circ_y, label='circunferencia')
plt.scatter(x_in,y_in,color='red',s=1)
plt.scatter(x_out, y_out, color='green', s=2)
plt.text(centro/2,centro,f'PI={PI}', size=14)
plt.gca().set_aspect('equal')
plt.xlabel('ejex')
plt.ylabel('ejey')
plt.title('valor de pi')
plt.show()

