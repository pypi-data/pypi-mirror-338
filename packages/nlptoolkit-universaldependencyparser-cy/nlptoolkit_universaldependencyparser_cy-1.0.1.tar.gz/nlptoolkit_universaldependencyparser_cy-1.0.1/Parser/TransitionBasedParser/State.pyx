from DependencyParser.Universal.UniversalDependencyRelation cimport UniversalDependencyRelation
from DependencyParser.Universal.UniversalDependencyTreeBankWord cimport UniversalDependencyTreeBankWord

from Parser.TransitionBasedParser.Command import Command
from Parser.TransitionBasedParser.TransitionSystem import TransitionSystem

cdef class State:

    def __init__(self,
                 stack: list,
                 wordList: list,
                 relations: list):
        """
        Constructs a State object with given stack, wordList, and relations.
        :param stack: The stack of words in the parser state.
        :param wordList: The list of words to be processed.
        :param relations: The relations established between words.
        """
        self.__stack = stack
        self.__word_list = wordList
        self.__relations = relations

    cpdef applyShift(self):
        """
        Applies the SHIFT operation to the parser state.
        Moves the first word from the wordList to the stack.
        """
        if len(self.__word_list) > 0:
            self.__stack.append(self.__word_list.pop(0))

    cpdef applyLeftArc(self, object _type):
        """
        Applies the LEFTARC operation to the parser state.
        Creates a relation from the second-to-top stack element to the top stack element
        and then removes the second-to-top element from the stack.
        :param _type: The type of the dependency relation.
        """
        if len(self.__stack) > 1:
            before_last = self.__stack[len(self.__stack) - 2].getWord()
            index = self.__stack[len(self.__stack) - 1].getToWord()
            before_last.setRelation(UniversalDependencyRelation(index, _type.name.replace("_", ":")))
            self.__stack.pop(len(self.__stack) - 2)
            self.__relations.append(StackRelation(before_last, UniversalDependencyRelation(index, _type.name.replace("_", ":"))))

    cpdef applyRightArc(self, object _type):
        """
        Applies the RIGHTARC operation to the parser state.
        Creates a relation from the top stack element to the second-to-top stack element
        and then removes the top element from the stack.
        :param _type: The type of the dependency relation.
        """
        if len(self.__stack) > 1:
            last = self.__stack[len(self.__stack) - 1].getWord()
            index = self.__word_list[0].getToWord()
            last.setRelation(UniversalDependencyRelation(index, _type.name.replace("_", ":")))
            self.__stack.pop()
            self.__relations.append(StackRelation(last, UniversalDependencyRelation(index, _type.name.replace("_", ":"))))

    cpdef applyArcEagerLeftArc(self, object _type):
        """
        Applies the ARC_EAGER_LEFTARC operation to the parser state.
        Creates a relation from the last element of the stack to the first element of the wordList
        and then removes the top element from the stack.
        :param _type: The type of the dependency relation.
        """
        if len(self.__stack) > 0 and len(self.__word_list) > 0:
            last_element_of_stack = self.__stack[len(self.__stack) - 1].getWord()
            index = self.__word_list[0].getToWord()
            last_element_of_stack.setRelation(UniversalDependencyRelation(index, _type.name.replace("_", ":")))
            self.__stack.pop()
            self.__relations.append(StackRelation(last_element_of_stack, UniversalDependencyRelation(index, _type.name.replace("_", ":"))))

    cpdef applyArcEagerRightArc(self, object _type):
        """
        Applies the ARC_EAGER_RIGHTARC operation to the parser state.
        Creates a relation from the first element of the wordList to the top element of the stack
        and then performs a SHIFT operation.
        :param _type: The type of the dependency relation.
        """
        if len(self.__stack) > 0 and len(self.__word_list) > 0:
            first_element_of_word_list = self.__word_list[0].getWord()
            index = self.__stack[len(self.__stack) - 1].getToWord()
            first_element_of_word_list.setRelation(UniversalDependencyRelation(index, _type.name.replace("_", ":")))
            self.applyShift()
            self.__relations.append(StackRelation(first_element_of_word_list, UniversalDependencyRelation(index, _type.name.replace("_", ":"))))

    cpdef applyReduce(self):
        """
        Applies the REDUCE operation to the parser state.
        Removes the top element from the stack.
        """
        if len(self.__stack) > 0:
            self.__stack.pop()

    cpdef apply(self, object command, object _type, object transitionSystem):
        """
        Applies a specific command based on the transition system.
        :param command: The command to be applied (e.g., SHIFT, LEFTARC, RIGHTARC, REDUCE).
        :param _type: The type of dependency relation, relevant for ARC operations.
        :param transitionSystem: The transition system (e.g., ARC_STANDARD, ARC_EAGER) that determines which command to apply.
        """
        if transitionSystem == TransitionSystem.ARC_STANDARD:
            if command == Command.LEFTARC:
                self.applyLeafArc(_type)
            elif command == Command.RIGHTARC:
                self.applyRightArc(_type)
            elif command == Command.SHIFT:
                self.applyShift()
        elif transitionSystem == TransitionSystem.ARC_EAGER:
            if command == Command.LEFTARC:
                self.applyArcEagerLeftArc(_type)
            elif command == Command.RIGHTARC:
                self.applyArcEagerRightArc(_type)
            elif command == Command.SHIFT:
                self.applyShift()
            elif command == Command.REDUCE:
                self.applyReduce()

    cpdef int relationSize(self):
        """
        Returns the number of relations established in the current state.
        :return: The size of the relations list.
        """
        return len(self.__relations)

    cpdef int wordListSize(self):
        """
        Returns the number of words remaining in the wordList.
        :return: The size of the wordList.
        """
        return len(self.__word_list)

    cpdef int stackSize(self):
        """
        Returns the number of words currently in the stack.
        :return: The size of the stack.
        """
        return len(self.__stack)

    cpdef UniversalDependencyTreeBankWord getStackWord(self, int index):
        """
        Retrieves a specific word from the stack based on its position.
        :param index: The position of the word in the stack.
        :return: The word at the specified position, or null if the index is out of bounds.
        """
        size = len(self.__stack) - 1
        if size - index < 0:
            return None
        return self.__stack[size - index].getWord()

    cpdef UniversalDependencyTreeBankWord getPeek(self):
        """
        Retrieves the top word from the stack.
        :return: The top word of the stack, or null if the stack is empty.
        """
        if len(self.__stack) > 0:
            return self.__stack[len(self.__stack) - 1].getWord()
        return None

    cpdef UniversalDependencyTreeBankWord getWordListWord(self, int index):
        """
        Retrieves a specific word from the wordList based on its position.
        :param index: The position of the word in the wordList.
        :return: The word at the specified position, or null if the index is out of bounds.
        """
        if index > len(self.__word_list) - 1:
            return None
        return self.__word_list[index].getWord()

    cpdef StackRelation getRelation(self, int index):
        """
        Retrieves a specific relation based on its index.
        :param index: The position of the relation in the relations list.
        :return: The relation at the specified position, or null if the index is out of bounds.
        """
        if index < len(self.__relations):
            return self.__relations[index]
        return None
