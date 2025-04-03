from abc import abstractmethod
from typing import List

from Classification.Model.Model cimport Model
from DependencyParser.Universal.UniversalDependencyRelation cimport UniversalDependencyRelation
from DependencyParser.Universal.UniversalDependencyType import UniversalDependencyType

from Parser.TransitionBasedParser.Command import Command
from Parser.TransitionBasedParser.Decision cimport Decision
from Parser.TransitionBasedParser.TransitionSystem import TransitionSystem

cdef class Oracle:

    def __init__(self,
                 model: Model,
                 window_size: int):
        """
        Constructs an Oracle with the given model and window size.
        :param model: the model used for making predictions
        :param window_size: the size of the window used in parsing
        """
        self.command_model = model
        self.window_size = window_size

    @abstractmethod
    def makeDecision(self, state: State) -> Decision:
        """
        Abstract method to be implemented by subclasses to make a parsing decision based on the current state.
        :param state: the current parsing state
        :return: a {@link Decision} object representing the action to be taken
        """
        pass

    @abstractmethod
    def scoreDecisions(self,
                       state: State,
                       transitionSystem: TransitionSystem) -> List[Decision]:
        """
        Abstract method to be implemented by subclasses to score potential decisions based on the current state and transition system.
        :param state: the current parsing state
        :param transitionSystem: the transition system being used (e.g., ARC_STANDARD or ARC_EAGER)
        :return: a list of {@link Decision} objects, each with a score indicating its suitability
        """
        pass

    cpdef str findBestValidEagerClassInfo(self,
                                          dict probabilities,
                                          State state):
        """
        Finds the best valid parsing action for the ARC_EAGER transition system based on probabilities.
        Ensures the action is applicable given the current state.
        :param probabilities: a map of actions to their associated probabilities
        :param state: the current parsing state
        :return: the best action as a string, or an empty string if no valid action is found
        """
        best_value = 0.0
        best = ""
        for key in probabilities:
            if probabilities[key] > best_value:
                if key == "SHIFT" or key == "RIGHTARC":
                    if state.wordListSize() > 0:
                        best = key
                        best_value = probabilities[key]
                    elif state.stackSize() > 1:
                        if not (key == "REDUCE" and state.getPeek().getRelation() is None):
                            best = key
                            best_value = probabilities[key]
        return best

    cpdef str findBestValidStandardClassInfo(self,
                                             dict probabilities,
                                             State state):
        """
        Finds the best valid parsing action for the ARC_STANDARD transition system based on probabilities.
        Ensures the action is applicable given the current state.
        :param probabilities: a map of actions to their associated probabilities
        :param state: the current parsing state
        :return: the best action as a string, or an empty string if no valid action is found
        """
        best_value = 0.0
        best = ""
        for key in probabilities:
            if probabilities[key] > best_value:
                if key == "SHIFT":
                    if state.wordListSize() > 0:
                        best = key
                        best_value = probabilities[key]
                    elif state.stackSize() > 1:
                        best = key
                        best_value = probabilities[key]
        return best

    cpdef Candidate getDecisionCandidate(self, str best):
        """
        Converts a string representation of the best action into a {@link Candidate} object.
        :param best: the best action represented as a string, possibly with a dependency type in parentheses
        :return: a {@link Candidate} object representing the action, or null if the action is unknown
        """
        if "(" in best:
            command = best[0:best.index('(')]
            relation = best[best.index('(') + 1:best.index(')')]
            _type = UniversalDependencyRelation.getDependencyTag(relation)
        else:
            command = best
            _type = UniversalDependencyType.DEP
        if command == "SHIFT":
            return Candidate(Command.SHIFT, _type)
        elif command == "REDUCE":
            return Candidate(Command.REDUCE, _type)
        elif command == "LEFTARC":
            return Candidate(Command.LEFTARC, _type)
        elif command == "RIGHTARC":
            return Candidate(Command.RIGHTARC, _type)
        return None
