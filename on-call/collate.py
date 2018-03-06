from helper import debug
from settings import SINCE, TIME_ZONE, UNTIL
from timewindow import duration, during_off_hours, during_peak_sleep

import datetime


def count_incident_type(incidents, type):
    """
    Gets total number of incidents of a certain type

    :param incidents: dictionary - set of incidents to parse
    :param type: string - key to parse within incidents
    :return: int - total incidents
    """

    total = 0

    for _, incident in incidents.items():
        total += incident[type]

    return total


def init_incident(incident):
    return {
        'urgency': incident.urgency,
        'total_duration': datetime.timedelta(),
        'total_incidents': 0,
        'off_hours': 0,
        'peak_sleep': 0
    }


def collate_incidents(pagerduty, since=SINCE, until=UNTIL, time_zone=TIME_ZONE):
    incidents = {}
    for incident in pagerduty.incidents.list(since=since, until=until, time_zone=time_zone):
        debug('New "{incident}" incident!'.format(incident=incident.title))

        if incident.title not in incidents:
            incidents[incident.title] = init_incident(incident)

        incidents[incident.title]['total_duration'] += duration(incident)
        debug('Total duration to ' + str(incidents[incident.title]['total_duration']), 2)

        incidents[incident.title]['total_incidents'] += 1
        debug('Total incidents to ' + str(incidents[incident.title]['total_incidents']), 2)

        if during_off_hours(incident):
            incidents[incident.title]['off_hours'] += 1

        if during_peak_sleep(incident):
            incidents[incident.title]['peak_sleep'] += 1

        debug()

    return incidents
