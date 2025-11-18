def nodal_energy(x, f=1.0, v=1.0, Z_N=1e-51):
    import math
    if x <= 0:
        return 0.0
    try:
        return f * math.sqrt(v * math.log(x / Z_N))
    except ValueError:
        return 0.0

