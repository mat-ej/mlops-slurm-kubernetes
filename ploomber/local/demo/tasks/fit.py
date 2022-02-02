import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn_evaluation.plot import confusion_matrix

from pathlib import Path
import pickle

import atexit
import pickle
import importlib
from unittest.mock import Mock

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn_evaluation import plot
from mlflow.exceptions import MlflowException


def fit(upstream, product, model, n_estimators, criterion, track, mlflow_tracking_uri):

    #dunno why
    import mlflow

    module, _, class_name = model.rpartition('.')
    Class_ = getattr(importlib.import_module(module), class_name)
    print(Class_)

    if track:
        print('tracking with mlflow...')
        mlflow.set_tracking_uri(mlflow_tracking_uri)

        @atexit.register
        def end_run():
            mlflow.end_run()
    else:
        print('tracking skipped...')
        mlflow = Mock()

    try:
        experiment_id = mlflow.create_experiment(name=class_name)
    except MlflowException:
        experiment_id = mlflow.get_experiment_by_name(name=class_name).experiment_id

    print(f'experiment id: {experiment_id}')
    # -


    clf = Class_(n_estimators=n_estimators, criterion=criterion)



    run = mlflow.start_run(experiment_id=experiment_id)
    print(run.info.run_id)

    df = pd.read_csv(upstream['features'])
    X = df.drop('target', axis='columns')
    y = df.target
    #
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.33,
                                                        random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)

    fig, ax = plt.subplots()
    plot.confusion_matrix(y_test, y_pred, ax=ax)

    mlflow.log_params(clf.get_params())
    mlflow.log_metric('accuracy', report['accuracy'])
    mlflow.log_figure(fig, 'cf.png')
    mlflow.sklearn.log_model(clf, artifact_path="sklearn-model")

    print(report)

    return pickle.dumps(clf)
    #
    # # + tags=["model-training"]
    # clf = Class_(**model_params)
    # clf.fit(X_train, y_train)


    # df.to_csv(product, index=False)

    # print(model)
    # print(args)

    # if track:
    #     print('tracking with mlflow...')
    #     mlflow.set_tracking_uri(mlflow_tracking_uri)
    #
    #     @atexit.register
    #     def end_run():
    #         mlflow.end_run()
    # else:
    #     print('tracking skipped...')
    #     mlflow = Mock()
    #
    # module, _, class_name = model.rpartition('.')
    # Class_ = getattr(importlib.import_module(module), class_name)
    # Class_
    #
    # # +
    # try:
    #     experiment_id = mlflow.create_experiment(name=class_name)
    # except MlflowException:
    #     experiment_id = mlflow.get_experiment_by_name(name=class_name).experiment_id
    #
    # print(f'experiment id: {experiment_id}')
    #
    # run = mlflow.start_run(experiment_id=experiment_id)
    #
    # print(run.info.run_id)
    #
    # print('some important information that I want to see on MLflow for debugging...')
    #
    # df = pd.read_csv(str(upstream['features']))
    # X = df.drop('target', axis='columns')
    # y = df.target
    #
    # X_train, X_test, y_train, y_test = train_test_split(X,
    #                                                     y,
    #                                                     test_size=0.33,
    #                                                     random_state=42)
    #
    # # + tags=["model-training"]
    # clf = Class_(**model_params)
    # clf.fit(X_train, y_train)
    #
    #
    # # df = pd.read_csv(upstream['features'])
    # #
    # # X = df.drop('target', axis='columns')
    # # y = df.target
    # #
    # # model = RandomForestClassifier()
    # # model.fit(X, y)
    # #
    # # y_pred = model.predict(X)
    # #
    # # confusion_matrix(y, y_pred)
    #
    # Path(product['model']).write_bytes(pickle.dumps(clf))