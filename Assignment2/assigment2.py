import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# -------------- TASK 1 -------------- #

n = 15                              # tidsintervallkonstant
T0 = 0.015
w0 = 400 * np.pi                    # 2 * np.pi / T0
n2 = np.arange(-n, n + 1, 1) 
wn = n2 * w0

Xn = np.zeros(len(n2), dtype=complex)
non_zeros = n2 != 0

Xn[non_zeros] = ((1j * (-1.0)**n2[non_zeros]) / (np.pi * n2[non_zeros]))*2*np.pi

# Create a plot with two rowes and one column
fig, ax = plt.subplots(2, 1)

# Plot magnitude spectrum
ax[0].stem(wn, np.abs(Xn))
ax[0].set_title("Magnitude spectrum")
#ax[0].set_xlabel('$\omega$ / rad / s')
ax[0].set_ylabel('|Xn|')
ax[0].grid()

# Plot phase spectrum
ax[1].stem(wn, np.angle(Xn))
ax[1].set_title("Phase spectrum")
ax[1].set_xlabel('$\omega$ (rad/s)')
ax[1].set_ylabel('∠Xn(rad)')
ax[1].grid()
plt.legend()
#plt.show()

# -------------- TASK 2 -------------- #

alpha = 1000*np.pi
dw = 30
w = np.arange(-n*1000, n*1000 + dw, dw)

# h = np.zeros(len(w), dtype=complex)
# non_zeros2 = w != 0
#h[non_zeros2]= (alpha**2)/(alpha + 1j*w[non_zeros2])**2

h = (alpha**2)/(alpha + 1j*w)**2

fig, ax = plt.subplots(2, 1)

# Plot magnitude spectrum
ax[0].plot(w, np.abs(h), linewidth=1, label="Hej")
ax[0].set_title("Magnitude spectrum")
#ax[0].set_xlabel('$\omega$ / rad / s')
ax[0].set_ylabel('|H|')
ax[0].grid()

# Plot phase spectrum
ax[1].plot(w, np.angle(h), linewidth=1, label="bajs")
ax[1].set_title("Phase spectrum")
ax[1].set_xlabel('$\omega$ (rad/s)')
ax[1].set_ylabel('∠H(rad)')
ax[1].grid()
plt.legend()
plt.show()

