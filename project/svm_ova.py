from sklearn.svm import SVC
from utils import *
from sklearn.cross_validation import *
X,y=load_train()

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
svm=SVC()
svm.fit(X_train,y_train)
print(svm.score(X_val,y_val))

