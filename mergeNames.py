
def unique_names(names1, names2):
    return list(set(names1 + names2))


names1 = ["Jim", "Bob", "John", "Bill"]
names2 = ["Pat", "Mike", "Bob", "Bob", "Pat"]


print(unique_names(names1, names2))
