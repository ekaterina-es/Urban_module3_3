def print_params(a=1, b="строка", c=True):
    print(a, b, c)

print_params()
print_params(False, 5, "star")
print_params("star")
print_params(7, True)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [5.9, False, "sun"]
values_dict = {"a": "number", "b": "phone", "c": 7172}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [88, "rain"]
print_params(*values_list_2, 42)