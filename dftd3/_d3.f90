! Copyright (C) 2017, Peter Spackman
! 
! This program is free software; you can redistribute it and/or modify
! it under the terms of the GNU General Public License as published by
! the Free Software Foundation; either version 3, or (at your option)
! any later version.
!
! This program is distributed in the hope that it will be useful,
! but WITHOUT ANY WARRANTY; without even the implied warranty of
! MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
! GNU General Public License for more details.
!
! For the GNU General Public License, see <http://www.gnu.org/licenses/>

module d3

    use dftd3_api
    implicit none

    private
    public d3_calc, periodic_d3_calc

contains

    subroutine d3_calc(n_atoms, atomic_numbers, coords, s6, s18, rs6, rs18, alp, version, edisp, grads)
        !f2py threadsafe
      integer, intent(in) :: n_atoms, atomic_numbers(n_atoms), version
      double precision, intent(in) :: s6, s18, rs6, rs18, alp, coords(3, n_atoms)
      double precision, intent(out) :: edisp, grads(3, n_atoms)

      type(dftd3_input) :: input
      type(dftd3_calc) :: dftd3

      ! the following setup may be subject to some minor change

      ! Threebody interactions
      input%threebody = .true.

      ! Numerical gradients
      input%numgrad = .false.

      ! Cutoffs
      input%cutoff = sqrt(9000.0d0)
      input%cutoff_cn = sqrt(1600.0d0)

      call dftd3_init(dftd3, input)
      call dftd3_set_params(dftd3, [s6, rs6, s18, rs18, alp], version)
      call dftd3_dispersion(dftd3, coords, atomic_numbers, edisp, grads)

    end subroutine

    subroutine periodic_d3_calc(n_atoms, atomic_numbers, coords, cell, s6, s18, rs6, rs18, alp, version, edisp, grads, stress)
        !f2py threadsafe
      integer, intent(in) :: n_atoms, atomic_numbers(n_atoms), version
      double precision, intent(in) :: s6, s18, rs6, rs18, alp, coords(3, n_atoms), cell(3,3)
      double precision, intent(out) :: edisp, grads(3, n_atoms), stress(3,3)

      type(dftd3_input) :: input
      type(dftd3_calc) :: dftd3

      ! the following setup may be subject to some minor change

      ! Threebody interactions
      input%threebody = .true.

      ! Numerical gradients
      input%numgrad = .false.

      ! Cutoffs
      input%cutoff = sqrt(9000.0d0)
      input%cutoff_cn = sqrt(1600.0d0)

      call dftd3_init(dftd3, input)
      call dftd3_set_params(dftd3, [s6, rs6, s18, rs18, alp], version)
      call dftd3_pbc_dispersion(dftd3, coords, atomic_numbers, &
                                cell, edisp, grads, stress)
    end subroutine



end module d3
