from collate import collate_incidents, count_incident_type
from helper import debug
from settings import PAGERDUTY_TOKEN

import pygerduty.v2


def print_summary(incidents):
    for incident, metrics in incidents.items():
        print('''
{incident}:
              Urgency: {urgency}
       Total Duration: {total_duration}
      Total Incidents: {total_incidents}
     Off Hours Alerts: {off_hours}
    Peak Sleep Alerts: {peak_sleep}
'''.format(incident=incident,
           urgency=metrics['urgency'],
           total_duration=metrics['total_duration'],
           total_incidents=metrics['total_incidents'],
           off_hours=metrics['off_hours'],
           peak_sleep=metrics['peak_sleep']))

    print('''
 Total Off Hours Alerts: {total_off}
Total Peak Sleep Alerts: {total_peak}
'''.format(total_off=count_incident_type(incidents, 'off_hours'),
           total_peak=count_incident_type(incidents, 'peak_sleep')))


def report():
    pager = pygerduty.v2.PagerDuty(PAGERDUTY_TOKEN)
    debug('Connecting to PagerDuty...\n')
    incidents = collate_incidents(pager)
    print_summary(incidents)
