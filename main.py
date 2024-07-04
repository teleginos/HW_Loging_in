import requests as rq
import logging
from requests.exceptions import RequestException


def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(levelname)s: %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


success_logger = setup_logger('success_logger', 'success_responses.log', level=logging.INFO)
bad_logger = setup_logger('bad_logger', 'bad_responses.log', level=logging.WARNING)
blocked_logger = setup_logger('blocked_logger', 'blocked_responses.log', level=logging.ERROR)

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    # ДОПОЛНИТЬ КОД ЗДЕСЬ
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            success_logger.info(f"{site}, response = {response.status_code} ")
        else:
            bad_logger.warning(f"{site}, response = {response.status_code}")
    except RequestException:
        blocked_logger.error(f"{site}, NO CONNECTION")
