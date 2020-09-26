import cirq as cq

q0, q1, q2 = [cq.GridQubit(i, 0) for i in range(3)]

def create_circuit(q0, q1, q2):
    circuit = cq.Circuit()
    circuit.append([cq.H(q0), cq.H(q1), cq.H(q2)])
    circuit.append(cq.CZ(q1, q2))
    circuit.append(cq.measure(q0, q1, q2, key='m'))
    return circuit

def simulate_circuit(circuit, repetitions, result_type=None):
    sim = cq.Simulator()
    res = sim.run(circuit, repetitions=repetitions)
    op_vec = sim.simulate(circuit)
    if result_type == 'output_vector':
        return op_vec
    else:
        return res

def main():
    circuit = create_circuit(q0, q1, q2)
    result = simulate_circuit(circuit, 1000, 'simulation')
    print(circuit)
    print(result.histogram(key='m'))

if __name__ == '__main__':
    main()




