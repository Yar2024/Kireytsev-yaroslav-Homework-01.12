#my_dict = {"a": 10, "b": 20, "c": 30}
#keys = list(my_dict.keys())
#print(keys)  # Виведе: ('a', 'b', 'c')
#values = list(my_dict.values())
#print(values)  # Виведе: [10, 20, 30]
#total_sum = sum(my_dict.values())
#print(total_sum)
# Два списки строк
list1 = ["a", "b", "c", "d"]
list2 = ["apple", "banana", "cherry", "date"]

# Створення словника з ключами з першого списку і значеннями з другого
result_dict = dict(zip(list1, list2))

# Виведемо результат
print(result_dict)
