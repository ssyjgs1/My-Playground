from matplotlib.collections import PolyCollection
from matplotlib import colors as mcolors
from matplotlib.ticker import NullFormatter
from matplotlib import transforms
from scipy.integrate import simps
from sklearn.impute import SimpleImputer
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from calendar import isleap
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.tri as mtri
import numpy as np
import koreanize_matplotlib
import string
import scipy as sp
import scipy.stats
import random
import missingno as msno
import patsy
import warnings
warnings.filterwarnings('ignore')
from patsy import demo_data
from patsy import dmatrix
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import FunctionTransformer

total_data = pd.read_csv("./total.csv")
data_g = pd.read_csv("./고구려.csv")
data_b = pd.read_csv("./백제.csv")
data_s = pd.read_csv("./신라.csv")

data_g_mean = data_g.mean()
data_b_mean = data_b.mean()
data_s_mean = data_s.mean()
# print(data_g_mean, data_b_mean, data_s_mean)
# show = pd.plotting.scatter_matrix(total_data,
# figsize=(30,30),
# marker='ro',
# alpha=0.5)
# plt.show()

colors= ['g','b','r']
fig,ax = plt.subplots(5,5, figsize=(20,20))
col_names = ['전체길이','모신부길이','모신부 최대폭','공부길이','공부직경']

for i, col1 in enumerate(col_names):
    for j, col2 in enumerate(col_names):
        for k, species in enumerate(total_data['국가'].unique()):
            plt.grid()
            siris = total_data[total_data['국가']==species]
            siris.plot.scatter(x=col1,y=col2, alpha=0.6,ax=ax[j][i], color=colors[k])
            

plt.show()