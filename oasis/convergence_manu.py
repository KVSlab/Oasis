
import numpy as np
import matplotlib.pyplot as plt


dt = [0.2, 0.1, 0.02, 0.01]

# IPCS P1P1 (N=80) (it=1)
L2_ux_N80 = [2.005465e-01, 7.067774e-02, 1.238817e-02, 5.570317e-03]
L2_p_N80  = [3.725475e-01, 3.127366e-01, 3.602970e-01, 4.079875e-01]
plt.figure(1)
plt.loglog(dt,L2_ux_N80,'o-', label='L2_ux (IPCS P1P1 N80 it1)')
plt.figure(2)
plt.loglog(dt,L2_p_N80,'o-', label='L2_p (IPCS P1P1 N80 it1)')

# IPCS P1P1 (N=120) (it=1)
L2_ux_N120 = [2.020160e-01, 7.199808e-02, 1.356848e-02, 6.297747e-03]
L2_p_N120  = [3.154901e-01, 1.371685e-01, 9.512440e-02, 9.393075e-02]
plt.figure(1)
plt.loglog(dt,L2_ux_N120,'o-', label='L2_ux (IPCS P1P1 N120 it1)')
plt.figure(2)
plt.loglog(dt,L2_p_N120,'o-', label='L2_p (IPCS P1P1 N120 it1)')

# IPCS P1P1 (N=200) (it=1)
L2_ux_N200 = [2.027891e-01, 7.269368e-02, 1.427567e-02,6.934438e-03]
L2_p_N200  = [2.774642e-01, 8.881414e-02, 2.271255e-02,2.239097e-02]
plt.figure(1)
plt.loglog(dt,L2_ux_N200,'o-', label='L2_ux (IPCS P1P1 N200 it1)')
plt.figure(2)
plt.loglog(dt,L2_p_N200,'o-', label='L2_p (IPCS P1P1 N200 it1)')





# BDFPC P1P1 (N=80) (it=1)
L2_ux_N80 = [9.413675e-01,4.279604e-01,4.124491e-02,1.311806e-02]
L2_p_N80  = [6.342218e-01,3.114048e-01,3.270598e-01,3.799542e-01]
plt.figure(1)
plt.loglog(dt,L2_ux_N80,'o-', label='L2_ux (BDFPC P1P1 N80 it1)')
plt.figure(2)
plt.loglog(dt,L2_p_N80,'o-', label='L2_p (BDFPC P1P1 N80 it1)')

# BDFPC P1P1 (N=120) (it=1)
L2_ux_N120 = [8.633667e-01,3.624945e-01,4.220501e-02,1.385250e-02]
L2_p_N120  = [7.072200e-01,1.593412e-01,9.667807e-02,9.992169e-02]
plt.figure(1)
plt.loglog(dt,L2_ux_N120,'o-', label='L2_ux (BDFPC P1P1 N120 it1)')
plt.figure(2)
plt.loglog(dt,L2_p_N120,'o-', label='L2_p (BDFPC P1P1 N120 it1)')

# BDFPC P1P1 (N=200) (it=1)
L2_ux_N200 = [8.027716e-01,2.978251e-01,4.216049e-02,1.463849e-02]
L2_p_N200  = [6.193281e-01,1.035083e-01,2.263918e-02,2.264149e-02]
plt.figure(1)
plt.loglog(dt,L2_ux_N200,'o-', label='L2_ux (BDFPC P1P1 N200 it1)')
plt.figure(2)
plt.loglog(dt,L2_p_N200,'o-', label='L2_p (BDFPC P1P1 N200 it1)')


plt.figure(1)
plt.grid(True)
plt.xlabel('dt')
plt.xlim(0.005, 0.5)
plt.ylabel('error')
plt.ylim(0.001, 10)
plt.title("Horiz. vel. error")
plt.legend()

plt.figure(2)
plt.grid(True)
plt.xlabel('dt')
plt.xlim(0.005, 0.5)
plt.ylabel('error')
plt.ylim(0.001, 10)
plt.title("Pressure error")
plt.legend()
plt.show()
