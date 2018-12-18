import matplotlib.pyplot as plt
import numpy as np



def ndft(t,f,N):
    k =  np.arange(N)
    return np.dot(f,np.exp(2j*np.pi*k*t[:,np.newaxis]))




t=-0.5+np.random.rand(1000)   #generating_time_domain
f=np.sin(100*2*np.pi*t)       #generating the signal
k=np.arange(200)
z=ndft(t,f,len(k))
plt.plot(k,z.imag)
