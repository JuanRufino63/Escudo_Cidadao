"""Aplicação demonstrativa para a Global Solution: não acessa URLs."""
from pathlib import Path
import joblib
import streamlit as st
from atributos import extrair_atributos, VARIAVEIS

st.set_page_config(page_title="Escudo Cidadão", page_icon="🛡️", layout="centered")
st.title("🛡️ Escudo Cidadão")
st.subheader("Análise educativa de URLs suspeitas")
st.write(
    "Informe um link para comparar dois modelos de Machine Learning: "
    "um treinado com HTTPS e outro sem HTTPS. O sistema analisa **apenas o texto**, sem abrir o endereço."
)

PASTA_MODELOS = Path(__file__).resolve().parents[1] / "ml" / "modelos"

@st.cache_resource
def carregar_modelos():
    return {
        "Com HTTPS": joblib.load(PASTA_MODELOS / "random_forest_com_https.joblib"),
        "Sem HTTPS": joblib.load(PASTA_MODELOS / "random_forest_sem_https.joblib"),
    }

texto = st.text_input("Cole a URL", placeholder="https://exemplo.com/login")

if st.button("Analisar link", type="primary"):
    url = texto.strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        st.warning("Digite uma URL completa começando com http:// ou https://.")
    elif len(url) > 2048:
        st.warning("O link é muito longo para esta demonstração (máximo de 2048 caracteres).")
    else:
        try:
            modelos = carregar_modelos()
            atributos = extrair_atributos(url)
            for nome, modelo in modelos.items():
                colunas = VARIAVEIS if nome == "Com HTTPS" else [
                    item for item in VARIAVEIS if item != "usa_https"
                ]
                predicao = int(modelo.predict(atributos[colunas])[0])
                indice_phishing = list(modelo.classes_).index(1)
                pontuacao = float(modelo.predict_proba(atributos[colunas])[0][indice_phishing])
                st.markdown(f"#### {nome}")
                st.metric("Classificação", "Padrão suspeito" if predicao == 1 else "Padrão semelhante a links legítimos")
                st.progress(pontuacao, text=f"Pontuação do modelo para phishing: {pontuacao:.1%}")
            st.caption(
                "As pontuações do classificador não são probabilidades calibradas de um golpe. "
                "Esta demonstração não inspeciona o site, não consulta listas de bloqueio "
                "e pode errar em links novos."
            )
        except FileNotFoundError:
            st.error("Modelos não encontrados. Execute primeiro o notebook na pasta ml/.")

st.divider()
st.info(
    "HTTPS cifra a conexão, mas não garante que o site seja confiável. "
    "Nunca forneça senhas ou dados bancários apenas porque o classificador indicou baixo risco."
)
st.caption("Projeto acadêmico • FIAP Global Solution 2026.2 • PhiUSIIL / UCI")
