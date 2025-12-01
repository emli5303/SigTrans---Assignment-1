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
x_t = np.cos(w*np.pi*tk)
x_k = x_t

sd.play(x_k, fs, blocking=True)