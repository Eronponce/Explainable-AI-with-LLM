# Projeto Gemini XAI - Explicações com Random Forest

Este projeto demonstra como integrar modelos de aprendizado de máquina com a API Gemini da Google para gerar explicações automáticas sobre decisões de classificação, no contexto de segurança de redes.

## 📁 Estrutura do Projeto

```
gemini_xai_project/
│
├── main.py                     # Script principal que executa todo o fluxo
└── src/
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

##Exemplos de resposta

### Identificação correta do modelo
<details>
<summary>Clique para expandir</summary>
[INFO] Explicando instância 1...  
[DEBUG] Classe prevista: Benign (índice interno: 0)  
[PROMPT] Enviado para Gemini (instância 1):

> O modelo classificou esta instância como **'Benign'** (rótulo real: **'Benign'**).  
> As 5 features com maior impacto local foram:
> - **Header_Length**: valor observado = 50.00, impacto SHAP = -0.0011  
> - **Time_To_Live**: valor observado = 81.70, impacto SHAP = 0.0007  
> - **Rate**: valor observado = 13870.05, impacto SHAP = 0.0002  
> - **Protocol Type**: valor observado = 6.00, impacto SHAP = 0.0002  
>
> Com base nesses valores, explique por que esta instância foi classificada dessa forma. Considere padrões típicos de tráfego de rede.

---
### [RESPOSTA] Gemini:

A instância foi classificada como **'Benign'** (benigna) e, analisando as features com maior impacto local, temos:

- **Header_Length: 50.00, SHAP = -0.0011**  
  Um comprimento de cabeçalho relativamente alto pode indicar conformidade com padrões de rede. Cabeçalhos de tráfego malicioso tendem a ser anômalos ou otimizados para entrega rápida de carga maliciosa. Aqui, o valor sugere tráfego típico e contribui para a classificação benigna.

- **Time_To_Live: 81.70, SHAP = 0.0007**  
  TTL alto pode indicar que o pacote percorreu uma distância razoável, o que é comum em tráfego legítimo. Malwares locais podem usar TTLs baixos para agir rapidamente. O impacto é positivo, embora pequeno.

- **Rate: 13870.05, SHAP = 0.0002**  
  Uma taxa de transmissão moderada pode indicar tráfego normal. Embora taxas muito altas possam sugerir DoS, esse valor parece dentro de uma faixa esperada, contribuindo ligeiramente para a classificação benigna.

- **Protocol Type: 6.00, SHAP = 0.0002**  
  O valor 6 geralmente representa o protocolo TCP, amplamente usado em comunicações legítimas. O uso do TCP reforça a percepção de tráfego benigno, já que protocolos incomuns podem estar ligados a atividades suspeitas.

---

### **Resumo: por que foi classificado como Benign?**

A combinação dos seguintes fatores resultou na classificação como **'Benign'**:
1. **Formato padrão:** Header_Length e Protocol Type estão de acordo com padrões de rede típicos.
2. **Comportamento de tráfego normal:** TTL e Rate não indicam anomalias.
3. **Impactos SHAP baixos, mas consistentes:** Todos os impactos apontam na direção de tráfego legítimo.

---

### **Considerações adicionais**

- **Normalização:** Os valores exibidos podem ter sido normalizados. Interpretações devem levar isso em conta.
- **Contexto:** A avaliação depende do tipo de rede, aplicação e hora do dia. O que é "normal" em uma rede pode não ser em outra.
- **Limitado às 5 features:** O modelo pode estar considerando outras variáveis que não foram listadas aqui.
- **Falsos negativos existem:** Uma classificação como 'Benign' não significa que a instância seja definitivamente segura. Monitoramento contínuo é essencial.

---

[INFO] Processo de explicação finalizado.
</details>

### Identificação errada do modelo
<details>
<summary>Clique para expandir</summary>
[INFO] Explicando instância 8...  
[DEBUG] Classe prevista: Reconnaissance (índice interno: 2)  
[PROMPT] Enviado para Gemini (instância 8):

> O modelo classificou esta instância como **'Reconnaissance'** (rótulo real: **'Benign'**).  
> As 5 features com maior impacto local foram:
> - **Protocol Type**: valor observado = 6.00, impacto SHAP = 0.0578  
> - **Time_To_Live**: valor observado = 77.50, impacto SHAP = -0.0248  
> - **Header_Length**: valor observado = 27.20, impacto SHAP = -0.0218  
> - **Rate**: valor observado = 220.12, impacto SHAP = -0.0112  
>
> Com base nesses valores, explique por que esta instância foi classificada dessa forma. Considere padrões típicos de tráfego de rede.

---

### [RESPOSTA] Gemini:

A classificação incorreta desta instância como **'Reconnaissance'** (quando o rótulo real é **'Benign'**) parece ser um falso positivo impulsionado principalmente pelo valor da feature `Protocol Type`. Vamos analisar:

- **Protocol Type: valor observado = 6.00, impacto SHAP = 0.0578**  
  Este é o principal fator que contribuiu para a classificação como 'Reconnaissance'. Um valor de 6 pode representar um protocolo raramente usado ou associado a atividades suspeitas. O impacto SHAP positivo indica que aumentou a probabilidade dessa classe.

- **Time_To_Live: valor observado = 77.50, impacto SHAP = -0.0248**  
  TTL nessa faixa teve impacto negativo, reduzindo a chance de ser classificado como 'Reconnaissance'. Pode indicar um comportamento típico de tráfego benigno.

- **Header_Length: valor observado = 27.20, impacto SHAP = -0.0218**  
  Também teve impacto negativo. Pode estar dentro do padrão de tráfego legítimo, contribuindo para afastar a hipótese de ataque.

- **Rate: valor observado = 220.12, impacto SHAP = -0.0112**  
  Uma taxa aparentemente normal de tráfego, também com pequeno impacto negativo.

---

### **Resumo: por que o modelo errou?**

1. **O valor de `Protocol Type` (6.00) teve peso dominante**, superando os impactos negativos das demais features.
2. **Falta de contexto:** O modelo pode não ter acesso a informações adicionais que ajudem a diferenciar tráfego benigno de malicioso.
3. **Desbalanceamento de classes:** Se 'Reconnaissance' for pouco representada no treino, o modelo pode tender a classificações conservadoras para evitar falsos negativos.

---

### **Soluções ou direções possíveis:**

- **Investigar `Protocol Type = 6`:** Descobrir qual protocolo está representado e por que é associado a ataques.
- **Rebalancear o dataset:** Usar oversampling ou undersampling para melhorar a representação das classes.
- **Engenharia de features:** Incorporar contexto (sessão, aplicação, usuário) para enriquecer a entrada do modelo.
- **Revisar o treinamento:** Verificar qualidade dos rótulos e variedade de amostras da classe 'Reconnaissance'.
- **Ajustar limiares de decisão:** Alterar o threshold pode reduzir falsos positivos, com impacto nos falsos negativos.

---

[INFO] Processo de explicação finalizado.
</details>

## 📄 Licença

MIT - Utilize e modifique livremente.
