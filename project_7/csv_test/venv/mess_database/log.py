import logging


def set_custom_log_info():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %P', filename="log_file/error.log", level=logging.DEBUG)


def report(e: Exception):
    logging.exception(str(e))

