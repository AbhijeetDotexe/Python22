#How import Works in Python
# import sklearn as sk
# print(sk.__version__)
# import sys
# print(sys.path)
from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

import file2
print(file2.a)
file2.joke(" hahahahaha")

from file2 import a
print(a)

