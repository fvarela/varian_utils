import logging

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    stream_format = logging.Formatter('%(message)s')

    #file_handler = logging.FileHandler('timesheet_automation.log')
    stream_handler = logging.StreamHandler()
    stream_handler.terminator = ""

    #file_handler.setFormatter(formatter)
    stream_handler.setFormatter(stream_format)
    #logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


logger = get_logger()