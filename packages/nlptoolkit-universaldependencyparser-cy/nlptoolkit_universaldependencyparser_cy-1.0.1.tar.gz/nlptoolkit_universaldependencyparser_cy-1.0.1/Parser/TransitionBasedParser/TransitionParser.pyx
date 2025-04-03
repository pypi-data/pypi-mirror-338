import copy
from abc import abstractmethod
from typing import List

from Classification.DataSet.DataSet cimport DataSet
from Classification.Instance.Instance cimport Instance
from DependencyParser.Universal.UniversalDependencyRelation cimport UniversalDependencyRelation
from DependencyParser.Universal.UniversalDependencyRelation import UniversalDependencyType
from DependencyParser.Universal.UniversalDependencyTreeBankCorpus cimport UniversalDependencyTreeBankCorpus
from DependencyParser.Universal.UniversalDependencyTreeBankSentence cimport UniversalDependencyTreeBankSentence
from DependencyParser.Universal.UniversalDependencyTreeBankWord cimport UniversalDependencyTreeBankWord

from Parser.TransitionBasedParser.Candidate cimport Candidate
from Parser.TransitionBasedParser.Command import Command
from Parser.TransitionBasedParser.StackWord cimport StackWord
from Parser.TransitionBasedParser.TransitionSystem import TransitionSystem

