#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    lst = []
    for i in range(list_length):
        try:
            lst.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            lst.append(0)
            print("out of range")
        except (ValueError, TypeError):
            lst.append(0)
            print("wrong type")
        except ZeroDivisionError:
            lst.append(0)
            print("division by 0")
        finally:
            pass
    return lst
