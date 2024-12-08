import logging
import yaml
import os

log = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.CRITICAL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="critical_log.log",
    force=True)
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="error_log.log",
    force=True)
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="warning_log.log",
    force=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="info_log.log",
    force=True)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="debug_log.log",
    force=True)

log.debug("This is a debug message")
log.info("This is an info message")
log.warning("This is a warning message")
log.error("This is an error message")
log.critical("This is a critical message")

list = [1,2,3,4,5]
for number in list:
    try:
        log.debug(f"This is a debug message {list[number]}")
    except Exception as ie:
        log.critical(f"{number} is not in the index")

for number in range(len(list)):
    print(number)