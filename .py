# Importing Libraries 
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets

# Importing metrics
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Importing classification algorithms
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB


# below package is for plotting box plots
import matplotlib.pyplot as plt
%matplotlib inline

# Loading test dataset
x_=pd.read_csv('test_data.csv')
x_.shape

# Loading train dataset
y_=pd.read_csv('train_data.csv')
y_.shape

# display of attribute names and top 5 rows of train dataset
x_.head()

# display of attribute names and top 5 rows of train dataset
y_.head()

# concatenation of x and y dataframe which containing test and train datasets
data=pd.concat([x_,y_]) 

# displaying Concatenated data
data.head()

## display of data
data

# description of data
data.describe()

# data after filling Nan values in UPDRS attribute 
data.UPDRS.fillna(13.000000,inplace=True)

# column names for data
data.columns

# To check data types of data 
data.dtypes

# replacing class to Class 
data.rename(columns={'class':'Class'}, inplace=True)

# To check class imbalance in Class Attribute
data.Class.value_counts() 

# Checking non-categorical features
non_cat_feature=[col for col in data.columns if data[col].dtypes!='O'] #categorical features data ki find cheyala leka train dataset ki matrame na?
print(non_cat_feature)

# listing out categorical features
cat_feature=[col for col in data.columns if data[col].dtypes=='O']
print(cat_feature)

# Plotting histograms for visualization to observe whether the data is normally distributed or not
data.hist(figsize=(20,20))
plt.show()

# heatmap for visualization to check correlation between variables  
corrmat=data.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=.8,square=True)
plt.show()

# display correlation matrix in values
corrmat

# Dropping id feature
data=data.drop(['id'],axis=1)

# All the variables have 1208 records, indicating that there is no missing value in the data.
print(data.shape)
print(data.info())

# Describing features
data.describe()

#Identifying Outliers with Interquartile Range (IQR)
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

#Replacing outlier values with median
print(data.quantile(0.50)) 
print(data.quantile(0.95))
#data['locJitter'] = np.where(data['locJitter'] > 5.36, 2.15, data['locJitter'])
#data.describe()

# Imputing outliers within the range of dimensions.
data['locJitter'] = np.where(data['locJitter'] > 3.7, 2.14, data['locJitter'])
data['locabsJitter'] = np.where(data['locabsJitter'] > 0.000267, 0.000133, data['locabsJitter'])
data['rapJitter'] = np.where(data['rapJitter'] > 1.82, 0.924125, data['rapJitter'])
data['ppq5Jitter'] = np.where(data['ppq5Jitter'] > 1.98, 0.988125, data['ppq5Jitter'])
data['ddpJitter'] = np.where(data['ddpJitter'] > 5.46, 2.773125, data['ddpJitter'])
data['locShimmer'] = np.where(data['locShimmer'] > 17.28, 11.442500, data['locShimmer'])
data['locdBShimmer'] = np.where(data['locdBShimmer'] > 1.5, 1.111000, data['locdBShimmer'])
data['apq3Shimmer'] = np.where(data['apq3Shimmer'] > 7.81, 4.794125, data['apq3Shimmer'])
data['apq5Shimmer'] = np.where(data['apq5Shimmer'] > 10.94, 6.427750, data['apq5Shimmer'])
data['apq11Shimmer'] = np.where(data['apq11Shimmer'] > 16.94, 10.458875, data['apq11Shimmer'])
data['ddaShimmer'] = np.where(data['ddaShimmer'] > 23.44, 14.381500, data['ddaShimmer'])
data['AC'] = np.where(data['AC'] > 0.8, 0.867694, data['AC'])
data['NTH'] = np.where(data['NTH'] > 0.3, 0.186532, data['NTH'])
data['HTN'] = np.where(data['HTN'] > 16.6, 10.209125, data['HTN'])
data['Median_pitch'] = np.where(data['Median_pitch'] > 214.2, 152.200875, data['Median_pitch'])
data['Mean_pitch'] = np.where(data['Mean_pitch'] > 223.5, 155.508125, data['Mean_pitch'])
data['Standard_deviation'] = np.where(data['Standard_deviation'] > 42.1, 11.059875, data['Standard_deviation'])
data['Minimum_pitch'] = np.where(data['Minimum_pitch'] > 180.6, 128.186750, data['Minimum_pitch'])
data['Maximum_pitch'] = np.where(data['Maximum_pitch'] > 346.86, 188.917750, data['Maximum_pitch'])
data['Number_of_pulses'] = np.where(data['Number_of_pulses'] > 178, 76.000000, data['Number_of_pulses'])
data['Number_of_periods'] = np.where(data['Number_of_periods'] > 176.0, 72.000000, data['Number_of_periods'])
data['Mean_period'] = np.where(data['Mean_period'] > 0.008, 0.006455, data['Mean_period'])
data['Standard_deviation_of_period'] = np.where(data['Standard_deviation_of_period'] > 0.0008, 0.000582, data['Standard_deviation_of_period'])
data['Fraction_of_locally_unvoiced_frames'] = np.where(data['Fraction_of_locally_unvoiced_frames'] > 49.6, 21.668375, data['Fraction_of_locally_unvoiced_frames'])
data['Number_of_voice_breaks'] = np.where(data['Number_of_voice_breaks'] > 2, 1.000000, data['Number_of_voice_breaks'])
data['Degree_of_voice_breaks'] = np.where(data['Degree_of_voice_breaks'] > 27.2, 0.69, data['Degree_of_voice_breaks'])
data['UPDRS'] = np.where(data['UPDRS'] > 32, 8.000000, data['UPDRS'])

