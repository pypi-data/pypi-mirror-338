from .maplpy import *
__all__ = ['Constraint', 'DataFrame', 'MAPL', 'Objective', 'Tuple', 'Variable']

def run_mapl():
    import sys
    from maplpy import MAPL

    MAPL.startCmd(sys.argv[1:])
