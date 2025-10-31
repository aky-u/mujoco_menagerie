import numpy as np

Rbm = np.array([[-1, 0, 0],
                [0, 0, -1],
                [0, -1, 0]])
quat_bm = np.array([0.7071, -0.7071, 0, 0])  # w, x, y, z
quat_0 = np.array([-0.354, -0.146, -0.854, 0.354])  # w, x, y, z

def multiply_quat(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1*w2 - x1*x2 - y1*y2 - z1*z2
    x = w1*x2 + x1*w2 + y1*z2 - z1*y2
    y = w1*y2 - x1*z2 + y1*w2 + z1*x2
    z = w1*z2 + x1*y2 - y1*x2 + z1*w2
    return np.array([w, x, y, z])

quat_thruster = multiply_quat(quat_bm, quat_0)
print("Quaternion for thrusters:", quat_thruster)