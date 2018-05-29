import logging

def set_custom_log_info(filename):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %P', filename=filename, level=logging.DEBUG)

def report(e:Exception):
    logging.exception(str(e))


