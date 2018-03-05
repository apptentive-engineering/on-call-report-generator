import os
import sys

DEBUG       = True
VERBOSITY   = 3
INDENT_SIZE = 4

PAGERDUTY_TOKEN = os.environ['PAGERDUTY_TOKEN']

TIME_ZONE = 'PST8PDT'               #: IANA time zone database format

SINCE = sys.argv[1] + 'T09:30:00'   #: ISO 8601 combined datetime format
UNTIL = sys.argv[2] + 'T09:29:59'   #: ISO 8601 combined datetime format

START_OFF  = '17:30:00'             #: ISO 8601 extended time format
END_OFF    = '08:30:00'             #: ISO 8601 extended time format
START_PEAK = '00:00:00'             #: ISO 8601 extended time format
END_PEAK   = '06:00:00'             #: ISO 8601 extended time format
