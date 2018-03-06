import argparse
import os
import sys


parser = argparse.ArgumentParser()
parser.add_argument('SINCE_DAY',
                    help='report start date '
                    + '(ISO 8601 date format)')
parser.add_argument('UNTIL_DAY',
                    help='report end date '
                    + '(ISO 8601 date format)')
parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='verbose mode '
                    + '(Multiple -v options increase the verbosity. The maximum is 3)')
parser.add_argument('-t', '--token',
                    help='PagerDuty API token')
parser.add_argument('-z', '--timezone', default='PST8PDT',
                    help='time zone '
                    + '(IANA time zone database format)')
parser.add_argument('--start-off', default='17:30:00',
                    help='off-duty start time '
                    + '(ISO 8601 time format)')
parser.add_argument('--end-off', default='08:30:00',
                    help='off-duty end time '
                    + '(ISO 8601 time format)')
parser.add_argument('--start-sleep', default='00:00:00',
                    help='peak sleep start time '
                    + '(ISO 8601 time format)')
parser.add_argument('--end-sleep', default='06:00:00',
                    help='peak sleep end time '
                    + '(ISO 8601 time format)')
parser.add_argument('-f', '--format', default='stdout',
                    help='report format '
                    + '(e.g. text, confluence)')
args = parser.parse_args()


DEBUG = (args.verbose > 0)
VERBOSITY = args.verbose
INDENT_SIZE = 4
TIME_ZONE = args.timezone
START_OFF = args.start_off
END_OFF = args.end_off
START_PEAK = args.start_sleep
END_PEAK = args.end_sleep
SINCE = sys.argv[1] + 'T09:30:00'
UNTIL = sys.argv[2] + 'T09:29:59'


if args.token is None:
    try:
        PAGERDUTY_TOKEN = os.environ['PAGERDUTY_TOKEN']
    except KeyError:
        print('PAGERDUTY_TOKEN environment variable not set!')
        sys.exit(1)
else:
    PAGERDUTY_TOKEN = args.token
