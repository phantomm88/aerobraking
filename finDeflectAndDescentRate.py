# with the drag coefficient and the initial drag force found, we can find the vertical trajectory of the probe using RK4 integration
# start at 500m, then move position until 200m, where parachute deployment begins
from ambiance import Atmosphere

deflections = [0, 5.04590913, 10.05382324, 15.00161705, 19.99682936, 25.00099569, 29.99162598, 35.01311173, 39.9999878, 45.01806451, 50.00989221, 55.04734811, 60.012329, 64.99198586, 69.9944205, 74.98734201, 80.01359005, 85.0208414, 89.9918667]
cds = [0.631063, 0.434616, 0.344225, 0.385946, 0.410455, 0.550586, 0.631883, 0.516476, 0.546382, 0.604318, 0.681891, 0.813361, 0.920758, 0.935919, 1.13333, 0.8605, 0.957689, 0.994221, 0.916066]

#  grams
M = 0.6080389

def f(state, d_ind):
  atmo = Atmosphere(state[0][0])
  return np.array([[state[1][0]],
                   [0.5 * atmo.density[0] * state[1][0]**2 * (0.0080008654 + 4 * 0.01482401 * np.sin(np.radians(deflections[d_ind]))) * cds[d_ind] / M - atmo.grav_accel[0]]])

def f_1(state, d_ind):
  return f(state, d_ind)

def f_2(state, d_ind, h):
  return f(state + 0.5 * h * f_1(state, d_ind), d_ind)

def f_3(state, d_ind, h):
  return f(state + 0.5 * h * f_2(state, d_ind, h), d_ind)

def f_4(state, d_ind, h):
  return f(state + h * f_3(state, d_ind, h), d_ind)

def update_time(t, h):
  return t + h

def update_state(state, d_ind, h):
  return state + h * ((1/6) * f_1(state, d_ind) + (1/3) * f_2(state, d_ind, h) + (1/3) * f_3(state, d_ind, h) + (1/6) * f_4(state, d_ind, h))

#### INITIAL STATE ####

probe_init = np.array([[500],
                       [-11.946417578034099]])


def rk4(init_state, t0, xf, d_ind):
  probe_states = []
  probe = init_state

  ts = []
  t = t0
  h = 0.05

  poss = []
  vels = []

  while probe[0][0] > xf:
    t_i = t
    ts.append(t_i)

    probe_i = probe
    probe_states.append(probe_i)
    poss.append(probe_i[0][0])
    vels.append(probe_i[1][0])

    t = update_time(t_i, h)
    probe = update_state(probe_i, d_ind, h)

  return ts, poss, vels

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,8))

for i in range(0, len(deflections)):
  ts, positions, velocities = rk4(probe_init, 0, 200, i)
  ax1.plot(ts, positions, label=str(deflections[i])+' degrees')
  ax2.plot(ts, velocities, label=str(deflections[i])+' degrees')
  ax1.legend(loc = 'upper right')
  ax1.set_xlabel('Time (s)')
  ax2.set_xlabel('Time (s)')

  ax1.set_ylabel('Vertical Position (m)')
  ax2.set_ylabel('Plunge Velocity (m/s)')

  ax1.set_title('Effect of Fin Deflection on Descent Position')
  ax2.set_title('Effect of Fin Deflection on Descent Rate')
  ax2.legend(loc = 'lower right')

  print('Deflection Angle:', deflections[i])
  print('Final time:', ts[-1])
  print('Final position:', positions[-1])
  print('Final velocity:', velocities[-1])
  print()


plt.show()
