import logging
import datetime
import sys

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler(f'logs/{datetime.datetime.now().strftime("%Y_%m_%d_")}_server.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logging.basicConfig(
  encoding='utf-8',
  filemode='a',
  filename=f'',
  level=logging.INFO
)
# logging.basicConfig(level=logging.DEBUG)
def get_logger(name):
  logger = logging.getLogger(name)
  logger.setLevel(logging.INFO)
  logger.addHandler(console_handler)
  logger.addHandler(file_handler)
  logger.info('Logger initialized.')
  return logger
