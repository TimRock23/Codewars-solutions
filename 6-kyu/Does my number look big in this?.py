def narcissistic( value ):
    string = str(value)
    num = 0
    for i in string:
        num += int(i) ** len(string)
    return num == value
