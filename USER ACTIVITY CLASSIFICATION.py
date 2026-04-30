# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load Train dataset
url = "PycharmProjects/Code/data/trainnew1.csv"
names = ['program_desc', 'program_file', 'days', 'slots', 'activity_class', 'specific Class']
dataset = pandas.read_csv(url, names=names)
# Load Test dataset
urlT = "PycharmProjects/Code/data/teststep.csv"
namesT = ['program_desc', 'program_file', 'days', 'slots', 'activity_class', 'specific Class']
datasetT = pandas.read_csv(urlT, names=namesT)
# shape
print(dataset.shape)
# shape
print(datasetT.shape)
from sklearn.preprocessing import LabelEncoder
    #if dataset[column].dtype == type(object):        
pd = LabelEncoder()
dataset['program_desc'] = pd.fit_transform(dataset['program_desc'])
pf = LabelEncoder()
dataset['program_file'] = pf.fit_transform(dataset['program_file'])
d = LabelEncoder()
dataset['days'] = d.fit_transform(dataset['days'])
s = LabelEncoder()
dataset['slots'] = s.fit_transform(dataset['slots'])
ac = LabelEncoder()
dataset['activity_class'] = ac.fit_transform(dataset['activity_class'])
sc = LabelEncoder()
dataset['specific Class'] = sc.fit_transform(dataset['specific Class'])
                
pdT = LabelEncoder()
datasetT['program_desc'] = pdT.fit_transform(datasetT['program_desc'])
pfT = LabelEncoder()
datasetT['program_file'] = pfT.fit_transform(datasetT['program_file'])
dT = LabelEncoder()
datasetT['days'] = dT.fit_transform(datasetT['days'])
sT = LabelEncoder()
datasetT['slots'] = sT.fit_transform(datasetT['slots'])
acT = LabelEncoder()
datasetT['activity_class'] = acT.fit_transform(datasetT['activity_class'])
scT = LabelEncoder()
datasetT['specific Class'] = scT.fit_transform(datasetT['specific Class'])
print (datasetT.columns)

datasetT
# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
plt.show()

# scatter plot matrix
scatter_matrix(dataset)
plt.show()
# Split-out validation dataset
array = dataset.values
X = array[:,1:2]
#print (X)
Y = array[:,4]
#print (Y)
validation_size = 0.10
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
arrayT = datasetT.values
XT = arrayT[:,1:2]
#XT = arrayT[:,1]
print (XT)
YT = arrayT[:,4]
XT_validation=XT

YT_validation=YT
print YT_validation

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
#models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('DecisionTree', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []

for name, model in models:
    
            
        kfold = model_selection.KFold(n_splits=10, random_state=seed)
        cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(msg)
        
        
# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X, Y)

nb=GaussianNB()
nb.fit(X, Y)
predictions3 = nb.predict(XT_validation)
datasetT['Naive Bays class']=predictions3

svm=SVC()
svm.fit(X, Y)
predictions4 = svm.predict(XT_validation)
datasetT['svm class']=predictions4


from sklearn import tree
tree = tree.DecisionTreeClassifier()
tree.fit(X, Y)
#print X_train
print tree
#print Y_train
#print X_validation
predictions = tree.predict(XT_validation)
predictions2 = knn.predict(XT_validation)
print predictions
datasetT['activity_class']=predictions
datasetT['Decision Tree class']=predictions
datasetT['KNN class']=predictions2
#predictions=sc.inverse_transform(predictions)
#print predictions
datasetT['program_desc'] = pdT.inverse_transform(datasetT['program_desc'])
datasetT['program_file'] = pfT.inverse_transform(datasetT['program_file'])
datasetT['days'] = dT.inverse_transform(datasetT['days'])
datasetT['slots'] = sT.inverse_transform(datasetT['slots'])
datasetT['activity_class'] = ac.inverse_transform(datasetT['activity_class'])
datasetT['specific Class'] = scT.inverse_transform(datasetT['specific Class'])

datasetT['Decision Tree class'] = ac.inverse_transform(datasetT['Decision Tree class'])
datasetT['KNN class'] = ac.inverse_transform(datasetT['KNN class'])
datasetT['Naive Bays class']=ac.inverse_transform(datasetT['Naive Bays class'])
datasetT['svm class'] = ac.inverse_transform(datasetT['svm class'])

print datasetT
#print sc.inverse_transform(Y_validation)
# evaluate predictions
#accuracy = accuracy_score(Y_validation, predictions)
#print("Accuracy: %.2f%%" % (accuracy * 100.0))
datasetT.to_csv('PycharmProjects/Code/data/result.csv')
print ('PycharmProjects/Code/data/result.csv'+ 'hase been created.')
