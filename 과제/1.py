def is_on_list(listname, str):
    return listname.count(str) > 0


def get_x(listname, index):
    return listname[index]


def add_x(listname, str):
    listname.append(str)


def remove_x(listname, str):
    listname.remove(str)


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)
