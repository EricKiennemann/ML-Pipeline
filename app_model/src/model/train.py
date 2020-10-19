import os
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts, set_tracking_uri

if __name__ == "__main__":
    set_tracking_uri('file:/mlflow_data/log')
    # Log a parameter (key-value pair)
    print("coucou")
    log_param("param1", randint(0, 100))

    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", random())
    log_metric("foo", random() + 1)
    log_metric("foo", random() + 2)

    # Log an artifact (output file)
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")
    log_artifacts("outputs")
