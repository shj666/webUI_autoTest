import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('./Logger')
ch = logging.StreamHandler()


logger.addHandler(fh)
logger.addHandler(ch)

formatter = logging.Formatter('%(asctime)s - %(name)s - $(levername)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)