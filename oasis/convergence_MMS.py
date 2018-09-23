import math
import sys
import re
import numpy as np
import matplotlib.pyplot as plt

from IPython import embed

################################################################################
# Reading text file
#text   = open("MMS_output_unitsq_dt_all.txt", "r").read()
#text   = open("MMS_Guermond_output_dt_all.txt", "r").read()
text   = open("MMS_output_dt_all.txt", "r").read()
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
dt_bdfpc_fast         = []
dt_ipcs_abcn    = []
dt_bdfpc        = []
dt_bdfpc_norot  = []
dx_bdfpc_fast         = []
dx_ipcs_abcn    = []
dx_bdfpc        = []
dx_bdfpc_norot  = []
L2u_bdfpc_fast        = []
L2u_ipcs_abcn   = []
L2u_bdfpc       = []
L2u_bdfpc_norot = []
L2p_bdfpc_fast        = []
L2p_ipcs_abcn   = []
L2p_bdfpc       = []
L2p_bdfpc_norot = []
H1p_bdfpc_fast        = []
H1p_ipcs_abcn   = []
H1p_bdfpc       = []
H1p_bdfpc_norot = []

for i in range(len(match)):
    solver = str(match[i][0])
    if solver=='BDFPC_Fast':
        dt_bdfpc_fast.append(float(match[i][2]))
        dx_bdfpc_fast.append(float(match[i][3]))
        L2u_bdfpc_fast.append(float(match[i][4]))
        L2p_bdfpc_fast.append(float(match[i][5]))
        H1p_bdfpc_fast.append(float(match[i][6]))
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
    if solver=='BDFPC':
        dt_bdfpc.append(float(match[i][2]))
        dx_bdfpc.append(float(match[i][3]))
        L2u_bdfpc.append(float(match[i][4]))
        L2p_bdfpc.append(float(match[i][5]))
        H1p_bdfpc.append(float(match[i][6]))


plt.figure(1) # Plotting MMS BC1 test P1P1
plt.title('MMS BC1 errors (P1P1)')
#plt.loglog(dt_bdfpc_fast[0:7],L2u_bdfpc_fast[0:7],'-r',lw=2, label='V (BDFPC_rot_fast)')
#plt.loglog(dt_bdfpc_fast[0:7],L2p_bdfpc_fast[0:7],'-rD',lw=1, label='P (BDFPC_rot_fast)')
plt.loglog(dt_bdfpc[0:7],L2u_bdfpc[0:7],'#cf0234',lw=2, label='V (BDFPC_rot)')
plt.loglog(dt_bdfpc[0:7],L2p_bdfpc[0:7],'#cf0234',marker='D',lw=1, label='P (BDFPC_rot)')
plt.loglog(dt_bdfpc_norot[0:7],L2u_bdfpc_norot[0:7],'#76cd26',lw=2, label='V (BDFPC_norot)')
plt.loglog(dt_bdfpc_norot[0:7],L2p_bdfpc_norot[0:7],'#76cd26',marker='D',lw=1, label='P (BDFPC_norot)')
plt.loglog(dt_ipcs_abcn[0:7],L2u_ipcs_abcn[0:7],'#02590f',lw=2, label='V (IPCS)')
plt.loglog(dt_ipcs_abcn[0:7],L2p_ipcs_abcn[0:7],'#02590f',marker='D',lw=1, label='P (IPCS)')
plt.loglog([dt_bdfpc_fast[0], dt_bdfpc_fast[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 2*abs(math.log10(dt_bdfpc_fast[0])-math.log10(dt_bdfpc_fast[-1]))) ],
           'k--')

