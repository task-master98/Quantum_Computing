import cirq as cq
import numpy as np

q0, q1 = cq.LineQubit.range(2)

def create_deutch_circuit(q0, q1, oracle):
    circuit = cq.Circuit()
    circuit.append([cq.X(q1), cq.H(q1), cq.H(q0)], strategy=cq.InsertStrategy.INLINE)
    circuit.append(oracle)
    circuit.append([cq.H(q0), cq.measure(q0, key='result')])
    return circuit


def make_oracle(q0, q1, secret_function):

    if secret_function[0]:
        yield [cq.CNOT(q0, q1), cq.X(q1)] 

    if secret_function[1]:   
        yield cq.CNOT(q0, q1)

def simulate_circuit(circuit):
    sim = cq.Simulator()
    result = sim.run(circuit)
    return result

def main():
    secret_function = [np.random.randint(0, 2) for _ in range(2)]
    # secret_function = np.array([1, 1])
    oracle = make_oracle(q0, q1, secret_function)
    circuit = create_deutch_circuit(q0, q1, oracle)
    result= simulate_circuit(circuit)
    print(secret_function)
    print(circuit)
    print(result)


if __name__ == '__main__':
    main()


