import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename = 'test.log', filemode="w")

logging.debug("This is debug log")
logging.info("THis is info log")
logging.warning("This is warning log")
logging.error("This is error log")
logging.critical("This is critical log")