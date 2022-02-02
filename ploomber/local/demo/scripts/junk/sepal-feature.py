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


# + tags=["injected-parameters"]
# Parameters
upstream = {
    "get": {
        "nb": "/mnt/products/train/get.ipynb",
        "data": "/mnt/products/train/get.csv",
    }
}
product = {
    "nb": "/mnt/products/train/sepal-feature.ipynb",
    "data": "/mnt/products/train/sepal-feature.csv",
}

# -

import pandas as pd
df = pd.read_csv(upstream['get']['data'])
df.head()

df['sepal-feature'] = df['sepal length (cm)'] * df['sepal width (cm)']

df[['sepal-feature']].to_csv(product['data'], index = False)
