"""Module to handle species."""

import numpy as np
import lvlspy.properties as lp
import lvlspy.calculate as calc
import lvlspy.transition as lt


class Species(lp.Properties):
    """A class for storing and retrieving data about a species.

    Args:
        ``name`` (:obj:`str`): The name of the species.

        ``levels`` (:obj:`list`, optional): A list of individual
        :obj:`lvlspy.level.Level` objects.

        ``transitions`` (:obj:`list`, optional): A list of individual
        :obj:`lvlspy.transition.Transition` objects.

        ``units`` (:obj:`str`, optional):  A string giving the
        units for the energy.

    """

    def __init__(self, name, levels=None, transitions=None):
        super().__init__()
        self.name = name
        self.levels = []
        self.transitions = []
        self.properties = {}
        if levels:
            for level in levels:
                self.levels.append(level)
        if transitions:
            for transition in transitions:
                self.add_transition(transition)

    def get_name(self):
        """Retrieve the name of the species.

        Return:
            The :obj:`str` giving the species name.

        """

        return self.name

    def update_name(self, name):
        """Change the name of the species.

        Args:
            ``name`` (:obj:`string`) The new name of the species

        Return:
            On successful return, the species' name has been updated
        """

        self.name = name

    def add_level(self, level):
        """Method to add a level to a species.

        Args:
            ``level`` (:obj:`lvlspy.level.Level`) The level to be added.

        Return:
            On successful return, the level has been added.  If the level
            previously existed in the species, it has been replaced with
            the new level.

        """

        if level in self.get_levels():
            self.remove_level(level)

        self.levels.append(level)

    def remove_level(self, level):
        """Method to remove a level from a species.

        Args:
            ``level`` (:obj:`lvlspy.level.Level`) The level to be removed.

        Return:
            On successful return, the level and all connected transitions have been removed.

        """
        for _l in self.get_upper_linked_levels(level):
            _t = self.get_level_to_level_transition(_l, level)
            if _t:
                self.remove_transition(_t)

        for _l in self.get_lower_linked_levels(level):
            _t = self.get_level_to_level_transition(level, _l)
            if _t:
                self.remove_transition(_t)

        self.levels.remove(level)

    def add_transition(self, transition):
        """Method to add a transition to a species.

        Args:
            ``transition`` (:obj:`lvlspy.transition.Transition`) The transition
            to be added.

        Return:
            On successful return, the transition has been added.  If the
            transition previously existed in the species, it has been
            replaced with the new transition.

        """

        if transition in self.get_transitions():
            self.remove_transition(transition)

        self.transitions.append(transition)

    def remove_transition(self, transition):
        """Method to remove a transition from a species.

        Args:
            ``transition`` (:obj:`lvlspy.transition.Transition`) The transition
            to be removed.

        Return:
            On successful return, the transition has been removed.

        """

        self.transitions.remove(transition)

    def get_lower_linked_levels(self, level):
        """Method to retrieve the lower-energy levels linked to the input level
        by transitions in the species.

        Args:
            ``level`` (:obj:`lvlspy.level.Level`) The level for which
            the linked levels are sought.

        Return:
            :obj:`list`: A list of the lower-energy levels linked to the
            input level by transitions.

        """

        result = []
        for transition in self.get_transitions():
            if transition.get_upper_level() == level:
                result.append(transition.get_lower_level())

        return result

    def get_upper_linked_levels(self, level):
        """Method to retrieve the higher-energy levels linked to the input level
        by transitions in the species.

        Args:
            ``level`` (:obj:`lvlspy.level.Level`) The level for which
            the linked levels are sought.

        Return:
            :obj:`list`: A list of the higher-energy levels linked to the
            input level by transitions.

        """

        result = []
        for transition in self.get_transitions():
            if transition.get_lower_level() == level:
                result.append(transition.get_upper_level())

        return result

    def get_level_to_level_transition(self, upper_level, lower_level):
        """Method to retrieve the downward transition from a particular
        upper level to a particular lower level.

        Args:
            ``upper_level`` (:obj:`lvlspy.level.Level`) The level from which
            the transition originates.

            ``lowerlevel`` (:obj:`lvlspy.level.Level`) The level to which
            the transition goes.

        Return:
            :obj:`lvlspy.transition.Transition`: The transition, or None
            if the transition is not found.

        """

        for transition in self.get_transitions():
            if (
                transition.get_upper_level() == upper_level
                and transition.get_lower_level() == lower_level
            ):
                return transition

        return None

    def get_levels(self):
        """Method to retrieve the levels for a species.

        Returns:
            :obj:`list`: A list of the levels.  The levels are sorted in
            ascending energy.

        """

        return sorted(self.levels, key=lambda x: x.energy)

    def get_transitions(self):
        """Method to retrieve the transitions for a species.

        Returns:
            :obj:`list`: A list of the transitions.

        """

        return self.transitions

    def compute_equilibrium_probabilities(self, temperature):
        """Method to compute the equilibrium probabilities for levels in a
        species.

        Args:
            ``temperature`` (:obj:`float`): The temperature in K at which to
            compute the equilibrium probabilities.

            Returns:
                :obj:`numpy.array`: A numpy array of the probabilities of the
                levels.  The levels are sorted in ascending energy.

        """

        levs = self.get_levels()

        prob = np.empty(len(levs))

        for i, lev in enumerate(levs):
            prob[i] = lev.compute_boltzmann_factor(temperature)

        prob /= np.sum(prob)

        return prob

    def compute_rate_matrix(self, temperature):
        """Method to compute the rate matrix for a species.

        Args:
            ``temperature`` (:obj:`float`): The temperature in K at which to
            compute the rate matrix.

            Returns:
                :obj:`numpy.array`: A 2d numpy array giving the rate matrix.

        """

        levels = self.get_levels()

        rate_matrix = np.zeros((len(levels), len(levels)))

        transitions = self.get_transitions()

        for transition in transitions:
            i_upper = levels.index(transition.get_upper_level())
            i_lower = levels.index(transition.get_lower_level())
            if (
                "useable" in levels[i_upper].get_properties()
                and levels[i_upper].get_properties()["useable"] is False
            ) or (
                "useable" in levels[i_lower].get_properties()
                and levels[i_lower].get_properties()["useable"] is False
            ):
                continue

            r_upper_to_lower = transition.compute_upper_to_lower_rate(
                temperature
            )
            r_lower_to_upper = transition.compute_lower_to_upper_rate(
                temperature
            )

            rate_matrix[i_lower, i_upper] += r_upper_to_lower
            rate_matrix[i_upper, i_upper] -= r_upper_to_lower

            rate_matrix[i_upper, i_lower] += r_lower_to_upper
            rate_matrix[i_lower, i_lower] -= r_lower_to_upper

        return rate_matrix

    def fill_missing_transitions(self, a):
        """Method to fill in transitions between levels using a Weisskopf estimate.
        Parity must be set as a property, otherwise method would return wrong estimates

        Args:
            `a` (:obj:`int`) Mass number of the species
        Returns:
            Upon successful return, the species will have an updated list of transitions
            based on Weisskopf estimate
        """

        levels = self.get_levels()
        for i in range(1, len(levels)):
            for j in range(i):
                t_dummy = self.get_level_to_level_transition(
                    levels[i], levels[j]
                )
                if t_dummy is None:

                    e = [levels[i].get_energy(), levels[j].get_energy()]
                    jj1 = [
                        (levels[i].get_multiplicity() - 1) // 2,
                        (levels[j].get_multiplicity() - 1) // 2,
                    ]
                    p1 = [
                        levels[i].get_properties()["parity"],
                        levels[j].get_properties()["parity"],
                    ]

                    p1 = lp.Properties().set_parity(p1)

                    ein_a = calc.Weisskopf().estimate(e, jj1, p1, a)

                    self.add_transition(
                        lt.Transition(levels[i], levels[j], ein_a)
                    )
