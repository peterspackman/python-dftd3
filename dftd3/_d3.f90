module d3

    use dftd3_api

    implicit none

    private
    public d3_calc

contains

    subroutine d3_calc(n_atoms, atomic_numbers, coords, func, bj, edisp, grads)
        !f2py threadsafe
      integer, intent(in) :: n_atoms, atomic_numbers(n_atoms)
      character(len=*) :: func
      double precision, intent(in) :: coords(3, n_atoms)
      logical, intent(in) :: bj
      double precision, intent(out) :: edisp, grads(3, n_atoms)

      type(dftd3_input) :: input
      type(dftd3_calc) :: dftd3

      !! Threebody interactions (default: .false.)
      input%threebody = .true.

      !! Numerical gradients (default: .false.)
      input%numgrad = .false.

      !! Cutoffs (below you find the defaults)
      input%cutoff = sqrt(9000.0d0)
      input%cutoff_cn = sqrt(1600.0d0)

      call dftd3_init(dftd3, input)
      ! Choose functional. Alternatively you could set the parameters manually
      ! by the dftd3_set_params() function.
      call dftd3_set_functional(dftd3, func=func, version=4, tz=.false.)

      ! Calculate dispersion and gradients for non-periodic case
      call dftd3_dispersion(dftd3, coords, atomic_numbers, edisp, grads)

    end subroutine


end module d3
