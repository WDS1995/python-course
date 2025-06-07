class PipelineETL:
    def __init__(self, reader, transform, writer):
        self.extrator = reader
        self.transformador = transform
        self.loader = writer

    def executar(self, caminho_csv, caminho_parquet):
        df = self.extrator.extrair(caminho_csv)
        df = self.transformador.transformar(df)
        self.loader.carregar(df, caminho_parquet)