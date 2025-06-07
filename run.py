from app.ETLReader import Reader
from app.ETLTransform import Transform
from app.ETLWriter import Writer
from app.config import *
from app.main import PipelineETL

if __name__ == "__main__":
    caminho_entrada = input_path
    caminho_saida = output_path

    extrator = Reader()
    transformador = Transform()
    loader = Writer()

    pipeline = PipelineETL(extrator, transformador, loader)
    pipeline.executar(caminho_entrada, caminho_saida)

    print("Processo ETL finalizado!")