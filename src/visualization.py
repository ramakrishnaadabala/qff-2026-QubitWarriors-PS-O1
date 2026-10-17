"""
src/visualization.py
Generates publication-ready figures for hardware topologies, graph instances, and results.
"""
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_graph_instance(graph, filename="graph_instance.png"):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph, seed=42)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title("Max-Cut Graph Instance")
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

def plot_hardware_topology(cmap, title, filename):
    plt.figure(figsize=(6, 6))
    G = nx.Graph(cmap.get_edges())
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=800, font_weight='bold')
    plt.title(title)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

def plot_metrics_comparison(metrics_A, metrics_B, filename="AB_tradeoffs_comparison.png"):
    df = pd.DataFrame([
        {'Processor': 'Processor A', **metrics_A},
        {'Processor': 'Processor B', **metrics_B}
    ])
    df_melted = df.melt(id_vars='Processor', var_name='Metric', value_name='Count')
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Metric', y='Count', hue='Processor', data=df_melted)
    plt.title("Transpilation Metrics Comparison (A vs B)")
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
