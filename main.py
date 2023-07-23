import matplotlib.pyplot as plt
import numpy as np
from propotional_integral import PropotionalIntegralDerivative as pid
from dynamic_model import MassSpringDamper as msd

DT = 0.0001 # он же dt, только капсом
reg = pid(15, 0, 0.01, DT, -14, 14) # вызов функции PID
model = msd(1, 1, 1, dt=DT)
T = 20
t = np.arange(0, T, DT)
F = 0
x_des = np.ones(len(t))
model_x = []

P_hist, D_hist, I_hist, F_hist = [], [], [], []
for i in range(len(t)):
    model_x.append(model.update(F))
    F = -reg.update(model_x[-1], x_des[i])
    P_hist.append(reg.propotional)
    D_hist.append(reg.derivative)
    I_hist.append(reg.integral)
    F_hist.append(F)

# задаем графики
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=[15, 9])
ax1.plot(t, model_x, label="real x")
ax1.plot(t, x_des, label="x desired")
ax2.plot(t, P_hist, label="P")
ax2.plot(t, I_hist, label="I")
ax2.plot(t, D_hist, label="D")
ax3.plot(t, F_hist, label="F")

# выводим графики
ax1.legend()
ax1.plot()
ax2.legend()
ax2.plot()
ax3.legend()
ax3.plot()

plt.show()
