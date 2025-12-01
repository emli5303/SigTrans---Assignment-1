import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# -------------- TASK 1 -------------- #

n = 12                              # tidsintervallkonstant, |nw0| < 15e3
T0 = 0.005
w0 = 400 * np.pi                    # 2 * np.pi / T0
n2 = np.arange(-n, n + 1, 1) 
wn = n2 * w0

Xn = np.zeros(len(n2), dtype=complex)
non_zeros = n2 != 0

Xn[non_zeros] = ((1j * (-1.0)**n2[non_zeros]) / (np.pi * n2[non_zeros]))*2*np.pi

# Create a plot with two rowes and one column
fig, ax = plt.subplots(2, 1)

# Plot magnitude spectrum
ax[0].stem(wn, np.abs(Xn), label="X($\omega$)")
ax[0].set_title("Magnitude spectrum")
#ax[0].set_xlabel('$\omega$ / rad / s')
ax[0].set_ylabel('|X($\omega$)|')
ax[0].legend()
ax[0].grid()

# Plot phase spectrum
ax[1].stem(wn, np.angle(Xn), label="X($\omega$)")
ax[1].set_title("Phase spectrum")
ax[1].set_xlabel('$\omega$ (rad/s)')
ax[1].set_ylabel('∠X($\omega$) (rad)')
ax[1].grid()
plt.legend()
#plt.show()

# -------------- TASK 2 -------------- #

alpha = 1000*np.pi
dw = 30
w = np.arange(-n*1000, n*1000 + dw, dw)

h = (alpha**2)/(alpha + 1j*w)**2

fig, ax = plt.subplots(2, 1)

# Plot magnitude spectrum
ax[0].plot(w, np.abs(h), linewidth=1, label="H($\omega$)")
ax[0].set_title("Magnitude spectrum")
#ax[0].set_xlabel('$\omega$ / rad / s')
ax[0].set_ylabel('|H($\omega$)|')
ax[0].legend()
ax[0].grid()

# Plot phase spectrum
ax[1].plot(w, np.angle(h), linewidth=1, label="H($\omega$)")
ax[1].set_title("Phase spectrum")
ax[1].set_xlabel('$\omega$ (rad/s)')
ax[1].set_ylabel('∠H($\omega$) (rad)')
ax[1].grid()
ax[1].legend()


# -------------- TASK 3a) -------------- #

Hn = (alpha**2)/(alpha + 1j*wn)**2
Yn = Hn * Xn

fig, ax = plt.subplots(2, 1)

# Plot magnitude spectrum
ax[0].stem(wn, np.abs(Xn), linefmt='orange', label="X($\omega$)")
ax[0].stem(wn, np.abs(Yn), linefmt='red', label="Y($\omega$)")
ax[0].plot(wn, np.abs(Hn), linewidth=1, label="H(w)")
ax[0].set_title("Magnitude spectrum")
ax[0].set_xlabel('$\omega$ / rad / s')
ax[0].set_ylabel('|Y($\omega$)|, |X($\omega$)|')
ax[0].grid()
ax[0].legend()

# Plot phase spectrum
ax[1].stem(wn, np.angle(Xn), linefmt='orange', label="X($\omega$)")
ax[1].stem(wn, np.angle(Yn), linefmt='red', label="Y($\omega$)")
#ax[1].plot(wn, np.angle(Hn), linewidth=1, label="H(w)")
ax[1].set_title("Phase spectrum")
ax[1].set_xlabel('$\omega$ (rad/s)')
ax[1].set_ylabel('∠Y($\omega$), ∠X($\omega$) (rad)')
ax[1].grid()
ax[1].legend()


# -------------- TASK 3b) -------------- #

t0 = 0
t1 = 0.015
inc = 0.00001
t = np.arange(t0, t1, inc)

n_max = 20
all_n = [1, 2, 10, 20]
n_full = np.arange(-n_max, n_max+1)

fig, ax = plt.subplots()

for i in all_n:
    n_current = np.arange(-i, i+1)
    wnew = n_current * w0

    Xnew = np.zeros(len(n_current), dtype=complex)
    non_zeros = n_current != 0

    Xnew[non_zeros] = ((1j * (-1.0)**n_current[non_zeros]) / (np.pi * n_current[non_zeros]))*2*np.pi
    Hnew = (alpha**2)/(alpha + 1j*wnew)**2
    Ynew = Hnew * Xnew
    
    y_t = (1/(2*np.pi)) * np.dot(Ynew, np.exp(1j*np.outer(wnew, t)))
    ax.plot(t, np.real(y_t), label=f"y(t), N={i}")

ax.set_title("Synthesized signals")
ax.set_xlabel("t (s)")
ax.set_ylabel("y(t)")
ax.grid()
ax.legend()
plt.show()



