## Regression and classification

The aim of the exercise is to implement decision trees created with the algorithm
ID3 with a maximum tree depth constraint.

Then use the created algorithm to create and test the quality of classifiers for the Cardio Vascular Disease Detection dataset
(https://www.kaggle.com/datasets/bhadaneeraj/cardio-vascular-disease-detection).
The class is the cardio field. Find the value of the maximum depth parameter that gives the best result.

Some of the attributes in the dataset are not discrete - age, weight, height , systolic pressure (ap hi), diastolic pressure (ap lo). These should be discretised by dividing the values into ranges of your choice.

Be sure to divide the data into training, validation and test sets. Ready-made functions can be used for this purpose.