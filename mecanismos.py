import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from celluloid import Camera
data = pd.read_excel('plaina.xlsx')
x = data.iloc[:,0].values.reshape(600,1)
y = data.iloc[:,1].values.reshape(600,1)
alpha = data.iloc[:,2].values.reshape(600,1)
beta = data.iloc[:,3].values.reshape(600,1)
theta = data.iloc[:,4].values.reshape(600,1)
u =1.1
v = 0.6
w = 0.22
a = 0.18
b = 1
r = 0.2
fig = plt.figure()
camera = Camera(fig)
for i in range(0,600):
    p0= [w ,0]
    p1 =[w - a*math.cos(alpha[i,0]),a*math.sin(alpha[i,0])]
    p2 = [0, v]
    p3 = [r*math.cos(theta[i,0]), y[i,0]*math.cos(beta[i,0]) + a*math.sin(alpha[i,0])]
    p4 = [x[i,0],u]

    x_v = [p0[0],p1[0]]
    y_v = [p0[1], p1[1]]
    plt.plot(x_v,y_v, color = 'black')
    
    x_v = [p1[0],p4[0]]
    y_v = [p1[1], p4[1]]
    plt.plot(x_v,y_v, color = 'black')
    
    x_v = [p2[0],p3[0]]
    y_v = [p2[1], p3[1]]
    plt.plot(x_v,y_v, color = 'black')
    
    #MARCADORES
    plt.scatter(p4[0],p4[1], color = 'red',marker = '+')
    plt.scatter(p2[0],p2[1], color = 'red',marker = '+')
    plt.scatter(p0[0],p0[1], color = 'red',marker = '+')
    
    #PLOTAR RETANGULO
    #PARTE 1
    
    x_v = [p4[0]-0.05,p4[0]-0.05]
    y_v = [p4[1]-0.05, p4[1]+0.05]
    plt.plot(x_v,y_v, color = 'black')
    #PARTE 2
    x_v = [p4[0]-0.05,p4[0]+0.05]
    y_v = [p4[1]+0.05, p4[1]+0.05]
    plt.plot(x_v,y_v, color = 'black')
    #PARTE 3
    x_v = [p4[0]+0.05,p4[0]+0.05]
    y_v = [p4[1]+0.05, p4[1]-0.05]
    plt.plot(x_v,y_v, color = 'black')
    #PARTE 4
    x_v = [p4[0]-0.05,p4[0]+0.05]
    y_v = [p4[1]-0.05, p4[1]-0.05]
    plt.plot(x_v,y_v, color = 'black')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5,1.5)
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.title("Simulação do torpedo da plaina limadora")
    camera.snap()
animation = camera.animate() 
