class Writer:
    def carregar(self, df, caminho_saida):
        print("Salvando como parquet (snappy)...")
        df.to_parquet(caminho_saida, compression='snappy', index=False)