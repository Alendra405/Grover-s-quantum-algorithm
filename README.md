# Grover's Quantum Search Algorithm – Unstructured Database Search in Qiskit 🚀

This project implements **Grover's algorithm**, one of the most famous quantum algorithms, using Qiskit. It searches an unstructured database of 3 items ('a', 'b', 'c') and finds the target item ('b') with very high probability after just **one iteration**.

### Key Features
- Database represented as a Python dictionary with 3 elements.
- 2 qubits to encode indices (0 = 'a', 1 = 'b', 2 = 'c').
- Custom oracle that marks the target state (|01⟩ for 'b').
- Grover diffusion operator for amplitude amplification.
- Results visualized with a histogram showing strong concentration on the target state.

### Why It Matters
Grover's algorithm provides a **quadratic speedup** O(√N) over classical unstructured search O(N). While the classical approach may require up to N queries in the worst case, Grover needs only ≈ √N. This makes it valuable for optimization, cryptography (symmetric key search), and large-scale data problems.


<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/cfe46e26-3222-457b-bb6d-fac135782ccc" />
