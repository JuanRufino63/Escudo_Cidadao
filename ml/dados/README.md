# Origem dos dados — Escudo Cidadão

- **Fonte:** *PhiUSIIL Phishing URL Dataset*, UCI Machine Learning Repository, dataset 967.
- **URL:** https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset
- **Publicação no repositório:** 2024. **Período de coleta das URLs:** não identificado de forma inequívoca no CSV utilizado; não atribuímos datas aos registros.
- **Licença informada pela UCI:** CC BY 4.0, com atribuição à fonte/autores.
- **Arquivo original:** `phiusiil+phishing+url+dataset.zip` (contém `PhiUSIIL_Phishing_URL_Dataset.csv`).
- **Volume original:** 235.795 linhas, 56 colunas. Limpeza remove 425 URLs duplicadas; restam 235.370.
- **Classes originais:** `label=0` é phishing; `label=1` é legítimo. No notebook, `phishing=1` é phishing.
- **Variáveis utilizadas:** apenas texto da coluna `URL`, para gerar 8 atributos lexicais, e `label` para o alvo. As outras colunas não entram no modelo.
- **Tratamento:** remoção de registros sem URL/rótulo e duplicatas por URL; divisão estratificada treino/teste 80%/20%.
- **Acesso a links:** nenhum endereço contido no arquivo é visitado.

> **Ressalva explícita da GS:** a base é pública e real, mas não é específica de uma cidade brasileira. A adequação territorial exigida no edital **permanece pendente por decisão de escopo**.

## Baixar o dataset (caso não esteja neste projeto)

Acesse a URL da UCI e coloque o arquivo ZIP original nesta pasta, preservando o nome. No Colab, execute a célula de upload do notebook se ele não localizar o arquivo.
