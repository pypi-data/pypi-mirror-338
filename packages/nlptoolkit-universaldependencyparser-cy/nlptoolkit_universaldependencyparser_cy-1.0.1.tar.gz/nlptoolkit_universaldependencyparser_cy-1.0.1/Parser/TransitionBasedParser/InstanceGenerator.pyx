from abc import abstractmethod

from Classification.Attribute.DiscreteIndexedAttribute cimport DiscreteIndexedAttribute
from Classification.Instance.Instance cimport Instance
from DependencyParser.Universal.UniversalDependencyTreeBankFeatures cimport UniversalDependencyTreeBankFeatures
from DependencyParser.Universal.UniversalDependencyTreeBankWord cimport UniversalDependencyTreeBankWord

from Parser.TransitionBasedParser.State cimport State

cdef class InstanceGenerator:

    @abstractmethod
    def generate(self,
                 state: State,
                 windowSize: int,
                 command: str) -> Instance:
        """
        Abstract method for generating an instance based on the current state, window size, and command.
        :param state: The current state of the parser.
        :param windowSize: The size of the window used for feature extraction.
        :param command: The command to be used for generating the instance.
        :return: The generated {@link Instance} object.
        """
        pass

    cpdef addAttributeForFeatureType(self,
                                     UniversalDependencyTreeBankWord word,
                                     list attributes,
                                     str featureType):
        """
        Adds an attribute for a specific feature type of a given word to the list of attributes.
        :param word: The word whose feature value is used to create the attribute.
        :param attributes: The list of attributes to which the new attribute will be added.
        :param featureType: The type of the feature to be extracted from the word.
        """
        feature = word.getFeatureValue(featureType)
        number_of_values = UniversalDependencyTreeBankFeatures.numberOfValues("tr", featureType) + 1
        if feature is not None:
            attributes.append(DiscreteIndexedAttribute(feature,
                                                       UniversalDependencyTreeBankFeatures.featureValueIndex("tr", featureType, feature) + 1,
                                                       number_of_values))
        else:
            attributes.append(DiscreteIndexedAttribute("null", 0, number_of_values))

    cpdef addEmptyAttributes(self, list attributes):
        """
        Adds a set of default (empty) attributes to the list of attributes. These attributes represent
        various feature types with default "null" values.
        :param attributes: The list of attributes to which the default attributes will be added.
        """
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "PronType") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "NumType") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Number") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Case") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Definite") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Degree") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "VerbForm") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Mood") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Tense") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Aspect") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Voice") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Evident") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Polarity") + 1))
        attributes.append(DiscreteIndexedAttribute("null", 0, UniversalDependencyTreeBankFeatures.numberOfValues("tr", "Person") + 1))

    cpdef addFeatureAttributes(self,
                               UniversalDependencyTreeBankWord word,
                               list attributes):
        """
        Adds attributes for various feature types of a given word to the list of attributes.
        :param word: The word whose feature values are used to create the attributes.
        :param attributes: The list of attributes to which the new attributes will be added.
        """
        self.addAttributeForFeatureType(word, attributes, "PronType")
        self.addAttributeForFeatureType(word, attributes, "NumType")
        self.addAttributeForFeatureType(word, attributes, "Number")
        self.addAttributeForFeatureType(word, attributes, "Case")
        self.addAttributeForFeatureType(word, attributes, "Definite")
        self.addAttributeForFeatureType(word, attributes, "Degree")
        self.addAttributeForFeatureType(word, attributes, "VerbForm")
        self.addAttributeForFeatureType(word, attributes, "Mood")
        self.addAttributeForFeatureType(word, attributes, "Tense")
        self.addAttributeForFeatureType(word, attributes, "Aspect")
        self.addAttributeForFeatureType(word, attributes, "Voice")
        self.addAttributeForFeatureType(word, attributes, "Evident")
        self.addAttributeForFeatureType(word, attributes, "Polarity")
        self.addAttributeForFeatureType(word, attributes, "Person")
