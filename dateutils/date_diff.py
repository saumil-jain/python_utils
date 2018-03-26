import datetime


def parse_date(date_str):
    """Parses a date string

    The date string should be in the format dd/mm/yyyy

    :param date_str: The input date string
    :return: A datetime.datetime object representing the input date
    :raises: IndexError and ValueError if date not in the required format
    """
    try:
        date_list = date_str.split("/")
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        date_object = datetime.date(year=year, month=month, day=day)

        return date_object
    except (IndexError, ValueError) as e:
        print("Invalid date format '{}'. It must be in the format dd/mm/yyyy".format(date_str))
        raise


def calculate_date_diff_from_today(date_object):
    """Calculates the difference between input date and today's date.

    :param date_object: The datetime.date object representing the input date
    :return: the difference of the two dates as a datetime.timedelta object.
    """
    today = datetime.date.today()
    difference = today - date_object
    return date_object, today, difference


def main():
    date_str = input("Enter date:\n")
    try:
        date_object, today, date_difference = calculate_date_diff_from_today(parse_date(date_str))
        print("The difference between {} and {} (today) is {}".format(date_object, today, date_difference))
    except Exception as e:
        print("Not able to calculate difference")
        print(e)


if __name__ == "__main__":
    main()
