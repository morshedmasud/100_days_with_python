import logging


def set_custom_log_info():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %P', filename="log_info/error.log", level=logging.DEBUG)


def report(e: Exception):
    logging.exception(str(e))


def error(comment):
    logging.error(comment)

