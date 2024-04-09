from qiskit import QuantumCircuit

######## Circuito de ejemplo

circuit = QuantumCircuit(3)
circuit.h(0)
circuit.h(1)
circuit.measure_all()

########################### Samplers ###########################

from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.least_busy(simulator=False, operational=True)
#backend = service.backend("ibm_osaka")

pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(circuit)

sampler = Sampler(backend)
sampler.options.default_shots = 1024

result = sampler.run([isa_circuit]).result()
for idx, pub_result in enumerate(result):
    print(f"Sample data for pub {idx}: {pub_result.data.meas.get_counts()}")
