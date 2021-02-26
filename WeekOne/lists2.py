person = ['Maximo', 10, 1000, True]

person.append('Mugisha')
# print(person)

person.extend(['Maximo', 20, 10.0, False])
# print(person)

# remove values
person.remove('Maximo')
# print(person)

# challenge, remove all repeating values
# without using .remove()

# insert  it doesnt replace, it shifts to the right

person.insert(5, 'Dog')
# print(person)

# sorting a list
list2 = [10, 1, 140, 5, 50, 11]
s_list = sorted(list2)
# print(s_list)

# challenge 2, sort a list without sorted() func
for i in range(len(list2)):
    if list2[-1] > list2[i]:
        list2[-1], list2[i] = list2[i], list2[-1]
# print(list2)


# finding max in a list
def max_num():
    l = [1, 5, 3, 2, 4, 334, 52]
    max = 0
    for i in range(len(l)):
        if max < l[i]:
            max = l[i]
    print(max)


#lists manipulation Slicing
# lis[2:] means everything from index 2 onwards
# lis[:2] means everything upto index 2
# max_num()


# try outs
# difference between lists, and tuples
# python dictionaries and accessing Dictionary keys
