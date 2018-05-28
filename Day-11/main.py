from webscrap import wlog

wlog.set_custom_log_info("html/error.log")

try:
    raise Exception
except Exception as e:
    wlog.report(e)