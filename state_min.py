import cirq as cq
import numpy as np
import sympy as sp
import random

class LayerCircuit:

    def __init__(self, layers, qubit_count):
        self.layers = layers/2
        self.qubit_count = qubit_count
        self.qubit_in = cq.LineQubit.range(qubit_count)
    

    def layer_odd(self):
        circuit = cq.Circuit()
        a, b, c, d = sp.symbols('a b c d')
        circuit.append(cq.rx(a).on(self.qubit_in[0]))
        circuit.append(cq.rx(b).on(self.qubit_in[1]))
        circuit.append(cq.rx(c).on(self.qubit_in[2]))
        circuit.append(cq.rx(d).on(self.qubit_in[3]))
      
        return circuit
    
    def layer_even(self):
        circuit = cq.Circuit()
        a, b, c, d = sp.symbols('a b c d')
        circuit.append(cq.rx(a).on(self.qubit_in[0]))
        circuit.append(cq.rx(b).on(self.qubit_in[1]))
        circuit.append(cq.rx(c).on(self.qubit_in[2]))
        circuit.append(cq.rx(d).on(self.qubit_in[3]))
        
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
        a, b, c, d = sp.symbols('a b c d')
        for _ in range(int(2*self.layers)):
            parameters = {
                a: random.uniform(0, 1),
                b: random.uniform(0, 1),
                c: random.uniform(0, 1),
                d: random.uniform(0, 1)
            }
            resolver = cq.ParamResolver(parameters)
            odd_circuit = self.layer_odd()
            evn_circuit = self.layer_even()
            circuit.append([odd_circuit, evn_circuit], strategy=cq.InsertStrategy.NEW_THEN_INLINE)
            trial_results = cq.Simulator().simulate(circuit, resolver)
            state_vec = trial_results._final_simulator_state
           
            
        return state_vec.state_vector

    def simulate_layer_circuit(self, circuit):
        simulator  = cq.Simulator()
        trial_results = simulator.simulate(circuit)
        state_vec = trial_results._final_simulator_state
        
        return state_vec.state_vector

    def find_distance(self, state_vector):
        dim = self.qubit_count**2
        random_init_vector = np.random.rand(dim)
        return np.linalg.norm(state_vector-random_init_vector)

    

  
    

layer_obj = LayerCircuit(2, 4)
block_circuit_obj = layer_obj.block_circuit()
# final_state = layer_obj.simulate_layer_circuit(block_circuit_obj)
# distance = layer_obj.find_distance(final_state)
print(block_circuit_obj)