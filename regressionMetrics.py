
## from regressionMetrics import * 
## performancemetrics.regression_metrics(predictions,Y_train)

import math 
import pandas as pd

class performancemetrics:
    def __init__(self, predictions,test_var):
        self.predictions = predictions
        self.test_var = test_var

    def regression_metrics(predictions,test_var):
        
        predictions = pd.DataFrame(predictions)
        
        nrows = len(pd.DataFrame.as_matrix(test_var))
        sum = test_var.sum()
        average =  float(sum/nrows)
        
        SSR = (predictions - average) ** 2
        SSR = SSR.sum()
    
        SSE = (pd.DataFrame.as_matrix(test_var)-predictions) ** 2
        SSE = SSE.sum()
    
        SST = (pd.DataFrame.as_matrix(test_var) - average) ** 2
        SST = SST.sum()
        R2 = SSR/SST
        
        
        RMSE = (predictions - pd.DataFrame.as_matrix(test_var)) ** 2
        RMSE = RMSE.sum()
        RMSE = math.sqrt(RMSE) / len(predictions)
        
        MAE = predictions - pd.DataFrame.as_matrix(test_var)
        MAE =  MAE.abs().sum()/ len(predictions)
        
        values = [['Numer of Predictions',len(predictions)],
                ['Numer of Test Variables',nrows],
                ['SSR',SSR],['SSE',SSE],
                ['SST',SST],
                ['R2',R2],
                ['MAE',MAE],
                ['RMSE',RMSE]]
        df = pd.DataFrame(values, columns=['Measurement', 'value'])
        df.a = df.value.astype(float).fillna(0.0)
        return(df)