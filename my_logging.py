import logging
import pdb

class Logger:
    def __init__(self, name='main', debug=True):
        self.logger = logging.getLogger(name)
        self.config_logger(name=name, debug=debug)

    def get_logger(self):
        return self.logger
    # def get_logger(self, name):
    #     return logging.getLogger(name)

    def config_logger(self, name, debug = True):
        if debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

        #formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        stream_format = logging.Formatter('%(message)s')

        #file_handler = logging.FileHandler('timesheet_automation.log')
        stream_handler = logging.StreamHandler()
        stream_handler.terminator = ""

        #file_handler.setFormatter(formatter)
        stream_handler.setFormatter(stream_format)
        #self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)
        return self.logger

    

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
