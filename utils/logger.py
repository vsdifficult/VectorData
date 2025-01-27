import logging

def setup_logger():
    logger = logging.getLogger('VectorDB')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('vector_db.log')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()