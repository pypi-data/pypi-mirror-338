from Classification.Attribute.DiscreteIndexedAttribute cimport DiscreteIndexedAttribute
from Classification.Instance.Instance cimport Instance
from DependencyParser.Universal.UniversalDependencyTreeBankFeatures cimport UniversalDependencyTreeBankFeatures
from DependencyParser.Universal.UniversalDependencyTreeBankWord cimport UniversalDependencyTreeBankWord

cdef class ArcEagerInstanceGenerator(InstanceGenerator):

    cpdef bint suitable(self, UniversalDependencyTreeBankWord word):
        """
        Checks if the given word has a valid relation.
        :param word: The UniversalDependencyTreeBankWord to check.
        :return: true if the relation is valid, false otherwise.
        """
        return word.getRelation() is not None

    cpdef Instance generate(self,
                            State state,
                            int windowSize,
                            str command):
        """
        Generates an Instance object based on the provided state, window size, and command.
        The Instance is populated with attributes derived from the words in the state.
        :param state: The state used to generate the instance.
        :param windowSize: The size of the window used to extract words from the state.
        :param command: The command associated with the instance.
        :return: The generated Instance object.
        """
        instance = Instance(command)
        attributes = []
        for i in range(windowSize):
            word = state.getStackWord(i)
            if word is None:
                attributes.append(DiscreteIndexedAttribute("null", 0, 18))
                self.addEmptyAttributes(attributes)
                attributes.append(DiscreteIndexedAttribute("null", 0, 59))
            else:
                if word.getName() == "root":
                    attributes.append(DiscreteIndexedAttribute("root", 0, 18))
                    self.addEmptyAttributes(attributes)
                    attributes.append(DiscreteIndexedAttribute("null", 0, 59))
                else:
                    attributes.append(DiscreteIndexedAttribute(word.getUpos().name, UniversalDependencyTreeBankFeatures.posIndex(word.getUpos().name) + 1, 18))
                    self.addFeatureAttributes(word, attributes)
                    if self.suitable(word):
                        attributes.append(DiscreteIndexedAttribute(word.getRelation().__str__(), UniversalDependencyTreeBankFeatures.dependencyIndex(word.getRelation().__str__()) + 1, 59))
                    else:
                        attributes.append(DiscreteIndexedAttribute("null", 0, 59))
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
