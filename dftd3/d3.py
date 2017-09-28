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
parameters = {}

# s6 parameters for D2
parameters['D2'] = {
    'b3lyp': 1.05,
    'b3pw91': 1.1,
    'b97': 0.75,
    'b971': 0.65,
    'b972': 1.05,
    'b973': 0.9,
    'b97d': 1.25,
    'blyp': 1.2,
    'bmk': 0.65,
    'bp86': 1.05,
    'm06': 0.25,
    'm062x': 0.06,
    'm06l': 0.2,
    'pbe': 0.75,
    'pbe0': 0.7,
    'pw6b95': 0.5,
    'revpbe': 1.25,
    'tpss': 1,
    'tpssh': 0.9,
}

# parameters taken from http://www.thch.uni-bonn.de/tc/downloads/DFT-D3/functionalsbj.html
# Parameters are as follows: (s6, rs6, s18)
parameters['zero'] = {
    'b1b95':        (1.0, 1.613, 1.868),
    'b2gpplyp':     (0.56, 1.586, 0.760),
    'b2ply':        (0.64, 1.427, 1.022),
    'b3lyp':        (1.0, 1.261, 1.703),
    'b3pw91':       (1.0, 1.176, 1.775),
    'b97':          (1,  0.8920,  0.9090),
    'b97d':         (1.0, 0.892, 0.909),
    'bhlyp':        (1.0, 1.370, 1.442),
    'bloc':         (1,  1.1040,  0.8880),
    'blyp':         (1.0, 1.094, 1.682),
    'bmk':          (1.0, 1.931, 2.168),
    'bop':          (1.0, 0.929, 1.975),
    'bp86':         (1.0, 1.139, 1.683),
    'bpbe':         (1.0, 1.087, 2.033),
    'camb3lyp':     (1.0, 1.378, 1.217),
    'dsdblyp':      (0.50, 1.569, 0.705),
    'hcth120':      (1.0, 1.221, 1.206),
    'hf':           (1,  1.1580,  1.7460),
    'hse-hjs':      (1,  1.1290,  0.1090),
    'lc-wpbe08':    (1,  1.3550,  1.2790),
    'lcωpbe':       (1.0, 1.355, 1.279),
    'm05':          (1.0, 1.373, 0.595),
    'm052x':        (1.0, 1.417, 0.00),
    'm06':          (1.0, 1.325, 0.00),
    'm062x':        (1.0, 1.619, 0.00),
    'm06hf':        (1.0, 1.446, 0.00),
    'm06l':         (1.0, 1.581, 0.00),
    'm11l':         (1,  2.3933,  1.1129),
    'mpw1b95':      (1.0, 1.605, 1.118),
    'mpwb1k':       (1.0, 1.671, 1.061),
    'mpwlyp':       (1.0, 1.239, 1.098),
    'ms0':          (1,  1.1500,  0.0000),
    'ms1':          (1,  1.0500,  0.0000),
    'ms2':          (1,  1.1400,  0.0000),
    'ms2h':         (1,  1.1400,  0.0000),
    'n12':          (1,  1.3493,  2.3916),
    'olyp':         (1.0, 0.806, 1.764),
    'opbe':         (1.0, 0.837, 2.055),
    'otpss':        (1.0, 1.128, 1.494),
    'pbe':          (1.0, 1.217, 0.722),
    'pbe0':         (1.0, 1.287, 0.928),
    'pbe38':        (1.0, 1.333, 0.998),
    'pbesol':       (1.0, 1.345, 0.612),
    'ptpss':        (0.75, 1.541, 0.879),
    'pw6b95':       (1.0, 1.532, 0.862),
    'pwb6k':        (1.0, 1.660, 0.550),
    'pwpb95':       (0.82, 1.557, 0.705),
    'revpbe':       (1,  0.9230,  1.0100),
    'revpbe0':      (1.0, 0.949, 0.792),
    'revpbe38':     (1.0, 1.021, 0.862),
    'revssb':       (1.0, 1.221, 0.560),
    'rpbe':         (1,  0.8720,  0.5140),
    'rpw86pbe':     (1.0, 1.224, 0.901),
    'scan':         (1,  1.3240,  0.0000),
    'ssb':          (1.0, 1.215, 0.663),
    'tpss':         (1.0, 1.166, 1.105),
    'tpss0':        (1.0, 1.252, 1.242),
    'tpssh':        (1.0, 1.223, 1.219),
}

