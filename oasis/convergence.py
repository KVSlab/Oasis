import math
import sys
import re
import numpy as np
import matplotlib.pyplot as plt

from IPython import embed

################################################################################
# Reading text file
#text   = open("MMS_output_P1P1_unitsq.txt", "r").read()
text   = open("MMS_output_P1P1_sq2.txt", "r").read()
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
dt_bdfpc        = []
dt_bdfpc_norot  = []
dx_ipcs         = []
dx_bdfpc        = []
dx_bdfpc_norot  = []
L2u_ipcs        = []
L2u_bdfpc       = []
L2u_bdfpc_norot = []
L2p_ipcs        = []
L2p_bdfpc       = []
L2p_bdfpc_norot = []
H1p_ipcs        = []
H1p_bdfpc       = []
H1p_bdfpc_norot = []

for i in range(len(match)):
    solver = str(match[i][0])
    if 'IPCS' in solver:
        dt_ipcs.append(float(match[i][2]))
        dx_ipcs.append(float(match[i][3]))
        L2u_ipcs.append(float(match[i][4]))
        L2p_ipcs.append(float(match[i][5]))
        H1p_ipcs.append(float(match[i][6]))
    if 'BDFPC_norot' in solver:
        dt_bdfpc_norot.append(float(match[i][2]))
        dx_bdfpc_norot.append(float(match[i][3]))
        L2u_bdfpc_norot.append(float(match[i][4]))
        L2p_bdfpc_norot.append(float(match[i][5]))
        H1p_bdfpc_norot.append(float(match[i][6]))
    elif 'BDFPC' in solver:
        dt_bdfpc.append(float(match[i][2]))
        dx_bdfpc.append(float(match[i][3]))
        L2u_bdfpc.append(float(match[i][4]))
        L2p_bdfpc.append(float(match[i][5]))
        H1p_bdfpc.append(float(match[i][6]))


plt.figure(1) # Plotting only IPCS errors (none rotational form)
plt.title('IPCS temporal errors (none rotational form)')
plt.loglog(dt_ipcs,L2u_ipcs,'-D', label='L2 V (P1P1)')
plt.loglog(dt_ipcs,L2p_ipcs,'-D', label='L2 P (P1P1)')
plt.loglog([dt_ipcs[0], dt_ipcs[-1]],
           [L2u_ipcs[0], math.pow(10, math.log10(L2u_ipcs[0]) - 1*abs(math.log10(dt_ipcs[0])-math.log10(dt_ipcs[-1]))) ],
           'k--')

plt.figure(2) # Plotting only BDFPC_noR errror (none rotational form)
plt.title('BDFPC temporal errors (none rotational form)')
tmp = 1
plt.loglog(dt_bdfpc_norot[(tmp-1)::tmp],L2u_bdfpc_norot[(tmp-1)::tmp],'-d', label='L2 V (P1P1)')
plt.loglog(dt_bdfpc_norot[(tmp-1)::tmp],L2p_bdfpc_norot[(tmp-1)::tmp],'-d', label='L2 P (P1P1)')
plt.loglog([dt_bdfpc_norot[0], dt_bdfpc_norot[-1]],
           [L2u_bdfpc_norot[tmp-1], math.pow(10, math.log10(L2u_bdfpc_norot[tmp-1]) - 1*abs(math.log10(dt_bdfpc_norot[0])-math.log10(dt_bdfpc_norot[-1]))) ],
           'k--')

plt.figure(3) # Plotting only BDFPC_R errror (rotational form)
plt.title('BDFPC temporal errors (rotational form)')
tmp = 1
plt.loglog(dt_bdfpc[(tmp-1)::tmp],L2u_bdfpc[(tmp-1)::tmp],'-d', label='L2 V (P1P1)')
plt.loglog(dt_bdfpc[(tmp-1)::tmp],L2p_bdfpc[(tmp-1)::tmp],'-d', label='L2 P (P1P1)')
plt.loglog([dt_bdfpc[0], dt_bdfpc[-1]],
           [L2u_bdfpc[tmp-1], math.pow(10, math.log10(L2u_bdfpc[tmp-1]) - 1*abs(math.log10(dt_bdfpc[0])-math.log10(dt_bdfpc[-1]))) ],
           'k--')



