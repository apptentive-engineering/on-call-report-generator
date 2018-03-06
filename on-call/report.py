from collate import total_incidents
from helper import debug
from settings import (END_OFF, END_PEAK, PAGERDUTY_TOKEN, SINCE,
                      START_OFF, START_PEAK, TIME_ZONE, UNTIL)
from timewindow import duration, during, end_datetime

import datetime
import dateutil
import pygerduty.v2


def report():
    pager = pygerduty.v2.PagerDuty(PAGERDUTY_TOKEN)
    debug('Connecting to PagerDuty...\n')

    incidents = {}
    for incident in pager.incidents.list(since=SINCE, until=UNTIL, time_zone=TIME_ZONE):
        debug('New "{incident}" incident!'.format(incident=incident.title))

        if incident.title not in incidents:
            incidents[incident.title] = {
                'urgency': incident.urgency,
                'total_duration': datetime.timedelta(),
                'total_incidents': 0,
                'off_hours': 0,
                'peak_sleep': 0
            }

        incidents[incident.title]['total_duration'] += duration(incident)
        debug('Total duration to ' + str(incidents[incident.title]['total_duration']), 2)

        incidents[incident.title]['total_incidents'] += 1
        debug('Total incidents to ' + str(incidents[incident.title]['total_incidents']), 2)

        if incident.urgency != 'low':
            debug('Checking if during off hours...', 2)
            if during(dateutil.parser.parse(incident.created_at),
                      end_datetime(incident, UNTIL),
                      START_OFF, END_OFF):
                incidents[incident.title]['off_hours'] += 1
                debug('Occurred during off hours!', 3)

            debug('Checking if during peak sleep...', 2)
            if during(dateutil.parser.parse(incident.created_at),
                      end_datetime(incident, UNTIL),
                      START_PEAK, END_PEAK):
                incidents[incident.title]['peak_sleep'] += 1
                debug('Occurred during peak sleep!', 3)

        debug()

    debug()

    for incident, metrics in incidents.items():
        print(incident + ':')
        print('            Urgency:', metrics['urgency'])
        print('     Total Duration:', metrics['total_duration'])
        print('    Total Incidents:', metrics['total_incidents'])
        print('   Off Hours Alerts:', metrics['off_hours'])
        print('  Peak Sleep Alerts:', metrics['peak_sleep'], '\n')

    print('\n Total Off Hours Alerts:', total_incidents(incidents, 'off_hours'))
    print('Total Peak Sleep Alerts:', total_incidents(incidents, 'peak_sleep'))
