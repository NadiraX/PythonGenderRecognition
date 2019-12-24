import os
import pandas
import numpy
os.environ['R_USER'] = 'C:/Users/wszcz' #path depends on where you installed Python. Mine is the Anaconda distribution


from rpy2.robjects.packages import importr
from rpy2.robjects import r, pandas2ri
pandas2ri.activate()
# utils = importr('utils')
# utils.install_packages('warbleR')
warbleR = importr('warbleR')

dataframe = pandas.DataFrame([['001_K.wav',int(1),int(2),int(3)]],columns=['sound.files', 'selec', 'start', 'end'])

print(dataframe)
print(warbleR.specan(X=dataframe,bp=r.c(0,28000)))