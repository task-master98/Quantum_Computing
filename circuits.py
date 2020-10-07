import cirq as cq
import numpy as np
import sympy as sp

def main():
    
    qubit = cq.LineQubit.range(4)
    a, b, c, d = sp.symbols('a b c d')
    circuit = cq.Circuit()
    circuit.append(cq.rx(a).on(qubit[0]))
    circuit.append(cq.rx(b).on(qubit[1]))
    circuit.append(cq.rx(c).on(qubit[2]))
    circuit.append(cq.rx(d).on(qubit[3]))

    for i, q in enumerate(qubit):
        if i == 0:
            circuit.append(cq.CZ(q, q+1), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
            circuit.append(cq.CZ(q, q+2), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
            circuit.append(cq.CZ(q, q+3), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
        elif i == 1:
            circuit.append(cq.CZ(q, q+1), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
            circuit.append(cq.CZ(q, q+2), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
        elif i == 2:
            circuit.append(cq.CZ(q, q+1), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
            

        else:
            break
        

    print(circuit)
    # sim_result = simulation(circuit, 20)
    

# def simulation(circuit, repetitions):
#     sim = cq.Simulator()
#     result = sim.run(circuit, repetitions=repetitions)
#     return result


if __name__ == '__main__':
    main()

# theta = sp.symbols('theta'*4)
# print(theta)


