import logging

logging.basicConfig(filename = 'test.log', level=logging.INFO)

logging.debug("This is debug log")
logging.info("THis is info log")
logging.warning("This is warning log")
logging.error("This is error log")
logging.critical("This is critical log")