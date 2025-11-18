import math
from . import Z_N

def nodal_energy(x, f=1.0, v=1.0):
    """
    Calcula la energía nodal según TTA–D10Z:

        E_x = f * sqrt(v * ln(x / Z_n))

    Donde x debe representar una magnitud medible:
    - intensidad señal
    - eficiencia
    - densidad nodal
    """
    if x <= 0:
        return 0.0

    try:
        return f * math.sqrt(v * math.log(x / Z_N))
    except ValueError:
        return 0.0
