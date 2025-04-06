def find_x_percent_of_y(num,percent):
    print("Loading LIB Just Simple Py")
    out = percent/100 * num
    return out
def find_percentage(number,totalval):
    print("Loading LIB Just Simple Py")
    out = number/totalval * 100
    return out
def find_after_x_percent(number,percent):
    print("Loading LIB Just Simple Py")
    process1 = find_x_percent_of_y(number,percent)
    out = process1 + number
    return out
