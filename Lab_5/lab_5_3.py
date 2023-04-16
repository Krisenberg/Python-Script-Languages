import logging
import sys


def loggingConfig(min_level):
    num_level = getattr(logging, min_level)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(level=num_level)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stderr_handler = logging.StreamHandler(sys.stderr)

    stdout_handler.setLevel(logging.DEBUG)
    stderr_handler.setLevel(logging.ERROR)

    formatter_stdout = logging.Formatter('%(asctime)s - %(message)s')
    formatter_stderr = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stdout_handler.setFormatter(formatter_stdout)
    stderr_handler.setFormatter(formatter_stderr)

    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)
    return logger

def logLine(line, logger):
    # sys.stderr = open('stderr.log', 'w')
    logger.debug(f'Read {len(line)} bytes')
    if 'accepted password' in line.lower() or 'connection closed' in line.lower():
        logger.info(line.strip())
    if 'authentication failure' in line:
        logger.warning('Possible authentication failure: ' + line.strip())
    if 'error' in line:
        logger.error(line.strip())  
    if 'POSSIBLE BREAK-IN ATTEMPT' in line:
        logger.critical(line.strip())

    # with open(filePath, 'r') as f:
    #     for line in f:
    #         logging.debug(f'Read {len(line)} bytes')
    #         if 'accepted password' in line.lower() or 'connection closed' in line.lower():
    #             logging.info(line.strip())
    #         if 'authentication failure' in line:
    #             logging.warning('Possible authentication failure: ' + line.strip())
    #         if 'error' in line:
    #             logging.error(line.strip())  
    #         if 'POSSIBLE BREAK-IN ATTEMPT' in line:
    #             logging.critical(line.strip())