# D3(BJ) damping parameters
# Parameters are as follows: (rs6, s18, rs18, s6)
# otherwise known as         ( s6,  a1,   s8, a2)
parameters['bj'] = {
    'b1b95':        (1.000, 0.2092, 1.4507, 5.5545),
    'b2gpplyp':     (0.560, 0.0000, 0.2597, 6.3332),
    'b2plyp':       (0.640, 0.3065, 0.9147, 5.0570),
    'b3lyp':        (1.000, 0.3981, 1.9889, 4.4211),
    'b3pw91':       (1.000, 0.4312, 2.8524, 4.4693),
    'b97d':         (1.000, 0.5545, 2.2609, 3.2297),
    'bhlyp':        (1.000, 0.2793, 1.0354, 4.9615),
    'blyp':         (1.000, 0.4298, 2.6996, 4.2359),
    'bmk':          (1.000, 0.1940, 2.0860, 5.9197),
    'bop':          (1.000, 0.4870, 3.295, 3.5043),
    'bp86':         (1.000, 0.3946, 3.2822, 4.8516),
    'bpbe':         (1.000, 0.4567, 4.0728, 4.3908),
    'camb3lyp':     (1.000, 0.3708, 2.0674, 5.4743),
    'dsdblyp':      (0.500, 0.0000, 0.2130, 6.0519),
    'hcth120':      (1.000, 0.3563, 1.0821, 4.3359),
    'hf':           (1.000, 0.3385, 0.9171, 2.883),
    'hse-hjs':      (1.000, 0.3830, 2.3100, 5.685),
    'lc-wpbe08':    (1.000, 0.3919, 1.8541, 5.0897),
    'lcωpbe':       (1.000, 0.3919, 1.8541, 5.0897),
    'm11':          (1.000, 0.0000, 2.8112, 10.1389),
    'mn12l':        (1.000, 0.0000, 2.2674, 9.1494),
    'mn12sx':       (1.000, 0.0983, 1.1674, 8.0259),
    'mpw1b95':      (1.000, 0.1955, 1.0508, 6.4177),
    'mpwb1k':       (1.000, 0.1474, 0.9499, 6.6223),
    'mpwlyp':       (1.000, 0.4831, 2.0077, 4.5323),
    'n12sx':        (1.000, 0.3283, 2.4900, 5.7898),
    'olyp':         (1.000, 0.5299, 2.6205, 2.8065),
    'opbe':         (1.000, 0.5512, 3.3816, 2.9444),
    'otpss':        (1.000, 0.4634, 2.7495, 4.3153),
    'pbe':          (1.000, 0.4289, 0.7875, 4.4407),
    'pbe0':         (1.000, 0.4145, 1.2177, 4.8593),
    'pbe38':        (1.000, 0.3995, 1.4623, 5.1405),
    'pbesol':       (1.000, 0.4466, 2.9491, 6.1742),
    'ptpss':        (0.750, 0.000, 0.2804, 6.5745),
    'pw6b95':       (1.000, 0.2076, 0.7257, 6.375),
    'pwb6k':        (1.000, 0.1805, 0.9383, 7.7627),
    'pwpb95':       (0.820, 0.0000, 0.2904, 7.3141),
    'revpbe':       (1.000, 0.5238, 2.3550, 3.5016),
    'revpbe0':      (1.000, 0.4679, 1.7588, 3.7619),
    'revpbe38':     (1.000, 0.4309, 1.4760, 3.9446),
    'revssb':       (1.000, 0.4720, 0.4389, 4.0986),
    'rpbe':         (1.000, 0.1820, 0.8318, 4.0094),
    'rpw86pbe':     (1.000, 0.4613, 1.3845, 4.5062),
    'scan':         (1.000, 0.5380, 0.0000, 5.42),
    'sogga11x':     (1.000, 0.1330, 1.1426, 5.7381),
    'ssb':          (1.000, -0.0952, -0.1744, 5.2170),
    'tpss':         (1.000, 0.4535, 1.9435, 4.4752),
    'tpss0':        (1.000, 0.3768, 1.2576, 4.5865),
    'tpssh':        (1.000, 0.4529, 2.2382, 4.6550),
    'b2kplyp':      (0.64,  0.0000, 0.1521, 7.1916),
    'dsd-pbep86':   (0.418, 0.0000, 0.0000, 5.6500)
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
    >>> edisp, _ = d3_correction(n, xyz, func='blyp')
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

    if variant in {'bj'}:
        s6, rs6, s18, rs18 = parameters[variant][func]
    else:
        raise NotImplementedError('Only BJ case is currently implemented')

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
    >>> edisp, forces, stress = periodic_d3_correction(n, xyz, cell, func='blyp')
    >>> edisp
    -0.001003511669637431
    >>> stress
    array([[ -4.90269691e-07,   8.86062624e-24,  -2.59065249e-23],
           [  1.39428235e-23,  -7.43729438e-07,  -8.81825353e-24],
           [ -2.08238107e-23,  -1.00894981e-23,  -5.39744195e-07]])
    """

    alp = 14.0
    version_id = versions[variant]

    if variant in {'bj'}:
        s6, rs6, s18, rs18 = parameters[variant][func]
    else:
        raise NotImplementedError('Only BJ damping is currently implemented')

    atomic_numbers = np.array(atomic_numbers, dtype=int)
    atomic_positions = np.array(atomic_positions, dtype=np.float64).T
    cell_vectors = np.array(cell_vectors, dtype=np.float64).T

    energy, forces, stress = periodic_dispersion_correction(
            atomic_numbers,
            atomic_positions,
            cell_vectors,
            s6, s18, rs6, rs18, alp, version_id)

    return energy, forces, stress

