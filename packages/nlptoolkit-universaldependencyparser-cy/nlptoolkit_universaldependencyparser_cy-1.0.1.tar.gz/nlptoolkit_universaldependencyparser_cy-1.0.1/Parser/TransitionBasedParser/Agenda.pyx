import sys

cdef class Agenda:

    def __init__(self, beamSize: int):
        self.__agenda = dict()
        self.__beam_size = beamSize

    cpdef list getKeySet(self):
        """
        Retrieves the set of states currently in the agenda.
        :return: A set of states that are currently in the agenda.
        """
        return list(self.__agenda)

    cpdef updateAgenda(self,
                       ScoringOracle oracle,
                       State current):
        """
        Updates the agenda with a new state if it is better than the worst state
        currently in the agenda or if there is room in the agenda.
        :param oracle: The ScoringOracle used to score the state.
        :param current: The state to be added to the agenda.
        """
        if current in self.__agenda:
            return
        point = oracle.score(current)
        if len(self.__agenda) < self.__beam_size:
            self.__agenda[current] = point
        else:
            worst = None
            worst_value = sys.maxsize
            for key in self.__agenda:
                if self.__agenda[key] < worst_value:
                    worst_value = self.__agenda[key]
                    worst = key
            if point > worst_value:
                self.__agenda.pop(worst)
                self.__agenda[current] = point

    cpdef State best(self):
        """
        Retrieves the best state from the agenda based on the highest score.
        :return: The state with the highest score in the agenda.
        """
        best = None
        best_value = sys.maxsize
        for key in self.__agenda:
            if self.__agenda[key] > best_value:
                best_value = self.__agenda[key]
                best = key
        return best
