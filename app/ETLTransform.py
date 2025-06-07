class Transform:
    def transformar(self, df):
        print("Transformando os dados...")
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].str.upper()
        return df