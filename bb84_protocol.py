# bb84_protocol.py

import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator

def perform_bb84(num_qubits):
    """
    Performs the BB84 Quantum Key Distribution protocol.

    Args:
        num_qubits (int): The number of qubits (and bits) in the key.

    Returns:
        str: The sifted secret key shared between Alice and Bob.
    """
    print("--- Starting BB84 Protocol ---")

    # === 1. Alice's Setup ===
    # Alice generates her random bits and bases
    alice_bits = np.random.randint(2, size=num_qubits)
    alice_bases = np.random.randint(2, size=num_qubits) # 0 for Z-basis, 1 for X-basis
    print(f"Alice's initial bits: {''.join(map(str, alice_bits))}")
    print(f"Alice's chosen bases: {''.join(map(str, alice_bases))}")

    # === 2. Alice Prepares Qubits ===
    qc = QuantumCircuit(num_qubits)
    for i in range(num_qubits):
        # If bit is 1, apply X gate
        if alice_bits[i] == 1:
            qc.x(i)
        # If basis is X (1), apply H gate
        if alice_bases[i] == 1:
            qc.h(i)

    # === 3. Bob's Setup ===
    # Bob generates his random bases for measurement
    bob_bases = np.random.randint(2, size=num_qubits)
    print(f"Bob's chosen bases:   {''.join(map(str, bob_bases))}")

    # === 4. Bob Measures Qubits ===
    # Bob applies basis transformations before measuring
    for i in range(num_qubits):
        if bob_bases[i] == 1: # If Bob chooses X-basis, apply H gate
            qc.h(i)

    # Measure all qubits
    qc.measure_all()

    # === 5. Simulation ===
    # Run the circuit on a simulator
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1, memory=True)
    result = job.result()
    bob_bits_str = result.get_memory()[0]
    bob_bits = [int(bit) for bit in bob_bits_str[::-1]] # Reverse to match qubit order
    print(f"Bob's measured bits:  {''.join(map(str, bob_bits))}")


    # === 6. Sifting ===
    # Alice and Bob compare their bases to find the matching ones
    sifted_key = []
    for i in range(num_qubits):
        if alice_bases[i] == bob_bases[i]:
            sifted_key.append(alice_bits[i])

    sifted_key_str = ''.join(map(str, sifted_key))
    print(f"\nBases match at indices where Alice and Bob both chose the same basis.")
    print(f"Sifted key: {sifted_key_str}")
    print("--- BB84 Protocol Finished ---\n")
    
    return sifted_key_str

if __name__ == '__main__':
    # Run a test of the protocol
    shared_key = perform_bb84(num_qubits=20)
    print(f"Successfully generated a shared secret key of length {len(shared_key)}.")
