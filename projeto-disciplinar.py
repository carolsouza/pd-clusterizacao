#%%
##IMPORTS
import kagglehub
import os
import pandas as pd 

# %%
# DOWNLOAD DO KAGGLE
# Set kagglehub cache to local datasets folder
os.environ['KAGGLEHUB_CACHE'] = os.path.abspath('./datasets')

# Download latest version
path = kagglehub.dataset_download("rohan0301/unsupervised-learning-on-country-data")
print("Path to dataset files:", path)


# %%
# Lendo o dataset
df = pd.read_csv(path + '/Country-data.csv')
print(df['country'].nunique())

#%%
