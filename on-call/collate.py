def total_incidents(incidents, type):
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
