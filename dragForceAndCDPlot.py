import numpy as np
import matplotlib.pyplot as plt

# these aerobraking results found from SolidWorks CFD
# input results from whatever source you want!

thetas = [0, 5.04590913, 10.05382324, 15.00161705, 19.99682936, 25.00099569, 29.99162598, 35.01311173, 39.9999878, 45.01806451, 50.00989221, 55.04734811, 60.012329, 64.99198586, 69.9944205, 74.98734201, 80.01359005, 85.0208414, 89.9918667]
drag_forces = [0.683894, 0.771145, 0.855684, 1.22062, 1.57216, 2.46562, 3.22167, 2.93978, 3.4129, 4.08805, 4.93499, 6.23576, 7.40307, 7.86251, 9.78146, 7.60876, 8.61314, 9.03255, 8.35028]
drag_coefs = [0.631063, 0.434616, 0.344225, 0.385946, 0.410455, 0.550586, 0.631883, 0.516476, 0.546382, 0.604318, 0.681891, 0.813361, 0.920758, 0.935919, 1.13333, 0.8605, 0.957689, 0.994221, 0.916066]

fig, ax1 = plt.subplots(figsize=(9, 6))

ax2 = ax1.twinx()
ax1.set_xlabel('Deflection Angle (degrees)')

ax1.plot(thetas, drag_coefs, color='red', label='Drag Coefficient')
ax1.set_ylabel('Drag Coefficient')

ax2.plot(thetas, drag_forces, label='Impulsive Deployment Drag Force')
ax2.set_ylabel('Impulsive Deployment Drag Force (N)')

fig.suptitle('Effect of Fin Deflection Angle on Drag Performance')
fig.legend(loc='lower right')

plt.show()
