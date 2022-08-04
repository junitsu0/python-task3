# Problem 1 ---------------------

def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

hello_name("username")

# Problem 2 ---------------------

def first_odds(x):
    for x in range(1,101):
        if x % 2 == 1:
            print(x)
first_odds(x)

# Problem 3 ---------------------

def max_num_in_list(a_list):
    print(max(a_list))

max_num_in_list([5, 8, 15, 62, 27, 50, 31, 46])
# Problem 4 ---------------------

def is_leap_year(a_year):
    if a_year % 400 == 0 and a_year % 100 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False

is_leap_year(144)

# Problem 5 ---------------------

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

is_consecutive([2,3,4,5,6,7])