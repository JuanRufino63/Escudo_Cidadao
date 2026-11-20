"""Atributos lexicais usados nos dois experimentos do notebook."""
import pandas as pd

VARIAVEIS = [
    "tamanho_url", "qtd_digitos", "qtd_pontos", "qtd_hifens",
    "qtd_barras", "qtd_especiais", "usa_https", "palavra_suspeita"
]

def extrair_atributos(texto_url):
    """Analisa apenas o texto da URL; não realiza requisições de rede."""
    url = pd.Series([texto_url.strip()])
    dados = pd.DataFrame()
    dados["tamanho_url"] = url.str.len()
    dados["qtd_digitos"] = url.str.count(r"\d")
    dados["qtd_pontos"] = url.str.count(r"\.")
    dados["qtd_hifens"] = url.str.count("-")
    dados["qtd_barras"] = url.str.count("/")
    dados["qtd_especiais"] = url.str.count(r"[@?=&%]")
    dados["usa_https"] = url.str.startswith("https://").astype(int)
    dados["palavra_suspeita"] = url.str.contains(
        r"login|verify|account|secure|update|confirm", case=False, regex=True
    ).astype(int)
    return dados[VARIAVEIS]
