# -------------------------------------------------------------------------
# AUTHOR: Linus Palm
# FILENAME: decision_tree.py
# SPECIFICATION: This program reads the contact_lens.csv file and outputs a decision tree.
# FOR: CS 4210- Assignment #1
# TIME SPENT: 5 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

# transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
# --> add your Python code here

# transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> addd your Python code here

valuetonumber = {
    'Young': 1,
    'Prepresbyopic': 2,
    'Presbyopic': 3,
    'Myope': 1,
    'Hypermetrope': 2,
    'Yes': 1,
    'No': 2,
    'Reduced': 1,
    'Normal': 2
}

for sample in db:
    numbersample = []
    for value in sample:
        numbersample.append(valuetonumber[value])
    Y.append(numbersample.pop())
    X.append(numbersample)

# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes', 'No'], filled=True,
               rounded=True)
plt.show()
