def print_success(message):
    print(f"\033[0;32m{message}\033[0m \n")

def print_error(message):
    print(f"\033[0;31m{message}\033[0m \n")

def print_info(message):
    print(f"\033[0;33m{message}\033[0m \n")



def print_r_success(message):
    return(f"\033[0;32m{message}\033[0m")

def print_r_error(message):
    return(f"\033[0;31m{message}\033[0m")

def print_r_info(message):
    return(f"\033[0;33m{message}\033[0m")

def dollar(value, val):
    return(f"{value:.{val}f}")