"""
src/metrics.py
Calculates evaluation metrics for the QAOA Max-Cut solutions.
"""
import numpy as np

def calculate_expectation(counts, problem):
    """Calculates the expectation value (average cut) from bitstring counts."""
    total_shots = sum(counts.values())
    expected_value = 0
    variance = 0
    
    # Calculate mean
    for bitstring, count in counts.items():
        prob = count / total_shots
        cut_val = problem.evaluate_bitstring(bitstring)
        expected_value += prob * cut_val
        
    # Calculate variance
    for bitstring, count in counts.items():
        prob = count / total_shots
        cut_val = problem.evaluate_bitstring(bitstring)
        variance += prob * (cut_val - expected_value)**2
        
    std_error = np.sqrt(variance / total_shots) if total_shots > 0 else 0
    return expected_value, variance, std_error

def calculate_approximation_ratio(expected_value, max_cut_value):
    """Calculates the approximation ratio."""
    if max_cut_value == 0:
        return 0
    return expected_value / max_cut_value

def calculate_optimal_probability(counts, optimal_bitstrings):
    """Calculates the probability of measuring an optimal ground state."""
    total_shots = sum(counts.values())
    opt_counts = sum(counts.get(bs, 0) for bs in optimal_bitstrings)
    return opt_counts / total_shots

def calculate_routing_overhead(transpiled_cx, logical_cx):
    """Calculates the CX overhead ratio."""
    if logical_cx == 0:
        return 1.0
    return transpiled_cx / logical_cx
