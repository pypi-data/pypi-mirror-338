import logging
from pymongo import MongoClient
from contextlib import contextmanager

@contextmanager
def mongodb_connect(conn_string: str, **kwargs):
    """Gerenciador de contexto para conexão MongoDB flexível.

    Args:
        conn_string (str): String de conexão do MongoDB.
        **kwargs: Parâmetros opcionais para o MongoClient.

    Yield:
        MongoClient: Conexão ativa com o MongoDB.
    """

    try:
        logging.info("Creating MongoDB connection")
        conn = MongoClient(conn_string, **kwargs)
        yield conn
    except Exception as e:
        logging.error(f"Database connection error: {e}", exc_info=True)
        raise
    finally:
        if conn:
            logging.info("Closing MongoDB connection")
            conn.close()