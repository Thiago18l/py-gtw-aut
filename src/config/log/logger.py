import logging
import logging.config as conf

__log_levels__ = {
    "CRITICAL": 50,
    "ERROR": 40,
    "WARNING": 30,
    "INFO": 20,
    "DEBUG": 10,
}


def logger(level=__log_levels__["DEBUG"], module=__name__):
    conf.fileConfig(fname="log.ini", disable_existing_loggers=False)
    logger = logging.getLogger(module)
    logger.setLevel(level)
    return logger
