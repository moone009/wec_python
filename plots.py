
# Add Time Series
# Add Corrplot
#g = sns.PairGrid(df)
#g.map(plt.scatter);      


import seaborn as sns
import matplotlib 
import matplotlib.pyplot as plt
import math

class plots:
    def __init__(self, df,numericvar,numericvar_two, nominalvar):
        self.df = df
        self.numericvar = numericvar
        self.nominalvar = nominalvar

    def boxplot(df,numericvar,nominalvar):
        sns.boxplot(x=numericvar, y=nominalvar, data=df, palette="PRGn")
        sns.despine(offset=10, trim=True)

    def hist(df,numericvar):
        sns.distplot(df[numericvar])

    def barchart(df,nominalvar):
        Data = df.groupby(nominalvar).size().reset_index()
        Data.columns = [nominalvar,'Total']
        Data = Data.sort(['Total'], ascending=[False])
        sns.barplot(x=nominalvar, y="Total", data=Data)
 
    def scatterplot(df,numericvar,numericvar_two):
        sns.regplot(x=numericvar, y=numericvar_two, data=df)

    def draw_histograms(df):
        li = []
        RowNames = list(df.columns.values)
        DataType = df.dtypes
        for i in range(0,len(DataType)):
            if (str(DataType[i]) == 'int64') or (str(DataType[i]) == 'float64'):
                li.append(i)
        if len(li) == 1:
            df.ix[:,li[1]].hist(ax=axs[x]).plot()
        if (len(li) > 1) & (len(li) <= 4):
            Rows = len(li)
            Rows = int(Rows)
            print('Plotting: ' + str(len(li)) + ' variables by ' + str(Rows) + ' column(s)') 
            fig, axs = plt.subplots(nrows=1,ncols=Rows,figsize=(15, 19))
            x_rows = 0 
            x_cols = 0
            x = 0
            for i in li:
                    df.ix[:,li[x]].hist(ax=axs[x_cols]).plot()
                    axs[x_cols].set_title(RowNames[li[x]])
                    x_cols = x_cols+1
                    x = x+1
                    if x_cols == 4:
                        x_rows = x_rows + 1
                        x_cols = 0                    
        if  len(li) > 4:
            Rows = math.ceil(len(li)/4)
            Rows = int(Rows)
            print('Plotting: ' + str(len(li)) + ' variables by ' + str(Rows) + ' column(s)') 
            fig, axs = plt.subplots(nrows=Rows,ncols=4,figsize=(15, 19))
            x_rows = 0 
            x_cols = 0
            x = 0
            print(len(li))
            for i in li:
                    df.ix[:,li[x]].hist(ax=axs[x_rows,x_cols]).plot()
                    axs[x_rows,x_cols].set_title(RowNames[li[x]])
                    x_cols = x_cols+1
                    x = x+1
                    if x_cols == 4:
                        x_rows = x_rows + 1
                        x_cols = 0
                        
                        
                        
                        
                 
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        