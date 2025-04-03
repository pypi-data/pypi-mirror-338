import time
import json
import logging
import pandas as pd
from typing import Dict, List, Callable, Optional

logging.getLogger().handlers.clear()
logging.basicConfig(level=logging.INFO, format='%(message)s')


def cast_to_json(df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Converte as colunas especificadas para JSON string se o valor for dict ou list.
    
    Args:
        df (pd.DataFrame): DataFrame original.
        columns (Optional[List[str]]): Lista de nomes de colunas a transformar.
    
    Returns:
        pd.DataFrame: DataFrame com as colunas transformadas para JSON onde aplicável.
    
    Raises:
        ValueError: Se alguma coluna informada não estiver presente no DataFrame.
    """
    
    missing = [coluna for coluna in columns if coluna not in df.columns]
    if missing:
        raise ValueError(f"As seguintes colunas não estão presentes no DataFrame: {missing}")

    df = df.copy()
    
    for col in columns:
        try:
            df[col] = df[col].apply(lambda x: json.dumps(x, default=str) if isinstance(x, (dict, list)) else x)
        except Exception as e:
            logging.error(f"Erro ao converter coluna '{col}' para JSON: {e}", exc_info=True)
            raise
            
    return df


def strip_and_nullify(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Aplica para as colunas especificadas:
      - Remoção de espaços em branco (strip) se o valor for string.
      - Substituição de strings vazias por pd.NA.
      
    Args:
        df (pd.DataFrame): DataFrame de entrada.
        columns (List[str]): Lista de nomes de colunas a serem transformadas.
    
    Returns:
        pd.DataFrame: DataFrame com as colunas transformadas.
    
    Raises:
        ValueError: Se alguma coluna informada não estiver presente no DataFrame.
    """
    missing = [coluna for coluna in columns if coluna not in df.columns]
    if missing:
        raise ValueError(f"As seguintes colunas não estão presentes no DataFrame: {missing}")

    df = df.copy()
    for col in columns:
        try:
            df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x).replace("", pd.NA)
        except Exception as e:
            logging.error(f"Erro ao aplicar strip e nullify na coluna '{col}': {e}", exc_info=True)
            raise
    return df


def convert_to_string(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Converte as colunas especificadas para o tipo 'string' do pandas.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada.
        columns (List[str]): Lista de nomes de colunas a serem convertidas.
    
    Returns:
        pd.DataFrame: DataFrame com as colunas convertidas para o tipo 'string'.
    
    Raises:
        ValueError: Se alguma coluna informada não estiver presente no DataFrame.
    """
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"As seguintes colunas não estão presentes no DataFrame: {missing}")

    df = df.copy()
    for col in columns:
        try:
            df[col] = df[col].astype("string")
        except Exception as e:
            logging.error(f"Erro ao converter a coluna '{col}' para string: {e}", exc_info=True)
            raise
    return df


def apply_transformations(df: pd.DataFrame, config: Dict[str, List[Callable[[pd.DataFrame, List[str]], pd.DataFrame]]]) -> pd.DataFrame:
    """
    Para cada coluna definida na configuração, aplica as funções listadas (na ordem definida).
    
    Args:
        df (pd.DataFrame): DataFrame a ser transformado.
        config (Dict[str, List[Callable]]): Dicionário onde as chaves são nomes de colunas
                                              e os valores são listas de funções de transformação.
    Returns:
        pd.DataFrame: DataFrame transformado.
    """
    df = df.copy()
    for col, funcs in config.items():
        if col not in df.columns:
            raise ValueError(f"A coluna '{col}' não está presente no DataFrame.")
        for func in funcs:
            start_time = time.perf_counter()
            try:
                df = func(df, [col])
                elapsed = time.perf_counter() - start_time
                logging.info(f"|'{col}'|: {func.__name__}............ [PASS in {elapsed:.2f}s]")
            except Exception as e:
                elapsed = time.perf_counter() - start_time
                logging.error(f"|'{col}'|: {func.__name__}............ [FAIL in {elapsed:.2f}s] - Erro: {e}", exc_info=True)
                raise
    return df