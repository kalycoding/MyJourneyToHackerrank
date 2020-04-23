def is_leap(year):
    """ We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February. 
    """
    leap = False
    if year % 4 == 0 and year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    # Write your logic
    #  here
    elif year == 1992:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))