cdef class TransitionParser:

    def __init__(self):
        pass

    cpdef UniversalDependencyTreeBankSentence createResultSentence(self,
                                                                   UniversalDependencyTreeBankSentence universalDependencyTreeBankSentence):
        """
        Creates a new {@link UniversalDependencyTreeBankSentence} with the same words as the input sentence,
        but with null heads, effectively cloning the sentence structure without dependencies.
        :param universalDependencyTreeBankSentence: the sentence to be cloned
        :return: a new {@link UniversalDependencyTreeBankSentence} with copied words but no dependencies
        """
        sentence = UniversalDependencyTreeBankSentence("u")
        for i in range(universalDependencyTreeBankSentence.wordCount()):
            word = universalDependencyTreeBankSentence.getWord(i)
            if isinstance(word, UniversalDependencyTreeBankWord):
                sentence.addWord(UniversalDependencyTreeBankWord(word.getId(),
                                                                 word.getName(),
                                                                 word.getLemma(),
                                                                 word.getUpos(),
                                                                 word.getXPos(),
                                                                 word.getFeatures(),
                                                                 None,
                                                                 word.getDeps(),
                                                                 word.getMisc()))
        return sentence

    @abstractmethod
    def simulateParse(self,
                      sentence: UniversalDependencyTreeBankSentence,
                      windowSize: int) -> List[Instance]:
        pass

    @abstractmethod
    def dependencyParse(self,
                        universalDependencyTreeBankSentence: UniversalDependencyTreeBankSentence,
                        oracle: Oracle) -> UniversalDependencyTreeBankSentence:
        pass

    cpdef simulateParseOnCorpus(self,
                                UniversalDependencyTreeBankCorpus corpus,
                                int windowSize):
        """
        Simulates parsing a corpus of sentences, returning a dataset of instances created by parsing each sentence.
        :param corpus: the corpus to be parsed
        :param windowSize: the size of the window used in parsing
        :return: a {@link DataSet} containing instances from parsing each sentence in the corpus
        """
        dataSet = DataSet()
        for i in range(corpus.sentenceCount()):
            sentence = corpus.getSentence(i)
            if isinstance(sentence, UniversalDependencyTreeBankSentence):
                dataSet.addInstanceList(self.simulateParse(sentence, windowSize))

    cpdef bint checkStates(self, Agenda agenda):
        """
        Checks if there are any states in the agenda that still have words to process or have more than one item in the stack.
        :param agenda: the agenda containing the states
        :return: true if there are states to process, false otherwise
        """
        for state in agenda.getKeySet():
            if state.wordListSize() > 0 or state.stackSize() > 1:
                return True
        return False

    cpdef State initialState(self, UniversalDependencyTreeBankSentence sentence):
        """
        Initializes the parsing state with a stack containing one empty {@link StackWord} and a word list containing all words in the sentence.
        :param sentence: the sentence to initialize the state with
        :return: a {@link State} representing the starting point for parsing
        """
        wordList = []
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            if isinstance(word, UniversalDependencyTreeBankWord):
                wordList.append(StackWord(word, i + 1))
        stack = [StackWord()]
        return State(stack, wordList, [])

    cpdef list constructCandidates(self,
                                   object transitionSystem,
                                   State state):
        """
        Constructs possible parsing candidates based on the current state and transition system.
        :param transitionSystem: the transition system used (ARC_STANDARD or ARC_EAGER)
        :param state: the current parsing state
        :return: a list of possible {@link Candidate} actions to be applied
        """
        if state.stackSize() == 1 and state.wordListSize() == 0:
            return []
        subsets = []
        if state.wordListSize() > 0:
            subsets.append(Candidate(Command.SHIFT, UniversalDependencyType.DEP))
        if transitionSystem == TransitionSystem.ARC_EAGER and state.stackSize() > 0:
            subsets.append(Candidate(Command.REDUCE, UniversalDependencyType.DEP))
        for i in range(len(UniversalDependencyRelation.universal_dependency_types)):
            _type = UniversalDependencyRelation.getDependencyTag(UniversalDependencyRelation.universal_dependency_types[i])
            if transitionSystem == TransitionSystem.ARC_STANDARD and state.stackSize() > 1:
                subsets.append(Candidate(Command.LEFTARC, _type))
                subsets.append(Candidate(Command.RIGHTARC, _type))
            elif transitionSystem == TransitionSystem.ARC_EAGER and state.stackSize() > 0 and state.wordListSize() > 0:
                subsets.append(Candidate(Command.LEFTARC, _type))
                subsets.append(Candidate(Command.RIGHTARC, _type))
        return subsets

    cpdef State dependencyParseWithBeamSearch(self,
                                              ScoringOracle oracle,
                                              int beamSize,
                                              UniversalDependencyTreeBankSentence universalDependencyTreeBankSentence,
                                              object transitionSystem):
        """
        Performs dependency parsing with beam search to find the best parse for a given sentence.
        :param oracle: the scoring oracle used for guiding the search
        :param beamSize: the size of the beam for beam search
        :param universalDependencyTreeBankSentence: the sentence to be parsed
        :param transitionSystem: the transition system used (ARC_STANDARD or ARC_EAGER)
        :return: the best parsing state from the beam search
        """
        sentence = self.createResultSentence(universalDependencyTreeBankSentence)
        initialState = self.initialState(sentence)
        agenda = Agenda(beamSize)
        agenda.updateAgenda(oracle, copy.deepcopy(initialState))
        while self.checkStates(agenda):
            for state in agenda.getKeySet():
                subsets = self.constructCandidates(transitionSystem, state)
                for subset in subsets:
                    command = subset.getCommand()
                    _type = subset.getUniversalDependencyType()
                    cloneState = copy.deepcopy(state)
                    cloneState.apply(command, _type, transitionSystem)
                    agenda.updateAgenda(oracle, copy.deepcopy(cloneState))
        return agenda.best()

    cpdef UniversalDependencyTreeBankCorpus dependencyParseCorpus(self,
                                                                  UniversalDependencyTreeBankCorpus universalDependencyTreeBankCorpus,
                                                                  Oracle oracle):
        """
        Parses a corpus of sentences using the given oracle and returns a new corpus with the parsed sentences.
        :param universalDependencyTreeBankCorpus: the corpus to be parsed
        :param oracle: the oracle used for guiding the parsing process
        :return: a {@link UniversalDependencyTreeBankCorpus} containing the parsed sentences
        """
        corpus = UniversalDependencyTreeBankCorpus()
        for i in range(universalDependencyTreeBankCorpus.sentenceCount()):
            sentence = universalDependencyTreeBankCorpus.getSentence(i)
            if isinstance(sentence, UniversalDependencyTreeBankSentence):
                corpus.addSentence(self.dependencyParse(sentence, oracle))
        return corpus
