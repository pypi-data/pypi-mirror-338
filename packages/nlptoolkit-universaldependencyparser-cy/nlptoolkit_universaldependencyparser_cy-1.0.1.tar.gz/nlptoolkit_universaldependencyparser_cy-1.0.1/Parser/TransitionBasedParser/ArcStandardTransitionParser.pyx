from DependencyParser.Universal.UniversalDependencyTreeBankSentence cimport UniversalDependencyTreeBankSentence
from DependencyParser.Universal.UniversalDependencyTreeBankWord cimport UniversalDependencyTreeBankWord

from Parser.TransitionBasedParser.Command import Command
from Parser.TransitionBasedParser.SimpleInstanceGenerator cimport SimpleInstanceGenerator
from Parser.TransitionBasedParser.StackWord cimport StackWord
from Parser.TransitionBasedParser.State cimport State

cdef class ArcStandardTransitionParser(TransitionParser):

    def __init__(self):
        super().__init__()

    cpdef bint checkForMoreRelation(self,
                                    list wordList,
                                    int _id):
        """
        Checks if there are more relations with a specified ID in the list of words.
        :param wordList: The list of words to check.
        :param _id: The ID to check for.
        :return: True if no more relations with the specified ID are found; false otherwise.
        """
        for word in wordList:
            if word.getWord().getRelation().to() == _id:
                return False
        return True

    cpdef list simulateParse(self,
                             UniversalDependencyTreeBankSentence sentence,
                             int windowSize):
        """
        Simulates the parsing process for a given sentence using the Arc Standard parsing algorithm.
        :param sentence: The sentence to be parsed.
        :param windowSize: The size of the window used for feature generation.
        :return: An ArrayList of {@link Instance} objects representing the parsed actions.
        """
        instance_generator = SimpleInstanceGenerator()
        instance_list = []
        word_list = []
        stack = []
        for j in range(sentence.wordCount()):
            word = sentence.getWord(j)
            if isinstance(word, UniversalDependencyTreeBankWord):
                word_list.append(StackWord(word, j + 1))
        stack.append(StackWord())
        state = State(stack, word_list, [])
        if len(word_list) > 0:
            instance_list.append(instance_generator.generate(state, windowSize, "SHIFT"))
            stack.append(word_list.pop(0))
            if len(word_list) > 1:
                instance_list.append(instance_generator.generate(state, windowSize, "SHIFT"))
                stack.append(word_list.pop(0))
            while len(word_list) > 0 or len(stack) > 1:
                top = stack[len(stack) - 1].getWord()
                top_relation = top.getRelation()
                if len(stack) > 1:
                    before_top = stack[len(stack) - 2].getWord()
                    before_top_relation = before_top.getRelation()
                    if before_top.getId() == top_relation.to() and self.checkForMoreRelation(word_list, top.getId()):
                        instance_list.append(instance_generator.generate(state, windowSize, "RIGHTARC(" + top_relation.__str__() + ")"))
                        stack.pop()
                    elif top.getId() == before_top_relation.to():
                        instance_list.append(instance_generator.generate(state, windowSize, "LEFTARC(" + before_top_relation.__str__() + ")"))
                        stack.pop(len(stack) - 2)
                    else:
                        if len(word_list) > 0:
                            instance_list.append(instance_generator.generate(state, windowSize, "SHIFT"))
                            stack.append(word_list.pop(0))
                        else:
                            break
                else:
                    if len(word_list) > 0:
                        instance_list.append(instance_generator.generate(state, windowSize, "SHIFT"))
                        stack.append(word_list.pop(0))
                    else:
                        break
        return instance_list

    cpdef UniversalDependencyTreeBankSentence dependencyParse(self,
                                                              UniversalDependencyTreeBankSentence universalDependencyTreeBankSentence,
                                                              Oracle oracle):
        """
        Performs dependency parsing on the given sentence using the provided oracle.
        :param universalDependencyTreeBankSentence: The sentence to be parsed.
        :param oracle: The oracle used to make parsing decisions.
        :return: The parsed sentence with dependency relations established.
        """
        sentence = self.createResultSentence(universalDependencyTreeBankSentence)
        state = self.initialState(sentence)
        while state.wordListSize() > 0 or state.stackSize() > 1:
            decision = oracle.makeDecision(state)
            if decision.getCommand() == Command.SHIFT:
                state.applyShift()
            elif decision.getCommand() == Command.LEFTARC:
                state.applyLeftArc(decision.getUniversalDependencyType())
            elif decision.getCommand() == Command.RIGHTARC:
                state.applyRightArc(decision.getUniversalDependencyType())
        return sentence
