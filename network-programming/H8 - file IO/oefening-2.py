import logging


# Set the logging level correctly
logging.basicConfig(filename="app.log", level=logging.DEBUG)  # Use logging.DEBUG directly here

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")