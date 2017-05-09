"""
Copyright (C) 2017, Peter Spackman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import numpy as np
from dftd3._d3 import d3

dft_dispersion_correction = d3.d3_calc
periodic_dispersion_correction = d3.periodic_d3_calc

versions = {
    'bj': 6, # DFT-D3 with Becke-Johnson damping parameters
    'zero': 5, # DFT-D3 with zero damping parameters
    'finite': 4, # DFT-D3 with Becke-Johnson finite-damping, variant 2 with their radii
    'none': 3, # DFT-D3 with no damping
    'D2': 2, # DFT-D2
}

# TODO parameters for other variants
# Parameters are as follows: (rs6, s18, rs18 ,s6)

parameters = {}

parameters['zero'] = {
    'slater-dirac-exchange': (0.999, -1.957, 0.697, 1.00),
    'blyp':                 (1.094, 1.6820, 1.000, 1.00),
    'bp':                   (1.139, 1.6830, 1.000, 1.00),
    'b97-d':                 (0.892, 0.9090, 1.000, 1.00),
    'revpbe':                (0.923, 1.0100, 1.000, 1.00),
    'pbe':                   (1.217, 0.7220, 1.000, 1.00),
    'pbesol':                (1.345, 0.6120, 1.000, 1.00),
    'rpw86-pbe':             (1.224, 0.9010, 1.000, 1.00),
    'rpbe':                  (0.872, 0.5140, 1.000, 1.00),
    'tpss':                  (1.166, 1.1050, 1.000, 1.00),
    'b3lyp':                (1.261, 1.7030, 1.000, 1.00),
    'pbe0':                  (1.287, 0.9280, 1.000, 1.00),
    'hse06':                 (1.129, 0.1090, 1.000, 1.00),
    'revpbe38':              (1.021, 0.8620, 1.000, 1.00),
    'pw6b95':                (1.532, 0.8620, 1.000, 1.00),
    'tpss0':                 (1.252, 1.2420, 1.000, 1.00),
    'b2plyp':               (1.427, 1.0220, 1.000, 0.64),
    'pwpb95':                (1.557, 0.7050, 1.000, 0.82),
    'b2gpplyp':             (1.586, 0.7600, 1.000, 0.56),
    'ptpss':                 (1.541, 0.8790, 1.000, 0.75),
    'hf':                    (1.158, 1.7460, 1.000, 1.00),
    'mpwlyp':                (1.239, 1.0980, 1.000, 1.00),
    'bpbe':                  (1.087, 2.0330, 1.000, 1.00),
    'bhlyp':                (1.370, 1.4420, 1.000, 1.00),
    'tpssh':                 (1.223, 1.2190, 1.000, 1.00),
    'pwb6k':                 (1.660, 0.5500, 1.000, 1.00),
    'b1b95':                 (1.613, 1.8680, 1.000, 1.00),
    'bop':                   (0.929, 1.9750, 1.000, 1.00),
    'olyp':                 (0.806, 1.7640, 1.000, 1.00),
    'opbe':                 (0.837, 2.0550, 1.000, 1.00),
    'ssb':                   (1.215, 0.6630, 1.000, 1.00),
    'revssb':                (1.221, 0.5600, 1.000, 1.00),
    'otpss':                 (1.128, 1.4940, 1.000, 1.00),
    'b3pw91':                (1.176, 1.7750, 1.000, 1.00),
    'revpbe0':               (0.949, 0.7920, 1.000, 1.00),
    'pbe38':                 (1.333, 0.9980, 1.000, 1.00),
    'mpw1b95':               (1.605, 1.1180, 1.000, 1.00),
    'mpwb1k':                (1.671, 1.0610, 1.000, 1.00),
    'bmk':                   (1.931, 2.1680, 1.000, 1.00),
    'camb3lyp':             (1.378, 1.2170, 1.000, 1.00),
    'lcwpbe':               (1.355, 1.2790, 1.000, 1.00),
    'm05':                   (1.373, 0.5950, 1.000, 1.00),
    'm052x':                 (1.417, 0.0000, 1.000, 1.00),
    'm06l':                  (1.581, 0.0000, 1.000, 1.00),
    'm06':                   (1.325, 0.0000, 1.000, 1.00),
    'm062x':                 (1.619, 0.0000, 1.000, 1.00),
    'm06hf':                 (1.446, 0.0000, 1.000, 1.00),
    'dftb3':                 (1.235, 0.6730, 1.000, 1.00),
    'hcth120':               (1.221, 1.2060, 1.000, 1.00),
    }

# D3(BJ) damping parameters
#                    (RS6    , S18    , RS18  , S6  )
parameters['bj'] = {
    'bp':           (0.39460, 3.28220, 4.8516, 1.00),
    'blyp':         (0.42980, 2.69960, 4.2359, 1.00),
    'revpbe':        (0.52380, 2.35500, 3.5016, 1.00),
    'rpbe':          (0.18200, 0.83180, 4.0094, 1.00),
    'b97d':         (0.55450, 2.26090, 3.2297, 1.00),
    'pbe':           (0.42890, 0.78750, 4.4407, 1.00),
    'rpw86pbe':     (0.46130, 1.38450, 4.5062, 1.00),
    'b3lyp':        (0.39810, 1.98890, 4.4211, 1.00),
    'tpss':          (0.45350, 1.94350, 4.4752, 1.00),
    'hf':            (0.33850, 0.91710, 2.8830, 1.00),
    'tpss0':         (0.37680, 1.25760, 4.5865, 1.00),
    'pbe0':          (0.41450, 1.21770, 4.8593, 1.00),
    'hse06':         (0.38300, 2.31000, 5.6850, 1.00),
    'revpbe38':      (0.43090, 1.47600, 3.9446, 1.00),
    'pw6b95':        (0.20760, 0.72570, 6.3750, 1.00),
    'b2plyp':       (0.30650, 0.91470, 5.0570, 0.64),
    'dsdblyp':      (0.00000, 0.21300, 6.0519, 0.50),
    'dsdblypfc':   (0.00090, 0.21120, 5.9807, 0.50),
    'bop':           (0.48700, 3.29500, 3.5043, 1.00),
    'mpwlyp':        (0.48310, 2.00770, 4.5323, 1.00),
    'olyp':         (0.52990, 2.62050, 2.8065, 1.00),
    'pbesol':        (0.44660, 2.94910, 6.1742, 1.00),
    'bpbe':          (0.45670, 4.07280, 4.3908, 1.00),
    'opbe':          (0.55120, 3.38160, 2.9444, 1.00),
    'ssb':           (-0.0952, -0.1744, 5.2170, 1.00),
    'revssb':        (0.47200, 0.43890, 4.0986, 1.00),
    'otpss':         (0.46340, 2.74950, 4.3153, 1.00),
    'b3pw91':        (0.43120, 2.85240, 4.4693, 1.00),
    'bhlyp':        (0.27930, 1.03540, 4.9615, 1.00),
    'revpbe0':       (0.46790, 1.75880, 3.7619, 1.00),
    'tpssh':         (0.45290, 2.23820, 4.6550, 1.00),
    'mpw1b95':       (0.19550, 1.05080, 6.4177, 1.00),
    'pwb6k':         (0.18050, 0.93830, 7.7627, 1.00),
    'b1b95':         (0.20920, 1.45070, 5.5545, 1.00),
    'bmk':           (0.19400, 2.08600, 5.9197, 1.00),
    'camb3lyp':     (0.37080, 2.06740, 5.4743, 1.00),
    'lcwpbe':       (0.39190, 1.85410, 5.0897, 1.00),
    'b2gpplyp':     (0.00000, 0.25970, 6.3332, 0.56),
    'ptpss':         (0.00000, 0.28040, 6.5745, 0.75),
    'pwpb95':        (0.00000, 0.29040, 7.3141, 0.82),
    'hf/mixed':      (0.56070, 3.90270, 4.5622, 1.00),
    'hf/sv':         (0.42490, 2.18490, 4.2783, 1.00),
    'hf/minis':      (0.17020, 0.98410, 3.8506, 1.00),
    'b3lyp/6-31gd': (0.50140, 4.06720, 4.8409, 1.00),
    'hcth120':       (0.35630, 1.08210, 4.3359, 1.00),
    'dftb3':         (0.74610, 3.20900, 4.1906, 1.00),
}


# TODO references
def d3_correction(atomic_numbers, atomic_positions, func='pbe', variant='bj'):
    """Calculate the D2/D3 dispersion correction for a given set of atoms.

    Grimme et al. dispersion corrections.

    Parameters
    ----------

    atomic_numbers : array_like 
        A set of atomic numbers of shape ``(N,) ``.  
    atomic_positions : array_like
        Set of atomic positions in atomic units (bohr) 
        of shape ``(N,3)``

    func : {'pbe'}, optional
        Choice of functional to use for this calculation (as given in)

    variant : {'bj', 'zero', 'd2'}, optional
        Choice of functional to use for this calculation (as given in)


    Returns
    -------
    results : dict
        The dispersion energy of the system (`edisp`) and the force on
        each atom (`grad`)
    

    Example:

    >>> n = [8, 1, 1]
    >>> xyz = [[0, 0, 0.222590804],[0, 1.42759927, -0.89036525],[0, -1.42759927, -0.89036525]]
    >>> edisp, _ = d3_correction(n, xyz, func='b-lyp')
    >>> edisp
    -0.0007192450505684787
    >>> _, forces = d3_correction(n, xyz, func='ptpss')
    >>> forces
    array([[  0.00000000e+00,   0.00000000e+00,   0.00000000e+00],
           [  0.00000000e+00,  -1.45090469e-08,   1.45090469e-08],
           [ -6.01894727e-07,   3.00947363e-07,   3.00947363e-07]])
    """
    alp = 14.0
    version_id = versions[variant]
    func = func.lower()

    if variant in {'bj', 'zero'}:
        rs6, s18, rs18, s6 = parameters[variant][func]
    else:
        raise NotImplementedError('Only BJ and zero damping cases are implemented')

    atomic_numbers = np.array(atomic_numbers, dtype=int)
    atomic_positions = np.array(atomic_positions, dtype=np.float64).T

    energy, forces = dft_dispersion_correction(
            atomic_numbers,
            atomic_positions,
            s6, s18, rs6, rs18, alp, version_id)

    return energy, forces


# TODO references
def periodic_d3_correction(atomic_numbers, atomic_positions, cell_vectors, func='pbe', variant='bj'):
    """Calculate the D2/D3 dispersion correction for a given periodic set of atoms.

    Grimme et al. dispersion corrections.

    Parameters
    ----------

    atomic_numbers : array_like 
        A set of atomic numbers of shape ``(N,) ``. 

    atomic_positions : array_like
        Set of atomic positions in atomic units (bohr) 
        of shape ``(N,3)``

    cell_vectors : array_like
        Set of unit cell vectors in atomic units (bohr)
        of shape ``(3,3)``

    func : {'pbe'}, optional
        Choice of functional to use for this calculation (as given in)

    variant : {'bj', 'zero', 'd2'}, optional
        Choice of functional to use for this calculation (as given in)


    Returns
    -------
    results : dict
        The dispersion energy of the system (`edisp`) and the force on
        each atom (`grad`)
    

    Example:

    >>> n = [8, 1, 1]
    >>> xyz = [[0, 0, 0.222590804],[0, 1.42759927, -0.89036525],[0, -1.42759927, -0.89036525]]
    >>> cell = [[10,0,0], [0,10,0], [0,0,10]]
    >>> edisp, forces, stress = periodic_d3_correction(n, xyz, cell, func='b-lyp')
    >>> edisp
    -0.001003511669637431
    >>> stress
    array([[ -4.90269691e-07,   8.86062624e-24,  -2.59065249e-23],
           [  1.39428235e-23,  -7.43729438e-07,  -8.81825353e-24],
           [ -2.08238107e-23,  -1.00894981e-23,  -5.39744195e-07]])
    """

    alp = 14.0
    version_id = versions[variant]

    if variant in {'bj', 'zero'}:
        rs6, s18, rs18, s6 = parameters[variant][func]
    else:
        raise NotImplementedError('Only BJ and zero damping cases are implemented')

    atomic_numbers = np.array(atomic_numbers, dtype=int)
    atomic_positions = np.array(atomic_positions, dtype=np.float64).T
    cell_vectors = np.array(cell_vectors, dtype=np.float64).T

    energy, forces, stress = periodic_dispersion_correction(
            atomic_numbers,
            atomic_positions,
            cell_vectors,
            s6, s18, rs6, rs18, alp, version_id)

    return energy, forces, stress

