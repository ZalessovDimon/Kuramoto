import os
os.system('cls')
import numpy as np
from numpy import pi,random,sin,zeros
import matplotlib.pyplot as plt

def startplot(phi,omega,N):
    t=range(100)
    plotData=[[] if i%2 else t  for i in range(2*N)]
    for i in t:
        for k in range(N):
            plotData[2*k+1].append(sin(omega[k]*i+phi[k]))
    plt.subplot(2,2,1)
    plt.plot(*plotData)
def kuramoto(Time,phi,omega,N,K):
    t=range(Time)
    plotData1=[[] if i%2 else t  for i in range(2*N)]
    plotData2=[[] if i%2 else t  for i in range(2*N)]
    dphi = zeros(N)
    for i in t:
        for k in range(N):
            dphi[k]=omega[k]+K/N*sum([sin(phi[j]-phi[k]) for j in range(N)])
            plotData1[2*k+1].append(sin(phi[k]))
            plotData2[2*k+1].append(dphi[k])
        phi+=dphi
    return plotData1,plotData2



N = 150 # количество осцилляторов
K = 1.06 # коэффициент связи
phi = random.uniform(low=0, high=2*pi, size=N) # случайные начальные фазы
omega = random.uniform(low=0.5, high=2, size=N) # случайные частоты осцилляторов
sr=sum(omega)/150
omega1=[abs(a-sr) for a in omega]
sr1=sum(omega1)/150
print(sr,sr1)
data=[phi,omega,N,K]
startplot(*data[:3])

plotData1,plotData2=kuramoto(150,*data)
plt.subplot(2,2,3)
plt.plot(*plotData1)
plt.subplot(2,2,2)
plt.plot(*plotData2)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
