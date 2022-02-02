# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# Add description here
#
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# +
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://ploomber.readthedocs.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# + tags=["parameters"]
# extract_upstream=True in your pipeline.yaml file, if this task has
# dependencies, list them them here (e.g. upstream = ['some_task']), otherwise
# leave as None. Once you modify the variable, reload it for Ploomber to inject
# the cell (On JupyterLab: File -> Reload File from Disk)

# extract_product=False in your pipeline.yaml file, leave this as None, the
# value in the YAML spec will be injected in a cell below. If you don't see it,
# check the Jupyter logs


# + tags=["injected-parameters"]
# Parameters
upstream = {
    "get": {
        "nb": "/mnt/products/train/get.ipynb",
        "data": "/mnt/products/train/get.csv",
    },
    "sepal-feature": {
        "nb": "/mnt/products/train/sepal-feature.ipynb",
        "data": "/mnt/products/train/sepal-feature.csv",
    },
    "petal-feature": {
        "nb": "/mnt/products/train/petal-feature.ipynb",
        "data": "/mnt/products/train/petal-feature.csv",
    },
}
product = {
    "nb": "/mnt/products/train/fit.ipynb",
    "model": "/mnt/products/train/model.pickle",
}


# +
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn_evaluation.plot import confusion_matrix

from pathlib import Path
import pickle

raw = pd.read_csv(upstream['get']['data'])
raw.head()
# -

sepal = pd.read_csv(upstream['sepal-feature']['data'])

petal = pd.read_csv(upstream['petal-feature']['data'])

df = raw.join(sepal).join(petal)
df

X = df.drop('target', axis='columns')

y = df.target

model = RandomForestClassifier()
model.fit(X, y)

y_pred = model.predict(X)

confusion_matrix(y, y_pred)

Path(product['model']).write_bytes(pickle.dumps(model))
