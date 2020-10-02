import cirq as cq
import numpy as np

# def main():
#     qubit = cq.LineQubit.range(4)
#     a = ((np.random.rand(4))*4)
    
#     circuit = cq.Circuit()
#     for theta, q in zip(*[a, qubit]):
#         circuit.append(cq.rx(theta).on(q))

#     for i, q in enumerate(qubit):
#         if i == 0:
#             circuit.append(cq.CZ(q, q+1), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
#             circuit.append(cq.CZ(q, q+2), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
#             circuit.append(cq.CZ(q, q+3), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
#         elif i == 1:
#             circuit.append(cq.CZ(q, q+1), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
#             circuit.append(cq.CZ(q, q+2), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
#         elif i == 2:
#             circuit.append(cq.CZ(q, q+1), strategy=cq.InsertStrategy.NEW_THEN_INLINE)
            

#         else:
#             break
        

#     print(circuit)
#     # sim_result = simulation(circuit, 20)
    

# def simulation(circuit, repetitions):
#     sim = cq.Simulator()
#     result = sim.run(circuit, repetitions=repetitions)
#     return result


# if __name__ == '__main__':
#     main()




a = np.random.rand(4, 4)
print(a)
print(a[:, 0])