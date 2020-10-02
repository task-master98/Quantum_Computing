import cirq as cq
import numpy as np

class LayerCircuit:

    def __init__(self, layers, qubit_count):
        self.layers = layers
        self.qubit_count = qubit_count
        self.qubit_in = cq.LineQubit.range(qubit_count)
        self.params = (np.random.rand(qubit_count))*4
        self.theta = (np.random.rand(qubit_count, 2*layers))*4

    def layer_odd(self, params):
        circuit = cq.Circuit()
        for theta, q in zip(*[params, self.qubit_in]):
            circuit.append(cq.rx(theta).on(q))
      
        return circuit
    
    def layer_even(self, params):
        circuit = cq.Circuit()
        for theta, q in zip(*[params, self.qubit_in]):
            circuit.append(cq.rx(theta).on(q))
        
        for i, q in enumerate(self.qubit_in):

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
            

        return circuit

    def block_circuit(self):
        circuit = cq.Circuit()
        index = 0
        for _ in range((self.theta.shape[1])):
            if index > self.layers:
                break
            circuit_odd = self.layer_odd(params=self.theta[:, index])
            circuit_evn = self.layer_even(params=self.theta[:, index+1])
            circuit.append([circuit_odd, circuit_evn], strategy=cq.InsertStrategy.NEW_THEN_INLINE)
            index += 2
            
        return circuit

    

layer_obj = LayerCircuit(2, 4)
block_circuit_obj = layer_obj.block_circuit()
print(block_circuit_obj)