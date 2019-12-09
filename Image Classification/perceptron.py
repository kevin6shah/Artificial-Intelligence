# perceptron.py
# -------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

# Perceptron implementation
import util
import random
import classificationMethod



PRINT = True

class PerceptronClassifier:
  """
  Perceptron classifier.
  
  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  def __init__( self, legalLabels, max_iterations):
    self.legalLabels = legalLabels
    self.type = "perceptron"
    self.max_iterations = max_iterations
    self.weights = {}
    for label in legalLabels:
      self.weights[label] = util.Counter() # this is the data-structure you should use

  def setWeights(self, weights):
    assert len(weights) == len(self.legalLabels)
    self.weights == weights
      
  def train( self, trainingData, trainingLabels, validationData, validationLabels ):
    """
    The training loop for the perceptron passes through the training data several
    times and updates the weight vector for each label based on classification errors.
    See the project description for details. 
    
    Use the provided self.weights[label] data structure so that 
    the classify method works correctly. Also, recall that a
    datum is a counter from features to values for those features
    (and thus represents a vector a values).
    """
    
    self.features = trainingData[0].keys() # could be useful later
    # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
    # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
  
    for i in range(len(self.weights)):
      for k in range(len(self.features)):
        self.weights[i][self.features[k]] = random.randint(0,1)
      self.weights[i]["bias"] = random.randint(0,1)
  
    label_values = util.Counter()
    for iteration in range(self.max_iterations):
      print "Starting iteration ", iteration, "..."
      for i in range(len(trainingData)): 
        #Have to compute the summation of weights and feature values
        #NOTE: counter computes the dot product in the mul operator so it can be done with *
        for labels in self.legalLabels:
          label_values[labels] = trainingData[i] * self.weights[labels]
          label_values[labels] += self.weights[labels]["bias"]
        selected_label = label_values.argMax()
        if(trainingLabels[i] != selected_label):
          #This is if the selected_label does not match with actual label
          #Weights and bias for selected_label have to be subtracted
          #Weights and bias for actual label have to be added
          self.weights[trainingLabels[i]]+= trainingData[i]
          self.weights[trainingLabels[i]]["bias"] += 1
          #now to subtract from selected_label weights
          self.weights[selected_label] -= trainingData[i]
          self.weights[selected_label]["bias"] -= 1

    
  def classify(self, data ):
    """
    Classifies each datum as the label that most closely matches the prototype vector
    for that label.  See the project description for details.
    
    Recall that a datum is a util.counter... 
    """
    guesses = []
    for datum in data:
      vectors = util.Counter()
      for l in self.legalLabels:
        vectors[l] = self.weights[l] * datum
      guesses.append(vectors.argMax())
    return guesses

  
  def findHighWeightFeatures(self, label):
    """
    Returns a list of the 100 features with the greatest weight for some label
    """
    featuresWeights = []

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    

    

    return featuresWeights

