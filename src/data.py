import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def carregar_dados(path="content/dataset_balanceado_label.csv"):
    try:
        df = pd.read_csv(path)
        print("Dataset carregado com sucesso!")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
        return None, None, None, None, None
    target_column = df.columns[-1]

    X = df.drop(columns=[target_column])
    y = df[target_column]

    if X.select_dtypes(include=["object", "category"]).shape[1] > 0:
        X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    return df, X_train, X_test, y_train, y_test
