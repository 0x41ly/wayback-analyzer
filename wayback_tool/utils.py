import logging

def setup_logger():
    """
    Sets up the logger for the application.

    Returns:
        logger (logging.Logger): The logger instance.
    """
    logger = logging.getLogger("wayback_tool_logger")
    logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG or change based on your preference

    # Create a console handler to output logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and attach it to the console handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Attach the handler to the logger
    logger.addHandler(console_handler)

    return logger

# Create a logger instance to be used in the app
logger = setup_logger()

def verbose_log(message):
    """
    Logs verbose level messages.

    Args:
        message (str): The message to log.
    """
    logger.debug(message)
