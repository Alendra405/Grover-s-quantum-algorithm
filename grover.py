from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np
database = {'a':0,'b':1,'c':2}
target_key = 'b'
target_index = database[target_key]

N = len(database)
n_qubits = int(np.ceil(np.log2(N)))
qc = QuantumCircuit(n_qubits)
qc.h(range(n_qubits))
iterations = 1
for _ in range(iterations):
    qc.x(1)
    qc.cz(0,1)
    qc.x(1)
    qc.h(range(n_qubits))
    qc.x(range(n_qubits))
    qc.cz(0,1)
    qc.x(range(n_qubits))
    qc.h(range(n_qubits))
qc.measure_all()
backend = AerSimulator()
job = backend.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

print(f"target index = {counts}")
print(f"target item {target_key} on {target_index} index ({bin(target_index)[2:].zfill(n_qubits)} binary) finded!")