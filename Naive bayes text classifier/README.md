# Naive-Bayes-Text-Classifier
1)Naive Bayes text classifier is a supervised learning method that uses probabilistic learning method to classify a given text based on training data .
2)We are classifying a given hotel review to be positive/negative review and as either a real/fake review.

3)The folder structure for training and testing data needs to be as follows:

root
(folder)---->positive review
(sub-folder)---->--->Deceptive review
(sub-folder)---->--->Truthful review 
(folder)---->Negative review
(sub-folder)---->--->Deceptive review
(sub-folder)---->--->Truthful review 

4) The input format is  text files with one review in each file.
Also the reviews which needs to be evaluated also needs to be in the same format.


5)Process:
1) First the Naive Bayes classifier is trained and model data is generated.( A text file is created)
2) Based on the training data classifier the given test data is tagged to its review to be truthful/deceptive and positive/negative review.

6) All the input files need to be in '.txt' format. 

Commands:
1)Run the nblearn.py
python nblearn.py "root path"

This will generate the model parameters file "nbmodel.txt"

2)Run the classifier nbclassify.py
python nblearn.py "root path of the files whose reviews are to be evaluated"

3) Finally output will be generated in the file "nbmodel.txt" with as follows for each file
LabelA labelB filename.



