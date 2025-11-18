from .engine import nodal_energy

def nodal_map(values):
    """
    Aplica la ecuación nodal a una lista de valores.

    Ejemplo:
        nodal_map([0.1, 0.2, 0.5])
    """
    return [nodal_energy(v) for v in values]


def nodal_coherence(values):
    """
    Calcula una métrica simple de coherencia nodal:
    la varianza inversa de los valores energéticos.
    """
    import statistics

    energies = nodal_map(values)
    if not energies:
        return 0.0

    mean = statistics.mean(energies)
    variance = statistics.pvariance(energies)
    return mean / (1 + variance)
