from loguru import logger
import os
import sys

class LoggerService:
    def __init__(self, log_dir='src/logs'):
        os.makedirs(log_dir, exist_ok=True)

        logger.remove()
        # Logs em formato log
        logger.add(
            f"{log_dir}/crawler_errors.log",
            rotation="5 MB",
            retention="7 days",
            level="ERROR",
            format="<red>{time:YYYY-MM-DD HH:mm:ss}</red> | "
                   "<level>{level}</level> | "
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                   "<level>{message}</level>"
        )
        # Logs em Json
        logger.add(
            f"{log_dir}/crawler_errors.json",
            rotation="5 MB",
            retention="10 days",
            level="ERROR",
            serialize=True
        )

        sys.excepthook = self.handle_unhandled_exception
        self.logger = logger

    def handle_unhandled_exception(self, exc_type, exc_value):
            self.logger.error(
                f"Erro fatal não tratado: {exc_type.__name__} - {exc_value}"
            )
            
    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(self,message)