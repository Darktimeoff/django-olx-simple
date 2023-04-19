
def date_time_field(time):
    return time.replace(tzinfo=None).isoformat(timespec='microseconds') + 'Z'