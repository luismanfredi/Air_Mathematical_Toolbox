from src.logging_config import setup_logging
from src.ui import airscal, scicalculator

if __name__ == "__main__":
    setup_logging(use_console=False)
    airscal()