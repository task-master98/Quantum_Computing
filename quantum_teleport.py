import cirq as cq
from cirq import final_wavefunction
import numpy as np
import random

def init(qubit_count=3):
    q0, q1, q2 = cq.LineQubit.range(qubit_count)
    return q0, q1, q2

def create_teleportation_circuit(q0, q1, q2, ranX, ranY):
    msg, alice, bob = q0, q1, q2
    circuit = cq.Circuit()
    circuit.append([cq.H(alice), cq.CNOT(alice, bob)])
    circuit.append([cq.X(msg)**ranX, cq.Y(msg)**ranY], strategy=cq.InsertStrategy.NEW_THEN_INLINE)
    circuit.append([cq.CNOT(msg, alice), cq.H(msg)])
    circuit.append(cq.measure(msg, alice))
    circuit.append([cq.CNOT(alice, bob), cq.CZ(msg, bob)])
    return circuit

def simulate_circuit(circuit):
    sim = cq.Simulator()
    result = sim.simulate(circuit)
     
    
    return result

def main():
    msg, bob, alice = init()
    ranX = random.random()
    ranY = random.random()
    q0 = cq.LineQubit(0)
    sim = cq.Simulator()
    message = sim.simulate(cq.Circuit([cq.X(q0)**ranX, cq.Y(q0)**ranY]))
    expected = message.bloch_vector_of(q0)
    
    circuit = create_teleportation_circuit(msg, alice, bob, ranX, ranY)
    result = simulate_circuit(circuit)
    final_vector = result.bloch_vector_of(bob)
    print(circuit)
    print(expected)
    print(final_vector)

if __name__ == '__main__':
    main()

