#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    '''Divides element by element 2 lists.

    Args:
        my_list_1 (list): The first parameter.
        my_list_2 (list): The second parameter.
        list_length (int): The third parameter.
    Returns:
        A new list (length = list_length) with all divisions.'''
    result_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)
    return result_list
