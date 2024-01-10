import logging

class CustomFormatter(logging.Formatter):
    '''Formato personalizado para añadir emojis al log level'''

    # Definimos los emojis para cada log level
    EMOJIS = {
        logging.DEBUG: "🐛",
        logging.INFO: "🌐",
        logging.WARNING: "🚨",
        logging.ERROR: "❌",
        logging.CRITICAL: "🚫"
    }

    def format(self, record):
        # Modifica el mensaje para incluir el emoticono según el nivel de log
        record.msg = f"{self.EMOJIS.get(record.levelno, '')} {record.msg}"
        return super().format(record)

def configure_logger(logging_level):
    # Configurar el logger
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = CustomFormatter('[%(asctime)s, %(lineno)d] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Ajustar el nivel del logger
    if logging_level == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    elif logging_level == 'INFO':
        logger.setLevel(logging.INFO)
    elif logging_level == 'WARNING':
        logger.setLevel(logging.WARNING)
    elif logging_level == 'ERROR':
        logger.setLevel(logging.ERROR)
    elif logging_level == 'CRITICAL':
        logger.setLevel(logging.CRITICAL)

    # Detener la propagación de los loggers anteriores
    logger.propagate = False

    return logger

# from your_logger_module import configure_logger
# logger = configure_logger('DEBUG')
# logger.info('This is an info message')
