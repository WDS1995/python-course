import pandas as pd

class Reader:
    def extrair(self, caminho_csv):
        print("Extraindo dados do CSV...")
        df = pd.read_csv(caminho_csv)
        return df