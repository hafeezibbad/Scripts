def format_duration(seconds):
    durations = {'year':0,
                 'days':0,
                 'hours':0,
                 'minute':0,
                 'second':0}
    while True:
        if seconds >= (86400*365):
            durations['year'] = seconds / (86400*365)
            seconds -= durations['year']*86400*365
        elif seconds >= 86400:
            durations['days'] =seconds / 86400
            seconds -= durations['day']*86400
        elif seconds >= 3600:
            durations['hour'] = seconds/3600
            seconds -= durations['hour']*3600
        elif seconds >= 60:
            durations['minute'] = seconds/60
            seconds -= durations['minute']*60
        else:
            durations['second'] = seconds
            break

    rer = ''
    if durations['year'] > 0:
        rer.
  # incomplete
print format_duration(3662)
