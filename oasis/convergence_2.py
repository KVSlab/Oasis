import math
import sys
import re
import numpy as np
import matplotlib.pyplot as plt

from IPython import embed

################################################################################
# Reading text file
text   = open("MMS_output_unitsq_dt_all.txt", "r").read()
number = "([0-9]+.[0-9]+e[+-][0-9]+)"
word   = "(\S+)"
match = re.findall("Scheme " + word +
                 "\nT      " + number +
                 "\ndt     " + number +
                 "\ndx     " + number +
                 "\nL2 norm \(ux-uxmms\) " + number +
                 "\nL2 norm \(p-pmms\)   " + number +
                 "\nH1 norm \(p-pmms\)   " + number, text)

# Arrange results by solvers into lists
dt_ipcs         = []
dt_ipcs_abcn    = []
dt_bdfpc        = []
dt_bdfpc_norot  = []
dx_ipcs         = []
dx_ipcs_abcn    = []
dx_bdfpc        = []
dx_bdfpc_norot  = []
L2u_ipcs        = []
L2u_ipcs_abcn   = []
L2u_bdfpc       = []
L2u_bdfpc_norot = []
L2p_ipcs        = []
L2p_ipcs_abcn   = []
L2p_bdfpc       = []
L2p_bdfpc_norot = []
H1p_ipcs        = []
H1p_ipcs_abcn   = []
H1p_bdfpc       = []
H1p_bdfpc_norot = []

for i in range(len(match)):
    solver = str(match[i][0])
    if solver=='IPCS':
        dt_ipcs.append(float(match[i][2]))
        dx_ipcs.append(float(match[i][3]))
        L2u_ipcs.append(float(match[i][4]))
        L2p_ipcs.append(float(match[i][5]))
        H1p_ipcs.append(float(match[i][6]))
    if solver=='IPCS_ABCN':
        dt_ipcs_abcn.append(float(match[i][2]))
        dx_ipcs_abcn.append(float(match[i][3]))
        L2u_ipcs_abcn.append(float(match[i][4]))
        L2p_ipcs_abcn.append(float(match[i][5]))
        H1p_ipcs_abcn.append(float(match[i][6]))
    if solver=='BDFPC_norot':
        dt_bdfpc_norot.append(float(match[i][2]))
        dx_bdfpc_norot.append(float(match[i][3]))
        L2u_bdfpc_norot.append(float(match[i][4]))
        L2p_bdfpc_norot.append(float(match[i][5]))
        H1p_bdfpc_norot.append(float(match[i][6]))
    elif solver=='BDFPC':
        dt_bdfpc.append(float(match[i][2]))
        dx_bdfpc.append(float(match[i][3]))
        L2u_bdfpc.append(float(match[i][4]))
        L2p_bdfpc.append(float(match[i][5]))
        H1p_bdfpc.append(float(match[i][6]))


plt.figure(1) # Plotting only IPCS errors (none rotational form)
plt.title('IPCS temporal errors (none rotational form)')
plt.loglog(dt_ipcs[0:7],L2u_ipcs[0:7],'-r',lw=1, label='L2 V (P1P1) (BC1)')
plt.loglog(dt_ipcs[0:7],L2p_ipcs[0:7],'-g',lw=2, label='L2 P (P1P1) (BC1)')
plt.loglog(dt_ipcs[7::],L2u_ipcs[7::],'-rd',lw=1, label='L2 V (P2P1) (BC1)')
plt.loglog(dt_ipcs[7::],L2p_ipcs[7::],'-gd',lw=2, label='L2 P (P2P1) (BC1)')
plt.loglog([dt_ipcs[0], dt_ipcs[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 1*abs(math.log10(dt_ipcs[0])-math.log10(dt_ipcs[-1]))) ],
           'k--', label='slope=1')

plt.figure(2) # Plotting only IPCS_ABCN errors (none rotational form)
plt.title('IPCS temporal errors (none rotational form)')
plt.loglog(dt_ipcs_abcn[0:7],L2u_ipcs_abcn[0:7],'-r',lw=1, label='L2 V (P1P1) (BC1)')
plt.loglog(dt_ipcs_abcn[0:7],L2p_ipcs_abcn[0:7],'-g',lw=2, label='L2 P (P1P1) (BC1)')
plt.loglog(dt_ipcs_abcn[7:14],L2u_ipcs_abcn[7:14],'-rd',lw=1, label='L2 V (P2P1) (BC1)')
plt.loglog(dt_ipcs_abcn[7:14],L2p_ipcs_abcn[7:14],'-gd',lw=2, label='L2 P (P2P1) (BC1)')
plt.loglog(dt_ipcs_abcn[14:21],L2u_ipcs_abcn[14:21],'-ro',lw=1, label='L2 V (P2P1) (BC2)')
plt.loglog(dt_ipcs_abcn[14:21],L2p_ipcs_abcn[14:21],'-go',lw=2, label='L2 P (P2P1) (BC2)')
plt.loglog(dt_ipcs_abcn[21::],L2u_ipcs_abcn[21::],'-r+',lw=1, label='L2 V (P2P1) (BC3)')
plt.loglog(dt_ipcs_abcn[21::],L2p_ipcs_abcn[21::],'-g+',lw=2, label='L2 P (P2P1) (BC3)')
plt.loglog([dt_ipcs_abcn[0], dt_ipcs_abcn[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 1*abs(math.log10(dt_ipcs_abcn[0])-math.log10(dt_ipcs_abcn[-1]))) ],
           'k--', label='slope=1')

plt.figure(3) # Plotting only BDFPC_noR errror (none rotational form)
plt.title('BDFPC temporal errors (none rotational form)')
plt.loglog(dt_bdfpc_norot[0:7],L2u_bdfpc_norot[0:7],'-r',lw=1, label='L2 V (P1P1) (BC1)')
plt.loglog(dt_bdfpc_norot[0:7],L2p_bdfpc_norot[0:7],'-g',lw=2, label='L2 P (P1P1) (BC1)')
plt.loglog(dt_bdfpc_norot[7::],L2u_bdfpc_norot[7::],'-rd',lw=1, label='L2 V (P2P1) (BC1)')
plt.loglog(dt_bdfpc_norot[7::],L2p_bdfpc_norot[7::],'-gd',lw=2, label='L2 P (P2P1) (BC1)')
plt.loglog([dt_bdfpc_norot[0], dt_bdfpc_norot[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 1*abs(math.log10(dt_bdfpc_norot[0])-math.log10(dt_bdfpc_norot[-1]))) ],
           'k--', label='slope=1')

plt.figure(4) # Plotting only BDFPC_R errror (rotational form)
plt.title('BDFPC temporal errors (rotational form)')
plt.loglog(dt_bdfpc[0:7],L2u_bdfpc[0:7],'-r',lw=1, label='L2 V (P1P1) (BC1)')
plt.loglog(dt_bdfpc[0:7],L2p_bdfpc[0:7],'-g',lw=1, label='L2 P (P1P1) (BC1)')
plt.loglog(dt_bdfpc[7::],L2u_bdfpc[7::],'-r',lw=2, label='L2 V (P2P1) (BC1)')
plt.loglog(dt_bdfpc[7::],L2p_bdfpc[7::],'-gd',lw=2, label='L2 P (P2P1) (BC1)')
plt.loglog([dt_bdfpc[0], dt_bdfpc[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 1*abs(math.log10(dt_bdfpc[0])-math.log10(dt_bdfpc[-1]))) ],
           'k--', label='slope=1')



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
