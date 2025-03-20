from loguru import logger
import os
import sys

class LoggerService:
    def __init__(self, log_dir='logs/'):
        os.makedirs(log_dir, exist_ok=True)

        logger.remove()

        # Logs de ERRO (em vermelho)
        logger.add(
            f"{log_dir}/crawler_errors.log",
            rotation="5 MB",
            retention="7 days",
            level="ERROR",
            format="<red>{time:YYYY-MM-DD HH:mm:ss}</red> | "
                   "<level>{level}</level> | "
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                   "<red>{message}</red>"
        )

        # Logs de WARNING (em amarelo)
        logger.add(
            f"{log_dir}/crawler_errors.log",
            rotation="5 MB",
            retention="7 days",
            level="WARNING",
            format="<yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> | "
                   "<level>{level}</level> | "
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                   "<yellow>{message}</yellow>"
        )

        # Logs em JSON
        logger.add(
            f"{log_dir}/crawler_errors.json",
            rotation="5 MB",
            retention="10 days",
            level="ERROR",
            serialize=True
        )

        sys.excepthook = self.handle_unhandled_exception
        self.logger = logger

    def handle_unhandled_exception(self, exc_type, exc_value, exc_traceback):
        self.logger.error(
            f"Erro fatal não tratado: {exc_type.__name__} - {exc_value}"
        )
        
    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)