plt.figure(2) # Plotting MMS BC1 test P2P1
plt.title('MMS BC1 errors (P2P1)')
#plt.loglog(dt_bdfpc_fast[7::],L2u_bdfpc_fast[7::],'-r',lw=1, label='V (BDFPC_rot_fast)')
#plt.loglog(dt_bdfpc_fast[7::],L2p_bdfpc_fast[7::],'-rD',lw=2, label='P (BDFPC_rot_fast)')
plt.loglog(dt_bdfpc[7::],L2u_bdfpc[7::],'#cf0234',lw=2, label='V (BDFPC_rot)')
plt.loglog(dt_bdfpc[7::],L2p_bdfpc[7::],'#cf0234',marker='D',lw=1, label='P (BDFPC_rot)')
plt.loglog(dt_bdfpc_norot[7::],L2u_bdfpc_norot[7::],'#76cd26',lw=2, label='V (BDFPC_norot)')
plt.loglog(dt_bdfpc_norot[7::],L2p_bdfpc_norot[7::],'#76cd26',marker='D',lw=1, label='P (BDFPC_norot)')
plt.loglog(dt_ipcs_abcn[7:14],L2u_ipcs_abcn[7:14],'#02590f',lw=2, label='V (IPCS)')
plt.loglog(dt_ipcs_abcn[7:14],L2p_ipcs_abcn[7:14],'#02590f',marker='D',lw=1, label='P (IPCS)')
plt.loglog([dt_bdfpc_fast[0], dt_bdfpc_fast[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 2*abs(math.log10(dt_bdfpc_fast[0])-math.log10(dt_bdfpc_fast[-1]))) ],
           'k--')

plt.figure(3)  # Plotting MMS BC2 test P2P1
plt.title('MMS BC2 errors (P2P1)')
plt.loglog(dt_ipcs_abcn[14:21],L2u_ipcs_abcn[14:21],'#02590f',lw=2, label='V (IPCS)')
plt.loglog(dt_ipcs_abcn[14:21],L2p_ipcs_abcn[14:21],'#02590f',marker='D',lw=1, label='P (IPCS)')
plt.loglog([dt_ipcs_abcn[0], dt_ipcs_abcn[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 2*abs(math.log10(dt_ipcs_abcn[0])-math.log10(dt_ipcs_abcn[-1]))) ],
           'k--')

plt.figure(4) # Plotting MMS BC3 test P2P1
plt.title('MMS BC3 errors (P2P1)')
plt.loglog(dt_ipcs_abcn[21::],L2u_ipcs_abcn[21::],'#02590f',lw=2, label='V (IPCS)')
plt.loglog(dt_ipcs_abcn[21::],L2p_ipcs_abcn[21::],'#02590f',marker='D',lw=1, label='P (IPCS)')
plt.loglog([dt_ipcs_abcn[0], dt_ipcs_abcn[-1]],
           [1e-2, math.pow(10, math.log10(1e-2) - 2*abs(math.log10(dt_ipcs_abcn[0])-math.log10(dt_ipcs_abcn[-1]))) ],
           'k--')


plt.figure(1)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('L2 error')
plt.xlim(2e-3, 2e-1)
plt.ylim(1e-6, 1e0)
plt.legend()
#plt.savefig('Error_MMS_BC1_P1P1.png', format='png', dpi=250)

plt.figure(2)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('L2 error')
plt.xlim(2e-3, 2e-1)
plt.ylim(1e-6, 1e0)
plt.legend()
#plt.savefig('Error_MMS_BC1_P2P1.png', format='png', dpi=250)

plt.figure(3)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('L2 error')
plt.xlim(2e-3, 2e-1)
plt.ylim(1e-6, 1e0)
plt.legend()
#plt.savefig('Error_MMS_BC2_P2P1.png', format='png', dpi=250)

plt.figure(4)
plt.grid(True,which="both",ls="-")
plt.xlabel('dt')
plt.ylabel('L2 error')
plt.xlim(2e-3, 2e-1)
plt.ylim(1e-6, 5)
plt.legend()
#plt.savefig('Error_MMS_BC3_P2P1.png', format='png', dpi=250)

plt.show()
