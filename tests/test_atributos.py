import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "web"))
from atributos import extrair_atributos

class TestAtributos(unittest.TestCase):
    def test_https(self):
        x = extrair_atributos("https://exemplo.com/login")
        self.assertEqual(x.loc[0, "usa_https"], 1)
        self.assertEqual(x.loc[0, "palavra_suspeita"], 1)
        self.assertEqual(x.loc[0, "qtd_pontos"], 1)

    def test_sem_https(self):
        x = extrair_atributos("http://abc123.com")
        self.assertEqual(x.loc[0, "usa_https"], 0)
        self.assertEqual(x.loc[0, "qtd_digitos"], 3)

if __name__ == "__main__":
    unittest.main()
