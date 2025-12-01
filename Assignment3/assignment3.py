import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

w = 2000
Ts = 0.1 * 10**(-3)
T0 = 0
T1 = 5
tk = np.arange(T0, T1, Ts)
fs = 1/Ts
fs2 = 1100
x_t = np.cos(w*np.pi*tk)
x_k = x_t
fb = 2000 
     
# -------------- TASK 1 -------------- #

sd.play(x_k, fs, blocking=True) # f = 10000 Hz
#sd.play(x_k, fs2, blocking=True) # f = 1100 Hz

# Plot x(t), x[k]
fig, ax = plt.subplots()
ax.stem(tk, x_k, label="x[k], discrete")
ax.plot(tk, x_k, label="x(t), continuous")
ax.set_title("Task 1")
ax.set_xlabel('t (s)')
ax.set_ylabel('x(t)')
ax.legend()
ax.set_xlim(0, 0.003) 
ax.set_ylim(-1.1, 1.1)
ax.grid()
plt.show()

# -------------- TASK 2 -------------- #
tk2 = np.arange(T0, T1, 1/2000)
x_t2 = np.cos(w*np.pi*tk2)
sd.play(x_t2, fb, blocking=True) 

fig, ax = plt.subplots()
ax.stem(tk2, x_t2, label="x[k], discrete")
ax.plot(tk2, x_t2, label="x(t), continuous")
ax.set_title("Task 1")
ax.set_xlabel('t (s)')
ax.set_ylabel('x(t)')
ax.legend()
ax.set_xlim(0, 0.003) 
ax.set_ylim(-1.1, 1.1)
ax.grid()
plt.show()

y_t = np.sin(w*np.pi*tk)

sd.play(y_t, fs, blocking=True) # låter samma som 1a) bara lite skillnad i phase

fig, ax = plt.subplots()
ax.stem(tk, y_t, label="y[k], discrete")
ax.plot(tk, y_t, label="y(t), continuous")
ax.set_title("Task 2")
ax.set_xlabel('t (s)')
ax.set_ylabel('y(t)')
ax.legend()
ax.set_xlim(0, 0.003) 
ax.set_ylim(-1.1, 1.1)
ax.grid()
plt.show()

# -------------- TASK 3 -------------- #
T = 10
fs3 = 40000
fs4 = 8000
K = T * fs3
x = sd.rec(int(K), fs3, channels=1, blocking=True)
print("Recording shape:", x.shape)

N = 4
wn = 3400 
z, p, k = signal.butter(N, wn, analog=True, output='zpk')

H = signal.ZerosPolesGain(z, p, k)

w, magnitude, phase = signal.bode(H, n=1000)

magnitude = 10**(magnitude/20)
phase = phase * (np.pi/180)
w = w/2*np.pi

fig, ax = plt.subplots()
ax.plot(w, magnitude, label="Magnitude")
ax.set_title("Task 3, Fourth-Order Butterworth Filter Amplitude Response")
ax.set_xlabel('f (Hz)')
ax.set_ylabel('Amplitude Gain, |H(f)|')
ax.legend()
ax.grid(which='both')
ax.set_xlim(1000, 10000) 
plt.show()

t_int = np.arange(0, T, 1/fs3)
tf, xf, __ = signal.lsim(H, x[:,0], t_int)

# Resampling
x = x[::5]
xf = xf[::5]
print("Sampled shape:", xf.shape)
sd.play(x, fs4, blocking=True)
sd.play(xf, fs4, blocking=True)


