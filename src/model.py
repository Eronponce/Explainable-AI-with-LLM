from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def treinar_modelo(X_train, y_train, X_test, y_test):
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)

    feature_importances = pd.Series(modelo.feature_importances_, index=X_train.columns).sort_values(ascending=False)
    return modelo, y_pred, feature_importances
