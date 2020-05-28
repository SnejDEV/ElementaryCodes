import logging

logging.basicConfig(filename="first.log",level=logging.DEBUG)
logging.debug("Debug message")
logging.info("Information message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
