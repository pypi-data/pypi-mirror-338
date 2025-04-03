import awswrangler as wr
import logging
import pandas as pd
from typing import Optional, List

def load_to_s3_parquet(path: str, df: pd.DataFrame, partition_cols: Optional[List[str]] = None, **kwargs) -> list:
    """
    Salva um DataFrame como arquivo Parquet no S3 usando AWS Wrangler.

    Args:
        path (str): Caminho do bucket S3 onde o arquivo Parquet será salvo.
        df (pd.DataFrame): DataFrame a ser salvo.
        partition_cols (Optional[List[str]]): Lista de colunas para particionamento.
        **kwargs: Parâmetros adicionais que serão repassados para wr.s3.to_parquet.
                  (Ex.: mode, database, table, compression, etc.)

    Returns:
        list: Lista de caminhos dos arquivos Parquet salvos.

    Raises:
        RuntimeError: Se ocorrer algum erro ao salvar o DataFrame.
    """
    try:
        response = wr.s3.to_parquet(
            df=df,
            path=path,
            partition_cols=partition_cols,
            dataset=True,
            **kwargs
        )
        logging.info(f"{len(df)} linhas salvas com sucesso em {path}.")
        return response.get("paths", [])
    except Exception as e:
        logging.error(f"Erro ao salvar o DataFrame no S3: {e}", exc_info=True)
        raise