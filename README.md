# 🛡️ Escudo Cidadão — Global Solution FIAP 2026.2

**Pergunta:** quanto a variável HTTPS influencia a classificação de URLs de phishing?

Este projeto apresenta dois classificadores Random Forest treinados com URLs públicas: um com **8 atributos**, incluindo HTTPS, e outro com **7 atributos**, sem HTTPS. Os resultados são apresentados em um notebook acadêmico e em uma interface educativa feita com Streamlit.

## Vídeo de demonstração

[Assista à apresentação do Escudo Cidadão no YouTube](https://www.youtube.com/watch?v=SFd9hyRrtdI).

## Como executar

**Requisitos:** Python 3.11 ou superior, preferencialmente em ambiente virtual.

```bash
pip install -r ml/requirements.txt
```

**Notebook:** acesse a pasta `ml/` e abra `notebook_escudo_cidadao.ipynb` no Jupyter. O dataset ZIP está em `ml/dados/` no pacote completo. Alternativamente, envie o arquivo no Google Colab.

```bash
cd ml
jupyter notebook notebook_escudo_cidadao.ipynb
```

**Aplicação:** abra outro terminal na pasta raiz do repositório e execute:

```bash
streamlit run web/app.py
```

**Testes dos atributos:**

```bash
python -m unittest discover -s tests -v
```

Os modelos já treinados estão em `ml/modelos/`. **O dataset ZIP original não está versionado neste repositório**: baixe-o da [UCI](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset) e salve como `ml/dados/phiusiil+phishing+url+dataset.zip` antes de executar o notebook. Há instruções adicionais em [`ml/dados/README.md`](ml/dados/README.md). O notebook também permite upload manual no Google Colab. Ao executá-lo, os arquivos `.joblib` e as tabelas poderão ser regenerados.

## Principais resultados no conjunto de teste

| Modelo | Acurácia | Precisão phishing | Recall phishing | F1 phishing |
|---|---:|---:|---:|---:|
| Com HTTPS | 99,59% | 99,93% | 99,10% | 99,52% |
| Sem HTTPS | 86,27% | 97,29% | 69,79% | 81,27% |

Foram avaliadas **12 combinações de 3 hiperparâmetros para cada modelo**, com validação cruzada estratificada de 3 partes somente no treino. A busca utilizou 25 mil registros extraídos exclusivamente do treino; cada modelo final foi ajustado em todos os 188.296 registros de treinamento e avaliado uma única vez nos 47.074 registros do teste.

## Estrutura

```text
escudo_cidadao_gs/
├── README.md
├── ml/
│   ├── notebook_escudo_cidadao.ipynb  # executado, com gráficos
│   ├── RELATORIO_ML.md
│   ├── RELATORIO_ML.pdf  # versão no GitHub ainda precisa ser substituída
│   ├── ANEXO_GRAFICOS.md
│   ├── figuras/             # 8 gráficos documentados
│   ├── requirements.txt
│   ├── dados/README.md
│   ├── dados/phiusiil+phishing+url+dataset.zip  # baixar manualmente (não versionado)
│   └── modelos/                      # 2 modelos e métricas
├── web/
│   ├── app.py                       # interface Streamlit
│   └── atributos.py                 # 8 atributos iguais aos do notebook
├── tests/test_atributos.py
└── docs/ROTEIRO_VIDEO.md
```

## Limites e uso responsável

- **HTTPS não significa URL segura**. Na base, 48.885 das URLs de phishing, após deduplicação, também começam com `https://`.
- A previsão da aplicação **não é certificação** de segurança, não checa o conteúdo ou reputação de sites e não substitui orientação especializada.
- Os resultados são específicos desta base e desta divisão aleatória; sites novos e outras fontes podem apresentar distribuição diferente.
- O projeto não coleta dados de usuários e **não realiza requisições** aos links informados; apenas lê o texto digitado.
- **Escopo dos dados:** o trabalho utiliza a base pública PhiUSIIL, aprovada pelo professor conforme orientação recebida pela equipe; os registros não têm recorte municipal. Outros componentes de disciplinas são entregas independentes.

## Autoria e referências

Trabalho acadêmico desenvolvido para a Global Solution FIAP 2026.2. Integrantes:

| Integrante | RM |
|---|---:|
| Heloísa Fleury Jardim | 556378 |
| Juan Fuentes Rufino | 557673 |
| Rickelmyn de Souza Ruescas | 556055 |
| Paulo Henrique Monteiro Golovanevsky | 555300 |
| Pedro Henrique Silva Batista | 558137 |

O relatório principal está em [`ml/RELATORIO_ML.md`](ml/RELATORIO_ML.md) e a coleção completa de gráficos em [`ml/ANEXO_GRAFICOS.md`](ml/ANEXO_GRAFICOS.md). **O relatório Markdown já utiliza os RMs corrigidos. O PDF do repositório ainda precisa ser substituído pela versão corrigida.**

Dataset: *PhiUSIIL Phishing URL Dataset*, UCI Machine Learning Repository (2024), https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset. Licença: CC BY 4.0.
