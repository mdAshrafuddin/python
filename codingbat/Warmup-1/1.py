def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

x = sleep_in(0, 1)
print(x)
