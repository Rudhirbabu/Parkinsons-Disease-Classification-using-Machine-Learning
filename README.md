# Parkinsons-Disease-Classification-using-Machine-Learning
## Problem Statement
Parkinson’s disease is a neurodegenerative disorder that affects millions of people
around the globe. Detecting Parskinson’s disease at an earlier stage could help to better diagnose the disease.

This disease largely limits the patient’s movement and speech abilities. The patient develops a tendency to fall frequently hence, ending up hurt with various injuries. Thus, it is very important to monitor and notify either the patients or their caregivers about the severity of the disease.

Popular machine learning algorithms are applied to the given dataset so as to classify people whether they are affected or not.

## Dataset
Our dataset is from Kaggle listed under the name “Parkinson’s Disease Classification” and it initially included about 3 million data points. It contained 27 features and 1 label which can be examined. Two data points from the unprocessed dataset We processed some of the existing features, created new features that we thought could be useful for prediction, and discarded some features using the library Pandas.

## Dataset Information
The PD database consists of training and test files. The training data belongs to 20 PWP (6 female, 14 male) and 20 healthy individuals (10 female, 10 male) who appealed at the Department of Neurology in Cerrahpasa Faculty of Medicine, Istanbul University. From all subjects, multiple types of sound recordings (26 voice samples including sustained vowels, numbers, words, and short sentences) are taken. A group of 26 linear and time frequency-based features are extracted from each voice sample. UPDRS (Unified Parkinson’s Disease Rating Scale) score of each patient which is determined by an expert physician is also available in this dataset.

During the collection of this dataset, 28 PD patients are asked to say only the sustained vowels 'a' and 'o' three times respectively which makes a total of 168 recordings. The same 26 features are extracted from voice samples of this dataset. This dataset can be used as an independent test set to validate the results obtained on the training set.

## Steps used for solving the problem
1. Read the Input dataset.
2. Perform all necessary Data Normalization, Standardization processing to prepare the transformed format of the given input dataset.
3.  Impute Missing values
4.  Perform Exploratory Data Analysis/Visualization and bring insights into the predictor variables.
5.  Apply Logistic Regression Classification, Gaussian Naïve Bayes, and Decision tree classifier by splitting data into train and test.
6.  Measure the Performance of the model using K-fold Cross Validation and obtain the values of Accuracy, Precision, and Recall.
7.   Apply statistical tests to explain the goodness of fit.
