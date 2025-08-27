SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def format_duration(time_delta):
        seconds = time_delta.total_seconds()
        hours = int(seconds // SECONDS_IN_HOUR)
        minutes = int((seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE)
        return f'{hours} часов {minutes} минут'