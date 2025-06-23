import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

GENERAL_LOG_FILE = os.path.join(LOG_DIR, "general.log")

# --- Formatter ---
def get_formatter(account_id=None):
    return logging.Formatter(
        fmt=f"%(asctime)s - %(levelname)s - {account_id or 'GENERAL'} - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

# --- Genel logger ---
_general_logger = logging.getLogger("general_logger")
_general_logger.setLevel(logging.DEBUG)

if not _general_logger.hasHandlers():
    # File handler
    file_handler = RotatingFileHandler(GENERAL_LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8")
    file_handler.setFormatter(get_formatter())

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(get_formatter())

    _general_logger.addHandler(file_handler)
    _general_logger.addHandler(console_handler)

# --- Genel loglama fonksiyonu ---
def log_general(message: str, level: str = "info"):
    """
    Genel log dosyasına ve ekrana mesaj yazar.
    level: info, warning, error, debug, critical
    """
    log_method = getattr(_general_logger, level.lower(), _general_logger.info)
    log_method(message)


# --- Hesap logger fonksiyonu ---
_loggers_by_account = {}

def log_account(account_id: str, message: str, level: str = "info"):
    """
    Belirtilen account_id için log mesajı yazar.
    Hem dosyaya hem ekrana yazılır.
    """
    if account_id not in _loggers_by_account:
        logger = logging.getLogger(f"account_{account_id}")
        logger.setLevel(logging.DEBUG)

        if not logger.hasHandlers():
            # File handler
            log_file = os.path.join(LOG_DIR, f"account_{account_id}.log")
            file_handler = RotatingFileHandler(log_file, maxBytes=2 * 1024 * 1024, backupCount=2, encoding="utf-8")
            file_handler.setFormatter(get_formatter(account_id))

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(get_formatter(account_id))

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        _loggers_by_account[account_id] = logger

    logger = _loggers_by_account[account_id]
    log_method = getattr(logger, level.lower(), logger.info)
    log_method(message)
