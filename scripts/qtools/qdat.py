from dateutil import parser

def convertDateToDisplayDate(date_string):
    """
    Converts a date string to 'DayOfWeek, Mon DD, YYYY' format.
    More flexible with different date string formats.
    """
    date_obj = parser.parse(date_string)
    display_date = date_obj.strftime('%A, %b %d, %Y')
    return display_date