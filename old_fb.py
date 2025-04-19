import logging
import coconuts

logging.basicConfig(level=logging.DEBUG)

try:
    coconuts.main()
except Exception as e:
    logging.error("An error occurred", exc_info=True)

