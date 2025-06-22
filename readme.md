# Projeto Gemini XAI - Explicações com Random Forest

Este projeto demonstra como integrar modelos de aprendizado de máquina com a API Gemini da Google para gerar explicações automáticas sobre decisões de classificação, no contexto de segurança de redes.

## 📁 Estrutura do Projeto

```
gemini_xai_project/
│
├── main.py                     # Script principal que executa todo o fluxo
└── src/
    ├── __init__.py             # Torna a pasta src um pacote
    ├── data.py                 # Carregamento e pré-processamento do dataset
    ├── model.py                # Treinamento de modelo Random Forest
    ├── explain.py              # Geração de explicações usando a API Gemini
    └── gemini.py               # Função de integração com a API Gemini
```

## ⚙️ Requisitos

- Python 3.11
- Anaconda 

Instale o ambiente com:

```bash
conda env create -f environment.yml
conda activate gemini_xai_env
```

## 🚀 Execução

Execute o projeto com:

```bash
python main.py
```

Certifique-se de que:
- O arquivo `dataset_balanceado_label.csv` esteja presente no diretório `/content/` (ou ajuste o caminho em `data.py`).
- A chave da API Gemini esteja disponível via `google.colab.userdata.get("GEMINI_API_KEY")` se estiver rodando no Colab, ou edite diretamente em `gemini.py`.

## 🧠 O que este projeto faz?

1. Carrega e limpa um dataset rotulado.
2. Treina um modelo Random Forest.
3. Identifica as principais features de decisão.
4. Usa a API Gemini para explicar classificações de tráfego anômalo.
5. Gera visualizações e relatórios interpretáveis.

## 📌 Observações

- A API Gemini requer uma chave válida da Google Cloud.
- A integração com a Gemini é feita via requisições HTTP (`requests`).
- Gráficos são salvos automaticamente como `.png` no ambiente de execução.

## 📄 Licença

MIT - Utilize e modifique livremente.