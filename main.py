#count_integer(numbers, integer)
def count_integer(list, x):
    count = 0
    for x in list:
        if x == int:
            count = (count + 1)
        print("{} occurs in your list {} times.".format(x, count+1))
        if count == 0:
            return 42


#list_func(numbers, integer)
def list_func(numbers, integer):
    result = False
    new_list = []
    for i in numbers:
        if i == integer:
            result = True
            new_list.append(6)
        else: new_list.append(i)
    original = new_list.copy()
    new_list.reverse()
    if not result:
        empty_list = []
        return empty_list
    else:
        print(new_list)
    return original



#compare_lists(list1, list2)
def compare_lists(list1, list2):
    list1_set = set(list1)
    list2_set = set(list2)
    if (list1_set & list2_set):
        print(list1_set and list2_set)
    else:
        print("[]")


#dict_func(dictionary)

def dict_func(dictionary):
    type = "unknown type"
    if "Type" in dictionary:
        type = dictionary["Type"]
    brand = "unknown brand"
    if "Brand" in dictionary:
        brand = dictionary["Brand"]
    price = "unknown price"
    if "Price" in dictionary:
        price = dictionary["Price"]
    print(f'You have a {type} from {brand} that costs {price}.')
    dictionary["OS"] = "Linux"
    print(dictionary)
    return dictionary
