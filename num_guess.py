import matplotlib.pyplot as plt
from sklearn import datasets, svm


# Loads digit datasets from Scikit-learn module
digits = datasets.load_digits()


# Creates SVM classifier object for sorting data by its features
clf = svm.SVC(gamma=0.0001, C=100)

# Sets aside last 10 data points for training and testing
X, y = digits.data[:-10], digits.target[:-10]

# Classifier trains model with given data and training sets
clf.fit(X, y)
print(f'Prediction: {clf.predict(digits.data[[-4]])}')

# Makes guess based on draw pad data


# Plots digit data for visual comparison
plt.imshow(digits.images[-4], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()