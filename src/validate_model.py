"""
Создайте скрипт для проверки качества модели:
- Читает модель и данные
- Получает accuracy (пересчитывает или читает из `metrics/metrics.json`)
- Сравнивает с порогом `accuracy_min` из `params.yaml`
- Завершается с кодом != 0 при `accuracy < accuracy_min`

"""

import json
import pickle

import pandas as pd
import yaml
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def load_model():
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)
        return model


def load_params():
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def read_data():
    df = pd.read_csv("data\processed\dataset.csv")
    return df


def get_accuracy():
    with open("metrics/metrics.json", "r") as f:
        metrics_arr = json.load(f)

    if metrics_arr:
        accuracy = metrics_arr[-1]["accuracy"]
        return accuracy
    else:
        params = load_params()
        model = load_model()
        df = read_data()

        X = df[["total_bill", "size"]]
        y = df["high_tip"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=params["test_size"], random_state=params["seed"]
        )

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        metrics_arr.append({"accuracy": accuracy, "rows": len(df)})
        with open("metrics/metrics.json", "w") as f:
            json.dump(metrics_arr, f)


def compare_accuracy():
    params = load_params()
    accuracy_min = params["accuracy_min"]
    accuracy_now = get_accuracy()

    if accuracy_now is None:
        print()
        print("Accuracy is not found")
        print()
        exit(1)

    elif accuracy_now <= accuracy_min:
        print()
        print(f"Accuracy {accuracy_now:.3f} <= Accuracy_min {accuracy_min}")
        print()
        exit(1)

    else:
        print()
        print(f"Accuracy {accuracy_now:.3f} > Accuracy_min {accuracy_min}")
        print()
        exit(0)


compare_accuracy()
