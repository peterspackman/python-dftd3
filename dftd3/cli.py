import argparse
import numpy as np
import logging
from dftd3 import d3_correction

LOG = logging.getLogger(__name__)

BOHR = 0.5291772105638411

elements = [
    "H ",                                                                                "He", 
    "Li","Be",                                                  "B ","C ","N ","O ","F ","Ne", 
    "Na","Mg",                                                  "Al","Si","P ","S ","Cl","Ar", 
    "K ","Ca","Sc","Ti","V ","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr", 
    "Rb","Sr","Y ","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I ","Xe", 
    "Cs","Ba","La",     "Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu", 
                   "Hf","Ta","W ","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn", 
    "Fr","Ra","Ac",     "Th","Pa","U ","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr", 
                   "Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Ut","Fl","Up","Lv","Us","Uo"  
]

def parse_xyz(lines):
    n = 0
    total_lines = len(lines)
    num, comment, *atom_lines = lines
    n = int(num.strip())
    if len(lines) != n + 2:
        LOG.warn('Incorrect number of lines in file')

    coords = np.zeros(3 * n, dtype=float).reshape(n, 3)
    atoms = np.zeros(n, dtype=int)

    for i, line in enumerate(atom_lines):
        symbol, x, y, z = line.strip().split()
        atoms[i] = elements.index(symbol) + 1
        coords[i, :] = [float(x), float(y), float(z)]
    return atoms, coords


def read_xyz(filename):
    LOG.debug('Reading lines from %s', filename)
    with open(filename) as f:
        return f.readlines()


def main():
    import time
    parser = argparse.ArgumentParser()
    parser.add_argument('geometry',
                        help='Path of .xyz file for input')
    parser.add_argument('--log-level', default='WARN',
                        help='Level of log info to display')
    parser.add_argument('--functional', '-f', default='b-lyp',
                        help='Which parameterization to use')
    args = parser.parse_args()
    logging.basicConfig(level=args.log_level)

    lines = read_xyz(args.geometry)
    atoms, coords = parse_xyz(lines)
    e, forces = d3_correction(atoms, coords / BOHR, func=args.functional)
    print('Func\t', args.functional)
    print('E(disp)\t', e)

