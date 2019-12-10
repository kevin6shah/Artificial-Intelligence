# <p align = "center"> Introduction to Artificial Intelligence </p>

<p align = "center"> CS440 - Final Assignment </p>
<p align = "center"> Image Classification </p>
<p align = "center"> Kevin Shah (kas665), Manav Patel (mpp124), and Ciera Fedell (clf124) </p>
<p align = "center"> December 9, 2019 </p>


## Features Used:

<p align = "center">For every classifying algorithm, the image had to be broken down into
features. These features give specific, individualized data for every section of
the image. These features are then used to classify the images based on
certain conditions and training.
In our case, we utilized a very simple feature extraction. We made each pixel
into a feature, and the value of that pixel (0 if off, 1 if on) was used as the
feature value. These features were then used to calculate and adjust weights
as well as create conditional probability tables in the following algorithms.

## Perceptron:

<p align = "center">The perceptron algorithm is a simple, intuitive, but highly effective algorithm
to classify things. In this case, it was used to detect faces and digits. The
perceptron works by training the weights for each feature, for each label. The
process of training the weights is the following: First the weights were
initialized randomly to either a 0 or 1. This is because the features used took
on those values and the computation of the weights depended on feature
values. For each training image, it computed the expected label. This was
done by multiplying each feature value by its corresponding weight value.
This was done for each label. Once this dot product was computed, the max
of all the labels was selected. This max label, was used as the expected label,
the predicted label.
<p align = "center">If the predicted label matched the actual label, nothing was done to the
weights and it continued on to the next image. However, if the label did not
match two things were done. The predicted, false, label had all of its
corresponding weights and bias subtracted by their corresponding feature values at each location. And the actual label had all of its weight values and
bias incremented in the same manner. This intuitively makes sense because
we are using the max values to assign labels. It would only make sense, to
subtract from the wrongly predicted values and add to the actual weight
vector.

## Naive Bayes Classifier:
<p align = "center">The Naive Bayes classifier essentially just uses the Bayes theorem. The
theorem is as follows:
<p align = "center">What we are essentially trying to find is the conditional probability of a
particular label given an image. The algorithm first computes P(y) which is
simply the number of times a given label occurs in the training label data
divided by the total number of training label data provided. Finding the
conditional probability was the tricky part.
<p align = "center">Because the image is composed of a bunch of features, we have to find the
product of the conditional probability of all features given a particular label.
We trained the algorithm by simply creating a table for the probability of a
feature occurring given a label has occurred. So for each label, we check just
from the pile of that label, how many times a given feature value occurs at
the particular location of the feature.

<p align = "center">Finally, we needed to be able to predict for a given test datum. To increase
our accuracy for the Bayes classifier, we chose to implement log probabilities
into the equation to get rid of the underflow:
There was a problem though that if we have a probability of 0 when we look
up in the training table, we would get inaccurate predictions and errors. So
we just changed the value of the probability to a very small value (0.0001).

## Mira:
<p align = "center">Mira is similar to perceptron, but tracks and updates weight vectors of
expected and true values based on the difference between the weights. It
knows the expected and true labels from scanning the data for each instance
and compares the two. As in perceptron, the variable y prime is taken as the
maximum label of this set. If y and y prime, the two labels, do not match, they
are updated according to the following equations:
_wy_ = _wy_ +τ _f
wy f_
′
= _wy_
′
−τ
τ= _min_ { _C_ , }

2 || _f_ || (^22)
( _wy_ ′− _wy_ ) _f_ + 1
<p align = "center">Above, y is the true label, _w_ is the weight of the true label, y prime is the^
_y_
expected label, and _wy_ is the weight of the expected label. C is a cap which is
′
<p align = "center">added to prevent too large of an update from happening at once, as may
happen when encountering an outlier or bad data point. If y and y prime
match, the weights are not updated and the next point is tested, repeating
the same process.


## Performance Analysis:

### PERCEPTRON:

<p align = "center">For the perceptron, it was evident that the weights for the face-recognition
were trained slightly faster than the training of digit-recognition. Also, the
training-testing accuracies converged faster for the face recognition
compared to digits. This was expected as recognizing something as a face or
not is a binary decision to make, while digits had ten labels to choose from.
Also standard deviation was better for digits than perceptron because it
utilized a larger data set.
### NAIVE BAYES:
<p align = "center">Accuracy was of course better faces over digits because faces had binary
features while the digit recognition had many more features. Automatically,
with binary features, the lowest probability one should be getting is 50%
which means automatically has the advantage.
### MIRA:
<p align = "center">Mira was able to train faces much more quickly than digits. While both
training times increased linearly with the percentage of training data utilized,
<p align = "center">training digits resulted in a much steeper slope for time increase. Faces
showed more accuracy improvement based on the training size, although
both were roughly linear again and were very similar in accuracy. It therefore
follows that the prediction error decreased more overall for faces, though
both showed the same downward trend with the amount of data used.
Because there is much more data in the digits training set (5000) vs faces
(451), it would be expected that given the same number of training points,
faces would become reasonably more accurate than digits with the same
algorithm.
