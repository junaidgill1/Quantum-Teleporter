import os
from pyquil.gates import *
from pyquil.quil import Program 
from pyquil.api import QVMConnection 
API_KEY = "nmRPAVunQl19TtQz9eMd11iiIsArtUDTaEnsSV6u"
USER_ID = "2a712fab-4095-4342-87a2-811f8cba905e" 

with open(os.path.expanduser('~/.pyquil_config'), 'w') as f:
    f.write(PYQUIL_CONFIG)
    

def Teleport(p):
    p.inst(H(1), CNOT(1, 2))
    p.inst(CNOT(0,1))
    p.inst(H(0))
    p.measure(0,0)
    p.measure(1,1)
    p.if_then(1, X(2))
    p.if_then(0, Z(2))
    p.measure(2, 2)
    return p

qvm = QVMConnection()
p = Program(I(0))
p = Teleport(p)
print("Teleporting |0> state: {}".format(qvm.run(p, [2])))

p = Program(X(0))
p = Teleport(p)
print("Teleporting |1> state: {}".format(qvm.run(p, [2])))

p = Program(H(0))
p = Teleport(p)
results = qvm.run(p, [2],10)
print("Teleporting |+> Superposition state: {}".format(results))
print("Collapse to |0>:", results.count([0]))
print("Collapse to |1>:", results.count([1]))
#wave = qvm.wavefunction(ins,[2])
#print(wave)
#print(ins)
