import datetime


def format_seconds(seconds: float):
    td = datetime.timedelta(seconds=seconds)
    return str(td)



if __name__ == '__main__':
    print(format_seconds(365030))