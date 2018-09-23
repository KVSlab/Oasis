#python NSfracStep.py problem=MMS N=50 dt=$1 T=0$(expr 20*$1 | bc) solver=IPCS


python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160 dt=0.2 T=1 solver=BDFPC
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.2 T=1 solver=BDFPC_norot
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.2 T=1 solver=IPCS
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.2 T=1 solver=IPCS_ABCN

python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.1 T=1 solver=BDFPC
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.1 T=1 solver=BDFPC_norot
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.1 T=1 solver=IPCS
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.1 T=1 solver=IPCS_ABCN

python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.05 T=1 solver=BDFPC
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.05 T=1 solver=BDFPC_norot
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.05 T=1 solver=IPCS
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.05 T=1 solver=IPCS_ABCN

python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.02 T=1 solver=BDFPC
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.02 T=1 solver=BDFPC_norot
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.02 T=1 solver=IPCS
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.02 T=1 solver=IPCS_ABCN

python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.01 T=1 solver=BDFPC
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.01 T=1 solver=BDFPC_norot
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.01 T=1 solver=IPCS
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.01 T=1 solver=IPCS_ABCN

python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.005 T=1 solver=BDFPC
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.005 T=1 solver=BDFPC_norot
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.005 T=1 solver=IPCS
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.005 T=1 solver=IPCS_ABCN

python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.002 T=1 solver=BDFPC
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.002 T=1 solver=BDFPC_norot
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.002 T=1 solver=IPCS
python NSfracStep.py problem=TaylorGreen2D velocity_degree=1 Nx=160 Ny=160  dt=0.002 T=1 solver=IPCS_ABCN



# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.2 T=1 solver=BDFPC
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.2 T=1 solver=BDFPC_norot
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.2 T=1 solver=IPCS
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.2 T=1 solver=IPCS_ABCN
#
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.1 T=1 solver=BDFPC
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.1 T=1 solver=BDFPC_norot
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.1 T=1 solver=IPCS
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.1 T=1 solver=IPCS_ABCN
#
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.05 T=1 solver=BDFPC
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.05 T=1 solver=BDFPC_norot
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.05 T=1 solver=IPCS
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.05 T=1 solver=IPCS_ABCN
#
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.02 T=1 solver=BDFPC
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.02 T=1 solver=BDFPC_norot
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.02 T=1 solver=IPCS
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.02 T=1 solver=IPCS_ABCN
#
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.01 T=1 solver=BDFPC
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.01 T=1 solver=BDFPC_norot
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.01 T=1 solver=IPCS
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.01 T=1 solver=IPCS_ABCN
#
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.005 T=1 solver=BDFPC
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.005 T=1 solver=BDFPC_norot
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.005 T=1 solver=IPCS
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.005 T=1 solver=IPCS_ABCN
#
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.002 T=1 solver=BDFPC
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.002 T=1 solver=BDFPC_norot
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.002 T=1 solver=IPCS
# python NSfracStep.py problem=TaylorGreen2D velocity_degree=2 Nx=160 Ny=160  dt=0.002 T=1 solver=IPCS_ABCN
#
#
#
# python NSfracStep.py problem=MMS_bc2 velocity_degree=2 Nx=160 Ny=160  dt=0.2 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc2 velocity_degree=2 Nx=160 Ny=160  dt=0.1 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc2 velocity_degree=2 Nx=160 Ny=160  dt=0.05 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc2 velocity_degree=2 Nx=160 Ny=160  dt=0.02 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc2 velocity_degree=2 Nx=160 Ny=160  dt=0.01 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc2 velocity_degree=2 Nx=160 Ny=160  dt=0.005 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc2 velocity_degree=2 Nx=160 Ny=160  dt=0.002 T=1 solver=IPCS_ABCN
#
#
# python NSfracStep.py problem=MMS_bc3 velocity_degree=2 Nx=160 Ny=160  dt=0.2 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc3 velocity_degree=2 Nx=160 Ny=160  dt=0.1 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc3 velocity_degree=2 Nx=160 Ny=160  dt=0.05 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc3 velocity_degree=2 Nx=160 Ny=160  dt=0.02 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc3 velocity_degree=2 Nx=160 Ny=160  dt=0.01 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc3 velocity_degree=2 Nx=160 Ny=160  dt=0.005 T=1 solver=IPCS_ABCN
# python NSfracStep.py problem=MMS_bc3 velocity_degree=2 Nx=160 Ny=160  dt=0.002 T=1 solver=IPCS_ABCN
