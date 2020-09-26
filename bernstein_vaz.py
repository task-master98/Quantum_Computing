import cirq as cq
import numpy as np

def qubit_init(qubit_count):
    qubit_in = [cq.GridQubit(i, 0) for i in range(qubit_count)]
    qubit_out = cq.GridQubit(qubit_count, 0)
    return qubit_in, qubit_out

def create_oracle(secret_string, qubit_in, qubit_out):
    for qubit, bit in zip(*[qubit_in, secret_string]):
        if bit:
            yield cq.CNOT(qubit, qubit_out)

def create_bv_circuit(qubit_in, qubit_out, oracle):
    circuit = cq.Circuit()
    circuit.append([cq.X(qubit_out), cq.H(qubit_out), cq.H.on_each(*qubit_in)], strategy=cq.InsertStrategy.NEW_THEN_INLINE)
    circuit.append(oracle)
    circuit.append([cq.H.on_each(*qubit_in), cq.measure(*qubit_in, key='result')], strategy=cq.InsertStrategy.NEW_THEN_INLINE)
    return circuit

def simulate_circuit(circuit, sample_count):
    sim = cq.Simulator()
    result = sim.run(circuit, repetitions=sample_count)
    frequencies = result.histogram(key='result', fold_func=bitstring)
    most_common_bitstring = frequencies.most_common(1)[0][0]
    return result, most_common_bitstring

def bitstring(bits):
    return ''.join(str(int(b)) for b in bits)

def main(qubit_count):
    qubit_in, qubit_out = qubit_init(qubit_count)
    secret_string = [np.random.randint(0, 2) for _ in range(qubit_count)]
    oracle = create_oracle(secret_string, qubit_in, qubit_out)
    circuit = create_bv_circuit(qubit_in, qubit_out, oracle)
    _, most_common_bitstring = simulate_circuit(circuit, 100)
    print(secret_string)
    print(circuit)
    print(most_common_bitstring)
    print('Most common matches secret factors:\n{}'.format(
        most_common_bitstring == bitstring(secret_string)))

if __name__ == '__main__':
    main(8)
    
