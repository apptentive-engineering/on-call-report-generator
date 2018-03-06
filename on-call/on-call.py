#!/usr/bin/env python3

"""
This will generate an on-call report based on information pulled from
PagerDuty's API. The report will be generated in ConfluenceWiki format
and will be posted to a target space/path in a target Confluence wiki.

Usage: ./on-call.py SINCE_DAY UNTIL_DAY

SINCE_DAY -- ISO 8601 date
UNTIL_DAY -- ISO 8601 date

i.e. ./on-call.py 2017-07-24 2017-07-31
"""

from report import report


if __name__ == '__main__':
    report()
