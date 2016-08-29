import math
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale

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
        
        df[Target] = df[Target].fillna(df[Target].median())
        
        return(df)
        
    def ValueImputationAverage(df,Target,IndicatorCol=False):
        if IndicatorCol == True:
            Col = Target + "_Missing"
            df[Col] = df[Target].isnull()
        
        df[Target] = df[Target].fillna(df[Target].mean())
        
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
        