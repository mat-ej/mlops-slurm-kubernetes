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
upstream = ['get', 'petal-feature', 'sepal-feature']

# extract_product=False in your pipeline.yaml file, leave this as None, the
# value in the YAML spec will be injected in a cell below. If you don't see it,
# check the Jupyter logs
product = None

model = None

# + tags=["injected-parameters"]
# Parameters
model = "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/model.pickle"

upstream = {
    "sepal-feature": {
        "nb": "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/products/serve/sepal-feature.ipynb",
        "data": "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/products/serve/sepal-feature.csv",
    },
    "get": {
        "nb": "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/products/serve/get-new.ipynb",
        "data": "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/products/serve/get-new.csv",
    },
    "petal-feature": {
        "nb": "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/products/serve/petal-feature.ipynb",
        "data": "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/products/serve/petal-feature.csv",
    },
}
product = {
    "nb": "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/products/serve/predict.ipynb",
    "data": "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/products/serve/predict.csv",
}


# +
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn_evaluation.plot import confusion_matrix

from pathlib import Path
import pickle

raw = pd.read_csv(upstream['get']['data'])

sepal = pd.read_csv(upstream['sepal-feature']['data'])

petal = pd.read_csv(upstream['petal-feature']['data'])

df = raw.join(sepal).join(petal)

print(df.head())

model_ = pickle.loads(Path(model).read_bytes())
print(model_)

preds = model_.predict(df)

out = pd.DataFrame({"y_pred": preds})
print(out)



out.to_csv(product['data'], index = False)
# your code here...
