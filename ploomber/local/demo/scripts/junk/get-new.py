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
upstream = None

# extract_product=False in your pipeline.yaml file, leave this as None, the
# value in the YAML spec will be injected in a cell below. If you don't see it,
# check the Jupyter logs
product = None


# + tags=["injected-parameters"]
# Parameters
product = {
    "nb": "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/products/serve/get-new.ipynb",
    "data": "/home/m/repo/mlops-slurm-kubernetes/ploomber/local/demo/products/serve/get-new.csv",
}

# -

from sklearn.datasets import load_iris
df = load_iris(as_frame=True)['data']
df

df.to_csv(product['data'], index=False)
