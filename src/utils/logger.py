import logging

utils_logger = logging.getLogger(__name__)
utils_logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/utils.log")
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
utils_logger.addHandler(handler)
