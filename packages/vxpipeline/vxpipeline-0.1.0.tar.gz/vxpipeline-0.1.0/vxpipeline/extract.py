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