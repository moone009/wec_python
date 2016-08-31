import math
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale
import random
from random import sample
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score

class missingvalues:
    def __init__(self, df,Target,IndicatorCol,k):
        self.df = df
        self.Target = Target
        self.IndicatorCol = IndicatorCol
        self.k = k
            
    def ValueImputationMedian(df,Target,IndicatorCol=False):
        if IndicatorCol == True:
            Col = Target + "_Missing"
            df[Col] = df[Target].isnull()
        
        # Removing because it updates the input dataset as well which causes issuses for selectbest function
        #df[Target] = df[Target].fillna(df[Target].median())
        
        # obtain missing values
        impute = df[pd.isnull(df).any(axis=1)]
        
        # Drop na values
        df = df.dropna()  
        
        # update na values
        impute[Target] = df[Target].median()
        df = df.append(impute)
        
        return(df)  
                        
    def ValueImputationAverage(df,Target,IndicatorCol=False):
        if IndicatorCol == True:
            Col = Target + "_Missing"
            df[Col] = df[Target].isnull()
        
        # Removing because it updates the input dataset as well which causes issuses for selectbest function
        #df[Target] = df[Target].fillna(df[Target].mean())
        
        # obtain missing values
        impute = df[pd.isnull(df).any(axis=1)]
        
        # Drop na values
        df = df.dropna()  
        
        # update na values
        impute[Target] = df[Target].mean()
        df = df.append(impute)
        
        return(df)    
        
    def ValueImputationRegression(df,target):     
        
        # obtain missing values
        impute = df[pd.isnull(df).any(axis=1)]
        impute = impute.drop(target, axis=1)
        
        # Drop na values
        df = df.dropna()     
        
        # Split the data into training/testing sets
        target_ = df[target]
        features = df.drop(target, axis=1)

        # Create linear regression object
        regressor = LinearRegression()
        regressor.fit(features,target_)
        predictions = regressor.predict(impute)
        impute[target] = predictions
        
        # bind data
        loc = df.columns.get_loc(target)
        imputelocation = impute.columns.get_loc(target)
        length = list(range(df.shape[1]))
        correction = list(range(loc)) 
        correction.append(imputelocation)
        correctCol = correction + [i for i in length if i not in correction]
        impute = impute[correctCol]
        
        #return data
        df = df.append(impute)
        return(df)
        
    def ValueImputationKNN(df,target,k):     
        
        # obtain missing values
        impute = df[pd.isnull(df).any(axis=1)]
        impute = impute.drop(target, axis=1)
        
        # Drop na values
        df = df.dropna()     
        
        # Split the data into training/testing sets
        target_ = df[target]
        features = df.drop(target, axis=1)

        # Create linear regression object
        knn=KNeighborsClassifier(n_neighbors=k)
        knn.fit(scale(features),target_)
        predictions = knn.predict(scale(impute))
        impute[target] = predictions
        
        # bind data
        loc = df.columns.get_loc(target)
        imputelocation = impute.columns.get_loc(target)
        length = list(range(df.shape[1]))
        correction = list(range(loc)) 
        correction.append(imputelocation)
        correctCol = correction + [i for i in length if i not in correction]
        impute = impute[correctCol]
        
        #return data
        df = df.append(impute)
        return(df)
    
    def Selectbest(df,target,k):

        # obtain missing values
        #impute = df[pd.isnull(df).any(axis=1)]
        #impute = impute.drop(target, axis=1)
        
        # Drop na values
        df = df.dropna()     
        
        # Test set
        rindex =  np.array(sample(range(len(df)), int(len(df)*.1)))
        test = df.ix[rindex]
        OriginalValues = list(test[target])
        test[target] = np.NaN

        # Train
        train = df.drop(df.index[rindex])
        train = train.append(test)
        
        # Median
        Median = missingvalues.ValueImputationMedian(train,target)
        print("Median MSE: %d" % mean_squared_error(y_true = OriginalValues, y_pred = Median.ix[test.index][target]))
        
        # Mean
        Mean = missingvalues.ValueImputationAverage(train,target)
        print("Mean MSE %d:" % mean_squared_error(y_true = OriginalValues, y_pred = Mean.ix[test.index][target]))
        
        # Regression
        Regression = missingvalues.ValueImputationRegression(train,target)
        print("Regression MSE: %d" % mean_squared_error(y_true = OriginalValues, y_pred = Regression.ix[test.index][target]))

        # Knn
        knn = missingvalues.ValueImputationKNN(train,target,k)
        print("KNN MSE: %d" % mean_squared_error(y_true = OriginalValues, y_pred = knn.ix[test.index][target]))
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        