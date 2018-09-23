import math
import sys
import re
import numpy as np
import matplotlib.pyplot as plt

from IPython import embed

################################################################################
# Reading text file
text   = open("TG_output_P1P1_dt_all.txt", "r").read()
number = "([0-9]+.[0-9]+e[+-][0-9]+)"
word   = "(\S+)"

match = re.findall("Final Error: u0=" + number
                 + " u1=" + number + " p=" + number, text)

# Arrange results by solvers into lists
dt = [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]
L2u_bdfpc       = [2.188186e-02,7.235445e-03,1.987625e-03,2.897166e-04,5.119619e-05,5.814377e-05]
L2u_bdfpc_norot = [2.164921e-02,7.203294e-03,1.984132e-03,2.895039e-04,5.116211e-05,5.814293e-05]
L2u_ipcs        = [1.896775e-02,5.811281e-03,1.527787e-03,2.074083e-04,4.378448e-05,6.211521e-05]
L2u_ipcs_abcn   = [1.896775e-02,5.811282e-03,1.527788e-03,2.074086e-04,4.378468e-05,6.211526e-05]

L2p_bdfpc       = [1.913520e-02,7.235445e-03,1.708302e-03,2.476892e-04,2.726677e-05,3.256632e-05]
L2p_bdfpc_norot = [2.010053e-02,6.557816e-03,1.790743e-03,2.611678e-04,3.027999e-05,3.169686e-05]
L2p_ipcs        = [1.646958e-02,5.192048e-03,1.378414e-03,1.882430e-04,1.348327e-05,3.631995e-05]
L2p_ipcs_abcn   = [1.646958e-02,5.192048e-03,1.378414e-03,1.882431e-04,1.348329e-05,3.631992e-05]



plt.figure(1) # Plotting only IPCS errors (none rotational form)
plt.title('IPCS temporal errors (none rotational form)')
plt.loglog(dt,L2u_ipcs,'-r',lw=1, label='L2 V (P1P1) (BC1)')
plt.loglog(dt,L2p_ipcs,'-g',lw=2, label='L2 P (P1P1) (BC1)')
plt.loglog([dt[0], dt[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 2*abs(math.log10(dt[0])-math.log10(dt[-1]))) ],
           'k--', label='slope=2')

plt.figure(2) # Plotting only IPCS_ABCN errors (none rotational form)
plt.title('IPCS temporal errors (none rotational form)')
plt.loglog(dt,L2u_ipcs_abcn,'-r',lw=1, label='L2 V (P1P1) (BC1)')
plt.loglog(dt,L2p_ipcs_abcn,'-g',lw=2, label='L2 P (P1P1) (BC1)')
plt.loglog([dt[0], dt[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 2*abs(math.log10(dt[0])-math.log10(dt[-1]))) ],
           'k--', label='slope=2')

plt.figure(3) # Plotting only BDFPC_noR errror (none rotational form)
plt.title('BDFPC temporal errors (none rotational form)')
plt.loglog(dt,L2u_bdfpc_norot,'-r',lw=1, label='L2 V (P1P1) (BC1)')
plt.loglog(dt,L2p_bdfpc_norot,'-g',lw=2, label='L2 P (P1P1) (BC1)')
plt.loglog([dt[0], dt[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 2*abs(math.log10(dt[0])-math.log10(dt[-1]))) ],
           'k--', label='slope=2')

plt.figure(4) # Plotting only BDFPC_R errror (rotational form)
plt.title('BDFPC temporal errors (rotational form)')
plt.loglog(dt,L2u_bdfpc,'-r',lw=1, label='L2 V (P1P1) (BC1)')
plt.loglog(dt,L2p_bdfpc,'-g',lw=1, label='L2 P (P1P1) (BC1)')
plt.loglog([dt[0], dt[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 2*abs(math.log10(dt[0])-math.log10(dt[-1]))) ],
           'k--', label='slope=2')


plt.figure(1)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('error')
plt.xlim(2e-3, 2e-1)
plt.ylim(2e-6, 1e0)
plt.legend()

plt.figure(2)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('error')
plt.xlim(2e-3, 2e-1)
plt.ylim(2e-6, 3)
plt.legend()

plt.figure(3)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('error')
plt.xlim(2e-3, 2e-1)
plt.ylim(2e-6, 1e0)
plt.legend()

plt.figure(4)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('error')
plt.xlim(2e-3, 2e-1)
plt.ylim(2e-6, 1e0)
plt.legend()

plt.show()
