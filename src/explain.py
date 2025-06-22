import matplotlib.pyplot as plt
import seaborn as sns
from src.gemini import get_gemini_response
import shap
import numpy as np

def explicar_instancias(modelo, X_test, y_test, y_pred):
    print("\n[INFO] Iniciando processo de explicação com Gemini usando SHAP...")

    print("[INFO] Gerando explainer SHAP para o modelo Random Forest...")
    explainer = shap.TreeExplainer(modelo, feature_perturbation="tree_path_dependent")


    print("[INFO] Calculando valores SHAP para o conjunto de teste...")
    shap_values = explainer.shap_values(X_test, check_additivity=False)

    print("[INFO] Identificando instâncias classificadas como ataque...")
    ataque_indices = np.where(y_pred != y_test.mode()[0])[0]
    
    print(f"[INFO] {len(ataque_indices)} instâncias diferentes de 'benigno' encontradas.")

    top_n = 5  # número de features com maior impacto local

    if len(ataque_indices) == 0:
        print("[AVISO] Nenhuma instância de ataque encontrada para explicar.")
        return

    for i in ataque_indices[:2]:  # explica até duas
        print(f"\n[INFO] Explicando instância {i}...")

        instancia = X_test.iloc[[i]]
        atual = y_test.iloc[i]
        previsto = y_pred[i]

        class_index = modelo.classes_.tolist().index(previsto)
        print(f"[DEBUG] Classe prevista: {previsto} (índice interno: {class_index})")

        shap_dict = dict(zip(X_test.columns, shap_values[class_index][i]))
        top_features = sorted(shap_dict.items(), key=lambda x: abs(x[1]), reverse=True)[:top_n]

        feature_lines = [
            f"{feat}: valor observado = {instancia.iloc[0][feat]:.2f}, impacto SHAP = {impact:.4f}"
            for feat, impact in top_features
        ]

        prompt = (
            f"O modelo classificou esta instância como '{previsto}' (rótulo real: '{atual}').\n"
            f"As {top_n} features com maior impacto local foram:\n" +
            "\n".join(feature_lines) +
            "\n\nCom base nesses valores, explique por que esta instância foi classificada dessa forma. "
            "Considere padrões típicos de tráfego de rede."
        )

        print(f"[PROMPT] Enviado para Gemini (instância {i}):\n{prompt}\n")
        resposta = get_gemini_response(prompt)
        print(f"[RESPOSTA] Gemini:\n{resposta}\n")

    print("[INFO] Processo de explicação finalizado.")
