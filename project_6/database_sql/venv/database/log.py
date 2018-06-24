import logging


def set_custom_log_info(file_name):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %P', filename=file_name, level=logging.INFO)


def success():
    logging.INFO("operation success")


def report(e: Exception):
    logging.exception(str(e))
