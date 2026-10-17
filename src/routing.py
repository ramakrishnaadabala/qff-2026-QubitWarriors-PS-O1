"""
src/routing.py
Handles the transpilation of logical circuits onto hardware-specific coupling maps.
"""
from qiskit import transpile

def route_and_compile(logical_circuit, processor_backend, cmap):
    """
    Transpiles the circuit and calculates the routing overhead (SWAPs, Depth, CX count).
    """
    compiled_circuit = transpile(
        logical_circuit,
        backend=processor_backend,
        coupling_map=cmap,
        optimization_level=1,
        seed_transpiler=42
    )
    
    ops = compiled_circuit.count_ops()
    metrics = {
        'depth': compiled_circuit.depth(),
        'cx_count': ops.get('cx', 0),
        'swap_count': ops.get('swap', 0),
        'native_1q': ops.get('rz', 0) + ops.get('sx', 0) + ops.get('x', 0)
    }
    
    return compiled_circuit, metrics
