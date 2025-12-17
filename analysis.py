import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('Fashion_Retail_Sales.csv')
df.head()

df.info()
df.isnull.sum()

