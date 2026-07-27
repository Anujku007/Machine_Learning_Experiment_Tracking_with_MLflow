# The data set used in this example is from http://archive.ics.uci.edu/ml/datasets/Wine+Quality

import warnings
import sys
import logging
from urllib.parse import urlparse

import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # -----------------------------
    # Set MLflow Tracking URI FIRST
    # -----------------------------
    remote_server_uri = "https://dagshub.com/Anujku007/mlflowexperiments.mlflow"
    mlflow.set_tracking_uri(remote_server_uri)

    # Read dataset
    csv_url = (
        "https://raw.githubusercontent.com/mlflow/mlflow/master/tests/datasets/winequality-red.csv"
    )

    try:
        data = pd.read_csv(csv_url, sep=";")
    except Exception as e:
        logger.exception(
            "Unable to download dataset. Error: %s", e
        )
        sys.exit(1)

    # Train-test split
    train, test = train_test_split(data, random_state=42)

    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)

    train_y = train["quality"]
    test_y = test["quality"]

    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

    # Start MLflow Run
    with mlflow.start_run():

        lr = ElasticNet(
            alpha=alpha,
            l1_ratio=l1_ratio,
            random_state=42
        )

        lr.fit(train_x, train_y)

        predicted_qualities = lr.predict(test_x)

        rmse, mae, r2 = eval_metrics(test_y, predicted_qualities)

        print(f"ElasticNet model (alpha={alpha}, l1_ratio={l1_ratio})")
        print(f"RMSE : {rmse}")
        print(f"MAE  : {mae}")
        print(f"R2   : {r2}")

        # Log Parameters
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)

        # Log Metrics
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        tracking_url_type_store = urlparse(
            mlflow.get_tracking_uri()
        ).scheme

        # Register model if remote store
        if tracking_url_type_store != "file":
            mlflow.sklearn.log_model(
                sk_model=lr,
                artifact_path="model",
                registered_model_name="ElasticnetWineModel",
            )
        else:
            mlflow.sklearn.log_model(
                sk_model=lr,
                artifact_path="model",
            )

    print("MLflow run completed successfully.")