from Classification.Attribute.DiscreteIndexedAttribute cimport DiscreteIndexedAttribute
from Classification.Instance.Instance cimport Instance
from DependencyParser.Universal.UniversalDependencyTreeBankFeatures cimport UniversalDependencyTreeBankFeatures

cdef class SimpleInstanceGenerator(InstanceGenerator):

    def __init__(self):
        super().__init__()

    cpdef Instance generate(self,
                            State state,
                            int windowSize,
                            str command):
        """
        Generates an instance based on the state, window size, and command.
        :param state: The current state of the parser, which includes the stack and word list.
        :param windowSize: The size of the window used for feature extraction.
        :param command: The command to be associated with the generated instance.
        :return: The generated {@link Instance} object with attributes based on the state and command.
        """
        instance = Instance(command)
        attributes = []
        for i in range(windowSize):
            word = state.getStackWord(i)
            if word is None:
                attributes.append(DiscreteIndexedAttribute("null", 0, 18))
                self.addEmptyAttributes(attributes)
            else:
                if word.getName() == "root":
                    attributes.append(DiscreteIndexedAttribute("root", 0, 18))
                    self.addEmptyAttributes(attributes)
                else:
                    attributes.append(DiscreteIndexedAttribute(word.getUpos().name, UniversalDependencyTreeBankFeatures.posIndex(word.getUpos().name) + 1, 18))
                    self.addFeatureAttributes(word, attributes)
        for i in range(windowSize):
            word = state.getWordListWord(i)
            if word is not None:
                attributes.append(DiscreteIndexedAttribute(word.getUpos().name, UniversalDependencyTreeBankFeatures.posIndex(word.getUpos().name) + 1, 18))
                self.addFeatureAttributes(word, attributes)
            else:
                attributes.append(DiscreteIndexedAttribute("root", 0, 18))
                self.addEmptyAttributes(attributes)
        for attribute in attributes:
            instance.addAttribute(attribute)
        return instance

