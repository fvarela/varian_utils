import logging
import pdb

def get_logger(name):
    return logging.getLogger(name)

def config_logger(name, debug):
    logger = logging.getLogger(name)

    if debug:
        logger.setLevel(logging.DEBUG)
    else:
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


# #logger = get_logger()
# # def config_logger(debug):
# #     logger = logging.getLogger(__name__)
# def config_logger(debug):
#     logger = logging.getLogger(__name__)
#     pdb.set_trace()
#     if debug:
#         logger.setLevel(logging.DEBUG)
#     else:
#         logger.setLevel(logging.INFO)

#     formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
#     stream_format = logging.Formatter('%(message)s')

#     #file_handler = logging.FileHandler('timesheet_automation.log')
#     stream_handler = logging.StreamHandler()
#     stream_handler.terminator = ""

#     #file_handler.setFormatter(formatter)
#     stream_handler.setFormatter(stream_format)
#     #logging.addHandler(file_handler)
#     logger.addHandler(stream_handler)
