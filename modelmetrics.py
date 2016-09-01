
class modelmetrics:
    def __init__(self, actual,predictions):
        self.actual = actual
        self.predictions = predictions

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
        
        return(SSR,SSE,SST)