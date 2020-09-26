import cirq as cq

def main():
    qubit = cq.GridQubit(0, 0)
    circuit = cq.Circuit()
    circuit.append(cq.X(qubit)**0.5)
    circuit.append(cq.measure(qubit, key='m'))
    print(circuit)
    sim_result = simulation(circuit, 20)
    print(sim_result)

def simulation(circuit, repetitions):
    sim = cq.Simulator()
    result = sim.run(circuit, repetitions=repetitions)
    return result


if __name__ == '__main__':
    main()




