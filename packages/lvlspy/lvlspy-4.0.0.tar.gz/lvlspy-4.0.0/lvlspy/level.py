"""Module to handle levels in species."""

import numpy as np
from gslconsts.consts import (
    GSL_CONST_CGSM_ELECTRON_VOLT,
    GSL_CONST_CGSM_BOLTZMANN,
)
import lvlspy.properties as lp

units_dict = {"eV": 1000, "keV": 1, "MeV": 1.0e-3, "GeV": 1.0e-6}


class Level(lp.Properties):
    """A class for storing and retrieving data about a level.

    Args:
        ``energy`` (:obj:`float`): The energy of the level.  It is in units
        given by the keyword `units`.

        ``multiplicity`` (:obj:`int`): The multiplicity of the level.

        ``units`` (:obj:`str`, optional):  A string giving the
        units for the energy.  Possible values are 'eV',
        'keV' (the default), 'MeV', or 'GeV'.

    """

    def __init__(self, energy, multiplicity, units="keV"):
        super().__init__()
        self.energy = energy / units_dict[units]
        self.multiplicity = multiplicity
        self.properties = {}
        self.units = "keV"

    def __eq__(self, other):
        if not isinstance(other, Level):
            return NotImplemented

        return (
            self.energy == other.energy
            and self.multiplicity == other.multiplicity
        )

    def get_energy(self, units="keV"):
        """Method to retrieve the energy for a level.

        Args:
            ``units`` (:obj:`str`, optional):  A string giving the
            units for the energy.

        Returns:
            :obj:`float`: The energy in units given by the `units` keyword.
            The default is 'keV'.

        """

        return units_dict[units] * self.energy

    def get_multiplicity(self):
        """Method to retrieve the multiplicity for a level.

        Returns:
            :obj:`int`: The multiplicity.

        """

        return self.multiplicity

    def update_energy(self, energy, units="keV"):
        """Method to update the energy for a level.

        Args:
            ``energy`` (:obj:`float`):  The new energy for the level.

            ``units`` (:obj:`str`, optional):  A string giving the
            units for the energy.

        Returns:
            On successful return, the energy has been updated.

        """

        self.energy = units_dict[units] * energy

    def update_multiplicity(self, multiplicity):
        """Method to update the multiplicity for a level.

        Args:
            ``multiplicity`` (:obj:`int`):  The new multiplicity for the level.

        Returns:
            On successful return, the multiplicity has been updated.

        """

        self.multiplicity = multiplicity

    def compute_boltzmann_factor(self, temperature):
        """Method to compute the Boltzmann factor for a level.

        Args:
            ``temperature`` (:obj:`float`):  The temperature in K at which to
            compute the factor.

        Returns:
            :obj:`float`: The computed Boltzmann factor
            multiplicity * exp(-Energy/kT).

        """
        # the factor of 1e+3 is to convert the energy to keV.
        k_bt = GSL_CONST_CGSM_BOLTZMANN * temperature

        energy = 1.0e3 * GSL_CONST_CGSM_ELECTRON_VOLT * self.energy

        if k_bt == 0:
            if energy == 0:
                return 1
            return 0

        return self.multiplicity * np.exp(-energy / k_bt)
