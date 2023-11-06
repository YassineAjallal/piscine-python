ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

tuple_to_list = list(ft_tuple)
set_to_list = list(sorted(ft_set))

ft_list[1] = 'World!'
tuple_to_list[1] = 'France!'
set_to_list[1] = 'Paris!'
ft_dict['Hello'] = "42Paris!"

ft_tuple = tuple(tuple_to_list)
ft_set = sorted(set(set_to_list))

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)