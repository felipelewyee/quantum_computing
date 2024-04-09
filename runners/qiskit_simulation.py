from qiskit import QuantumCircuit

######## Circuito de ejemplo

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

########################### Samplers ###########################

######## Sampler Qiskit

print()
print("Sampler de Qiskit")

from qiskit.primitives import Sampler
results = Sampler().run(circuit).result()
print(results)

######## Sampler local

print()
print("Sampler con Local IBM Runtime")

from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit_ibm_runtime.fake_provider import FakeMontrealV2
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

backend = FakeMontrealV2()
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_qc = pm.run(circuit)
sampler = Sampler(backend)

result = sampler.run([isa_qc]).result()
for idx, pub_result in enumerate(result):
    print(f"Sample data for pub {idx}: {pub_result.data.meas.get_counts()}")

######## Sampler online (Será descontinuado pronto)

print()
print("Sampler con IBM_Quantum Runtime")

from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# Remember you need to have a token saved, or write it as an argument of QiskitRuntimeService
service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.backend("ibmq_qasm_simulator")
 
sampler = Sampler(backend)
job = sampler.run([circuit])
result = job.result()
for idx, pub_result in enumerate(result):
    print(f"Sample data for pub {idx}: {pub_result.data.meas.get_counts()}")
