def convert_into_24hr(time_12hr):

    if time_12hr[-2:] == "AM":
        remove_am = time_12hr.replace('AM', '')
        if time_12hr[:2] == "12":
            x = remove_am.replace('12', '00')
            return x
        return remove_am

    elif time_12hr[-2:] == "PM":
        remove_pm = time_12hr.replace('PM', '')
        if time_12hr[:2] == "12":
            return remove_pm
        hour = int(time_12hr[:2])
        hour_24format = str(hour + 12)
        hour_24format = remove_pm.replace(remove_pm[:2], hour_24format)
        return hour_24format


print(convert_into_24hr("12:01:00PM"))
print(convert_into_24hr("12:01:00AM"))
print(convert_into_24hr("07:05:45PM"))
