import yaml
import datetime

SCHEDULE_FILE = "config/schedules.yaml"

def current_time_in_range(start, end, now):
    start = datetime.datetime.strptime(start, "%H:%M").time()
    end = datetime.datetime.strptime(end, "%H:%M").time()

    if start < end:
        return start <= now <= end
    else:
        return now >= start or now <= end


def get_active_blocks():
    with open(SCHEDULE_FILE) as f:
        schedules = yaml.safe_load(f)

    now = datetime.datetime.now().time()
    active_blocks = set()

    for rule, config in schedules.items():
        if current_time_in_range(config["start"], config["end"], now):
            for category in config["block"]:
                active_blocks.add(category)

    return active_blocks
