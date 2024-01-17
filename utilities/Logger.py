import logging


logger = logging.getLogger(__name__)

logger.addHandler()

filehandler = logging.FileHandler('logfile.log')

logger.addHandler(filehandler)


logger.debug("This is debug")
logger.info("This is debug")
logger.warning("This is debug")
logger.error("This is debug")
logger.critical("This is debug")
