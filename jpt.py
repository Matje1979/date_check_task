import re


def get_commission(date_str):
    """
    Function that takes a string in the YYYY-MM-DD format and
    returns an info about the related commission
    """
    # Check if date_str is a valid date.
    pattern = re.compile(
        "^[0-2][0-9][0-9][0-9]-((0[1-9])|(1[0-2]))-(0[1-9]|[1-2][0-9]|3[0-1])$"
    )
    assert pattern.match(date_str)

    date_list = date_str.split("-")
    if 6 > int(date_list[1][1]) < 9:
        return float(15)
    return float(10)


if __name__ == "__main__":
    date_str = input("Please enter a date:")
    print(type(date_str))
    print(get_commission(date_str))