#Outlier removal using IQR
df_out = data[~((data < (Q1 - 1.5 * IQR)) |(data > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df_out.shape)

# Shape of data
print(df_out.shape)

# Class Imbalance check
df_out.Class.value_counts()

#Outlier replacing with median
data3 = np.array(df_out['HTN'].values.tolist())
df_out['HTN']=np.where(data3>14.744200,10.209125,data3).tolist()#3.5622500000000015
data4 = np.array(df_out['HTN'].values.tolist())
df_out['HTN']=np.where(data4<3.5622500000000015,10.209125,data4).tolist()

# Dropping features values
df_out.drop(df_out[(df_out.Number_of_periods>165.5)|(df_out.Number_of_periods<-30.5)].index,inplace=True)
df_out.drop(df_out[(df_out.HTN>16.146500000000003)|(df_out.HTN<4.4765)].index,inplace=True)
df_out.drop(df_out[(df_out.locdBShimmer>1.8595)|(df_out.locdBShimmer<0.12750000000000006)].index,inplace=True)

#Outlier replacing with median
data1 = np.array(df_out['UPDRS'].values.tolist())
df_out['UPDRS']=np.where(data1>31.000000,8.000000,data1).tolist()
#Outlier replacing with median
data2 = np.array(df_out['Number_of_periods'].values.tolist())
df_out['Number_of_periods']=np.where(data2>153.150000,72.000000,data2).tolist()
df_out.drop('AC',axis=1,inplace=True)
df_out.drop('Degree_of_voice_breaks',axis=1,inplace=True)
df_out.describe()

# Saving in dataframe
Final_data=df_out

#For Classification and best fit line at final classification  feature selection
a=Final_data.drop(columns='Class',axis=1)#independent variables 
b=Final_data['Class'] #Target variable

# Minmax Normalization of feature
from sklearn import preprocessing 
  
""" MIN MAX SCALER """
  
min_max_scaler = preprocessing.MinMaxScaler(feature_range =(0, 1)) 
  
# Scaled feature 
Final_data = min_max_scaler.fit_transform(Final_data) 
print ("\nAfter min max Scaling : \n", Final_data) 

#Converting into DataFrame
import pandas as pd
Final_data = pd.DataFrame(Final_data)
Final_data

df_out.describe()

# Appending column names
Final_data.columns=['locJitter','locabsJitter','rapJitter','ppq5Jitter','ddpJitter','locShimmer','locdBShimmer','apq3Shimmer','apq5Shimmer','apq11Shimmer','ddaShimmer','NTH','HTN','Median_pitch','Mean_pitch','Standard_deviation','Minimum_pitch','Maximum_pitch','Number_of_pulses','Number_of_periods','Mean_period','Standard_deviation_of_period','Fraction_of_locally_unvoiced_frames','Number_of_voice_breaks','Class','UPDRS']
Final_data
Final_data['Class']=Final_data['Class'].astype(int)
df=Final_data

## Get the Fraud and the normal dataset 

Diseased = data[data['Class']==1]

Healthy = data[data['Class']==0]

# Independent and dependent features
X = df.drop("Class", 1)       # feature matrix 
y = df['Class']               # target feature

# Visualization of features using histograms
df.hist(figsize=(20,20))
plt.show()

**Sequential Forward selection**

import statsmodels.api as sm
def backward_elimination(df, target,significance_level = 0.05):
    features = df.columns.tolist()
    while(len(features)>0):
        features_with_constant = sm.add_constant(df[features])
        p_values = sm.OLS(target, features_with_constant).fit().pvalues[1:]
        max_p_value = p_values.max()
        if(max_p_value >= significance_level):
            excluded_feature = p_values.idxmax()
            features.remove(excluded_feature)
        else:
            break 
    return features
	
backward_elimination(X,y) 

#importing the necessary libraries
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.linear_model import LinearRegression

#For plotting Kfeatures
sfs1 = SFS(LinearRegression(), 
          k_features=(3,11), 
          forward=True, 
          floating=False,
          cv=0)
sfs1.fit(X, y)

#SFS visualization
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt
fig1 = plot_sfs(sfs1.get_metric_dict(), kind='std_dev')
plt.title('Sequential Forward Selection (w. StdErr)')
plt.grid()
plt.show()

#Logistic regression classifier using sklearn
from matplotlib import pyplot as plt
plt.scatter(df.UPDRS,df.Class,marker='+',color='red')

# Seperating dependent and independent features
X=df.drop(['Class'],axis=1)
y=df['Class']
X.shape,y.shape

# splitting X and y into training and testing sets
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split

**Function declaration**
#Function to Train and Test Machine Learning Model
def train_test_ml_model(X_train,y_train,X_test,Model):
    model.fit(X_train,y_train) #Train the Model
    y_pred = model.predict(X_test) #Use the Model for prediction

    # Test the Model
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test,y_pred)
    accuracy = round(100*np.trace(cm)/np.sum(cm),1)

    #Plot/Display the results
    cm_plot(cm,Model)
    print('Accuracy of the Model' ,Model, str(accuracy)+'%')
    from sklearn.metrics import classification_report
    print(Model)
    print(classification_report(y_test,y_pred)
	
#Function to plot Confusion Matrix
def cm_plot(cm,Model):
    plt.clf()
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Wistia)
    classNames = ['Negative','Positive']
    plt.title('Comparison of Prediction Result for '+ Model)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    tick_marks = np.arange(len(classNames))
    plt.xticks(tick_marks, classNames, rotation=45)
    plt.yticks(tick_marks, classNames)
    s = [['TN','FP'], ['FN', 'TP']]
    for i in range(2):
        for j in range(2):
            plt.text(j,i, str(s[i][j])+" = "+str(cm[i][j]))
    plt.show()
    print(cm[1][0])
	
**Logistic Regression**

# Import packages related to Model
from sklearn.linear_model import LogisticRegression  
Model = "LogisticRegression"
model=LogisticRegression()

train_test_ml_model(X_train,y_train,X_test,Model)


**Gaussian Naive Bayes Classifier**

from sklearn.naive_bayes import GaussianNB
Model = "GaussianNB"
model=GaussianNB()

train_test_ml_model(X_train,y_train,X_test,Model)


**Decision Tree Classifier**

from sklearn.tree import DecisionTreeClassifier
Model = "DecisionTreeClassifier"
model=DecisionTreeClassifier()

train_test_ml_model(X_train,y_train,X_test,Model)

# KFold cross validation

**cross_val_score function**

from sklearn.model_selection import cross_val_score

 #Average of Accuracy of Logistic Regression Classifier
 score1=cross_val_score(LogisticRegression(),X,y,cv=10,scoring='accuracy').mean()
 print('Accuracy of LogisticRegression:',score1)
 
 
 #Average of Accuracy of Gaussian Naive Bayes Classifier
score2=cross_val_score(GaussianNB(),X,y,cv=10,scoring='accuracy').mean()
print('Accuracy of Gaussian Naive Bayes Classifier:',score2)

#Average of Accuracy of Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
score3 = cross_val_score(DecisionTreeClassifier(),X,y,cv=10,scoring='accuracy').mean()
print('Accuracy of Decision Tree Classifier:',score3)

# T-test

#Function declaration for T-test 
def ttest_Classify(Model1,Model2):
    Pa=cross_val_score(Model1,X,y,cv=100,scoring='accuracy')
    Pb=cross_val_score(Model2,X,y,cv=100,scoring='accuracy')
    di=abs(Pa-Pb)
    #print(di)
    import statistics
    print("Variance of sample set is sigma2: % s" %(statistics.variance(di)))
    d_mean=sum(di)/100
    print('Mean:',d_mean)
    #print((di-d̅))
    #print(d-d̅)

# Comparison between two models	
Model1=LogisticRegression()
Model2=GaussianNB()
ttest_Classify(Model1,Model2)

sigma2=0.007883796644127224
d_mean=0.030909090909090907
#compute the number of data points used for training 
n1 = len(y_train)
#compute the number of data points used for testing 
n2 = len(y_test)
#compute the total number of data points
n = len(y)

# Printing values
print(n1)
print(n2)
print(n)

#compute the modified variance
sigma2_mod = sigma2 * (1/n + n2/n1)
#compute the t_static
t_static =  d_mean / np.sqrt(sigma2_mod)
from scipy.stats import t
#Compute p-value and plot the results 
Pvalue = ((1 - t.cdf(t_static, n-1))*200)/100

Pvalue

print(t_static)

**The p-value is .595961**

**The result is not significant at p>.05.**

# So it accepts Null hypothesis,states that there is no difference between the performance of two ML models, that are LogisticRegression and Gaussian Naive Bayes.
