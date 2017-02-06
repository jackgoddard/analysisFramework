from pandasAnalysisFramework import framework as fwrk

import pandas


def string2float(str):
    return float(str)



dataFile = 'data/Iris.csv'

dataVars = ['Id',
            'SepalLengthCm',
            'SepalWidthCm',
            'PetalLengthCm',
            'PetalWidthCm',
            'Species'
            ]

dataTypes = {
    
    1 : string2float ,
    2 : string2float ,
    3 : string2float ,
    4 : string2float

    }

df_import = pandas.read_csv( dataFile, converters = dataTypes )


#print(df_import.head())

fw = fwrk()

fw.setVerbose(True)
fw.setDebug(False)

fw.importDataFrame(df_import)

fw.dataFrame()


histograms = {'h_sepal_length' : 'SepalLengthCm', 
              'h_petal_length' : 'PetalLengthCm'
              }


print(histograms['h_sepal_length'])



print(fw.dataFrame()[histograms['h_sepal_length']])



fw.getHistDefinitions()

fw.produceJsonHists()

#fw.produceHistograms('test3', histograms)

#fw.printPdfFile()
