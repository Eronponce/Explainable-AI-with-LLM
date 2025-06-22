from src.model import treinar_modelo
from src.data import carregar_dados
from src.explain import explicar_instancias
from src.gemini import get_gemini_response

def main():
    df, X_train, X_test, y_train, y_test = carregar_dados()
    modelo, y_pred, feature_importances = treinar_modelo(X_train, y_train, X_test, y_test)
    explicar_instancias(modelo, X_test, y_test, y_pred)

if __name__ == "__main__":
    main()
