import scipy
import pandas as pd

class summarystats:
    def __init__(self, df):
        self.df = df


    def dataframestats(df):

        Types = pd.DataFrame(df.dtypes)
        Types = Types.reset_index()
        
        Types.columns = ['VarName','VarType']
        Types['CompleteRecords'] = ''
        Types['MissingRecords'] = ''
        Types['Average'] =''
        Types['Median'] =''
        Types['StandardDeviation'] =''
        Types['Min'] =''
        Types['Max'] =''        
        Types['Possible_Nominal_UniqueRecords'] = ''
        Types['Skewness'] = ''
        for i in range(0,len(Types)):
            Types['MissingRecords'][i] = sum(pd.isnull(df[Types['VarName'][i]]).values.ravel())
            Types['CompleteRecords'][i] =  sum(df[Types['VarName'][i]].notnull().values.ravel())
            if str(df[Types['VarName'][i]].dtype) != 'object':
                Types['Average'][i] = df[Types['VarName'][i]].mean()
                Types['Median'][i] = df[Types['VarName'][i]].median()
                Types['Min'][i] = min(df[Types['VarName'][i]])
                Types['Max'][i] = max(df[Types['VarName'][i]])
                Types['StandardDeviation'][i] = df[Types['VarName'][i]].std()
                Types['Skewness'][i] = scipy.stats.skew(df[Types['VarName'][i]], axis=0, bias=True) 
            if len(pd.Series(df[Types['VarName'][i]].ravel()).unique()) < 32:
                Types['Possible_Nominal_UniqueRecords'][i] = len(pd.Series(df[Types['VarName'][i]].ravel()).unique())
        Types = Types.fillna('')        
        return(Types)
        
        
        
        