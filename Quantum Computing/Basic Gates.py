import qiskit 
import pylatexenc
import qiskit_aer
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
"""
qc1= QuantumCircuit(1)

qc1.x(0)
qc1.z(0)
qc1.h(0)
qc1.draw('mpl')

statevector= Statevector(qc1)
print(statevector)"""

qc2= QuantumCircuit(2)

qc2.x(0)
qc2.cx(0,1)
qc2.cz(0,1)
qc2.h(1)

qc2.draw('mpl')
statevector=Statevector(qc2)
print(statevector)

plt.show()
