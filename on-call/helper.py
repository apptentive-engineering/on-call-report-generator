from settings import DEBUG_INDENT, VERBOSITY

import sys


ISO_8601_DATE_FORMAT = '%Y-%m-%d'
ISO_8601_TIME_FORMAT = '%H:%M:%S'
ISO_8601_COMBINED_FORMAT = ISO_8601_DATE_FORMAT + 'T' + ISO_8601_TIME_FORMAT + '%z'


def debug(message='', verbosity=1):
    """
    Prints debug messages to stderr at varying verbosity levels

    :param message: string -- debug message
    :param verbosity: int -- verbosity level
    """

    if VERBOSITY >= verbosity:
        sys.stderr.write((' ' * DEBUG_INDENT * (verbosity - 1)) + message + '\n')
