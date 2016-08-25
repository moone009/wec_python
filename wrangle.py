import pandas as pd
import glob

class wrangle:
    def __init__(self, df, dummycode,FilePath):
        self.df = df
        self.dummycode = dummycode
        self.FilePath = FilePath
     
    def dummycode(df,dummycode):
        
        dummies = pd.get_dummies(df[dummycode])
        dummies = pd.concat([df, dummies], axis=1)      
        dummies =  dummies.drop([dummycode], axis=1)
        
        return(dummies)
        
    def loopFolder(FilePath):
        path =FilePath # use your path
        allFiles = glob.glob(path + "/*.csv")
        frame = pd.DataFrame()
        list_ = []
        for file_ in allFiles:
            df = pd.read_csv(file_,index_col=None, header=0)
            list_.append(df)
        frame = pd.concat(list_)
        frame = frame.reset_index()
        frame = frame.drop('index', axis=1)

        return(frame)
        
        
        