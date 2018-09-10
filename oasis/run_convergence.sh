#python NSfracStep.py problem=MMS N=50 dt=$1 T=0$(expr 20*$1 | bc) solver=IPCS

python NSfracStep.py problem=MMS N=10 dt=0.01 T=1 solver=IPCS
python NSfracStep.py problem=MMS N=20 dt=0.01 T=1 solver=IPCS
python NSfracStep.py problem=MMS N=100 dt=0.01 T=1 solver=IPCS
python NSfracStep.py problem=MMS N=150 dt=0.01 T=1 solver=IPCS

python NSfracStep.py problem=MMS N=10 dt=0.01 T=1 solver=BDFPC
python NSfracStep.py problem=MMS N=20 dt=0.01 T=1 solver=BDFPC
python NSfracStep.py problem=MMS N=100 dt=0.01 T=1 solver=BDFPC
python NSfracStep.py problem=MMS N=150 dt=0.01 T=1 solver=BDFPC

python NSfracStep.py problem=MMS N=100 dt=0.3 T=1 solver=IPCS
python NSfracStep.py problem=MMS N=100 dt=0.1 T=1 solver=IPCS
python NSfracStep.py problem=MMS N=100 dt=0.03 T=1 solver=IPCS
python NSfracStep.py problem=MMS N=100 dt=0.01 T=1 solver=IPCS

python NSfracStep.py problem=MMS N=100 dt=0.3 T=1 solver=BDFPC
python NSfracStep.py problem=MMS N=100 dt=0.1 T=1 solver=BDFPC
python NSfracStep.py problem=MMS N=100 dt=0.03 T=1 solver=BDFPC
python NSfracStep.py problem=MMS N=100 dt=0.01 T=1 solver=BDFPC
