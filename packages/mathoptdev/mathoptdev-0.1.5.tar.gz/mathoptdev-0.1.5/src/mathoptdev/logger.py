import colorlog
import logging

logger = logging.getLogger("mathopt")
logger.setLevel(logging.DEBUG)

# Remove any existing handlers
logger.handlers = []

# Prevent propagation to the root logger
logger.propagate = False

# Create console handler with colored formatter
handler = colorlog.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'red,bg_white',
    }
)

handler.setFormatter(formatter)
logger.addHandler(handler)