################################################################################
# Reading text file
#text   = open("MMS_output_P2P1_unitsq.txt", "r").read()
text   = open("MMS_output_P2P1_sq2.txt", "r").read()
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
dt_bdfpc        = []
dt_bdfpc_norot  = []
dx_ipcs         = []
dx_bdfpc        = []
dx_bdfpc_norot  = []
L2u_ipcs        = []
L2u_bdfpc       = []
L2u_bdfpc_norot = []
L2p_ipcs        = []
L2p_bdfpc       = []
L2p_bdfpc_norot = []
H1p_ipcs        = []
H1p_bdfpc       = []
H1p_bdfpc_norot = []

for i in range(len(match)):
    solver = str(match[i][0])
    if 'IPCS' in solver:
        dt_ipcs.append(float(match[i][2]))
        dx_ipcs.append(float(match[i][3]))
        L2u_ipcs.append(float(match[i][4]))
        L2p_ipcs.append(float(match[i][5]))
        H1p_ipcs.append(float(match[i][6]))
    if 'BDFPC_norot' in solver:
        dt_bdfpc_norot.append(float(match[i][2]))
        dx_bdfpc_norot.append(float(match[i][3]))
        L2u_bdfpc_norot.append(float(match[i][4]))
        L2p_bdfpc_norot.append(float(match[i][5]))
        H1p_bdfpc_norot.append(float(match[i][6]))
    elif 'BDFPC' in solver:
        dt_bdfpc.append(float(match[i][2]))
        dx_bdfpc.append(float(match[i][3]))
        L2u_bdfpc.append(float(match[i][4]))
        L2p_bdfpc.append(float(match[i][5]))
        H1p_bdfpc.append(float(match[i][6]))


plt.figure(1) # Plotting only IPCS errors (none rotational form)
plt.title('IPCS temporal errors (none rotational form)')
plt.loglog(dt_ipcs,L2u_ipcs,'-D', label='L2 V (P2P1)')
plt.loglog(dt_ipcs,L2p_ipcs,'-D', label='L2 P (P2P1)')
plt.loglog([dt_ipcs[0], dt_ipcs[-1]],
           [L2p_ipcs[0], math.pow(10, math.log10(L2p_ipcs[0]) - 2*abs(math.log10(dt_ipcs[0])-math.log10(dt_ipcs[-1]))) ],
           'k--')

plt.figure(2) # Plotting only BDFPC_noR errror (none rotational form)
plt.title('BDFPC temporal errors (none rotational form)')
tmp = 1
plt.loglog(dt_bdfpc_norot[(tmp-1)::tmp],L2u_bdfpc_norot[(tmp-1)::tmp],'-d', label='L2 V (P2P1)')
plt.loglog(dt_bdfpc_norot[(tmp-1)::tmp],L2p_bdfpc_norot[(tmp-1)::tmp],'-d', label='L2 P (P2P1)')
plt.loglog([dt_bdfpc_norot[0], dt_bdfpc_norot[-1]],
           [L2u_bdfpc_norot[tmp-1], math.pow(10, math.log10(L2u_bdfpc_norot[tmp-1]) - 2*abs(math.log10(dt_bdfpc_norot[0])-math.log10(dt_bdfpc_norot[-1]))) ],
           'k--')

plt.figure(3) # Plotting only BDFPC_R errror (rotational form)
plt.title('BDFPC temporal errors (rotational form)')
tmp = 1
plt.loglog(dt_bdfpc[(tmp-1)::tmp],L2u_bdfpc[(tmp-1)::tmp],'-d', label='L2 V (P2P1)')
plt.loglog(dt_bdfpc[(tmp-1)::tmp],L2p_bdfpc[(tmp-1)::tmp],'-d', label='L2 P (P2P1)')
plt.loglog([dt_bdfpc[0], dt_bdfpc[-1]],
           [L2u_bdfpc[tmp-1], math.pow(10, math.log10(L2u_bdfpc[tmp-1]) - 2*abs(math.log10(dt_bdfpc[0])-math.log10(dt_bdfpc[-1]))) ],
           'k--')





plt.figure(1)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('error')
plt.xlim(3e-3, 2e-1)
plt.ylim(2e-6, 1e0)
plt.legend()

plt.figure(2)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('error')
plt.xlim(3e-3, 2e-1)
plt.ylim(2e-6, 1e0)
plt.legend()

plt.figure(3)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('error')
plt.xlim(3e-3, 2e-1)
plt.ylim(2e-6, 1e0)
plt.legend()


plt.show()
