import numpy as np

def multiply_quat(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1*w2 - x1*x2 - y1*y2 - z1*z2
    x = w1*x2 + x1*w2 + y1*z2 - z1*y2
    y = w1*y2 - x1*z2 + y1*w2 + z1*x2
    z = w1*z2 + x1*y2 - y1*x2 + z1*w2
    return np.array([w, x, y, z])

q_mb1 = np.array([0.7071, 0.7071, 0, 0])  # w, x, y, z
q_mb2 = np.array([0.7071, 0, 0.7071, 0])  # w, x, y, z
quat_mb = multiply_quat(q_mb1, q_mb2)

b_q_iy_z = np.array([0.7071, -0.7071, 0, 0])  # w, x, y, z
# b_q_z_t = np.array([-0.354, 0.146, -0.354, 0.854])  # w, x, y, z
b_q_z_t = np.array([1, 0, -0, 0.])  # w, x, y, z
b_q = multiply_quat(b_q_iy_z, b_q_z_t)
m_q = multiply_quat(quat_mb, b_q)

print("Calculated quaternion for sub thrusters:", m_q)