def check_func(first_str, second_str):
    if type(first_str) == str and type(second_str) == str:
        if first_str == second_str:
            return 1
        elif first_str != second_str and len(first_str) > len(second_str):
            return 2
        elif first_str != second_str and second_str == 'learn':
            return 3
    else:
        return 0


print(check_func(123, 'learn'))