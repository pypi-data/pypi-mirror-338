import logging
from typing import Optional, Dict, Any, List
from pymongo import MongoClient

def extract_from_mongo(
    client: MongoClient,
    database: str,
    collection: str,
    query_filter: Optional[Dict[str, Any]] = None
) -> List[Dict[str, Any]]:
    """
    Extrai documentos de uma coleção MongoDB e os retorna como lista de dicionários.

    Args:
        client (MongoClient): Instância do MongoClient já conectada.
        database (str): Nome do banco de dados no MongoDB.
        collection (str): Nome da coleção a ser consultada.
        query_filter (dict, optional): Filtro para o find(). Defaults to {}.

    Returns:
        List[Dict[str, Any]]: Lista de documentos retornados pela query.
    """
    
    query_filter = query_filter or {}
    col = client[database][collection]
    
    try:
        logging.info(f"Iniciando extração da coleção '{collection}' do banco '{database}'")
        
        docs = list(col.find(query_filter))
        
        logging.info(f"Extração concluída: {len(docs)} documentos extraídos da coleção '{collection}'.")
        
        return docs
    
    except Exception as e:
        logging.error(f"Erro ao extrair documentos da coleção '{collection}': {e}", exc_info=True)
        raise
    
    
import boto3
import json
import logging
from typing import Any, Dict

def extract_from_secrets(secret_name: str, **kwargs: Any) -> Dict[str, Any]:
    """
    Recupera os segredos do AWS Secrets Manager.

    Args:
        secret_name (str): Nome do segredo a ser recuperado.
        **kwargs: Parâmetros adicionais que podem ser passados para boto3.client,
                  como region_name, endpoint_url, etc.
    Returns:
        dict: Dicionário contendo os segredos.
    Raises:
        Se ocorrer algum erro ao recuperar o segredo.
    """
    client = boto3.client('secretsmanager', **kwargs)
    try:
        response = client.get_secret_value(SecretId=secret_name)
        secret_str = response.get("SecretString")
        secret = json.loads(secret_str)
        logging.info(f" Segredo '{secret_name}' recuperado com sucesso.")
        return secret
    except Exception as e:
        logging.error(f"Erro ao recuperar o segredo '{secret_name}': {e}", exc_info=True)
        raise