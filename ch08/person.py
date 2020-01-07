def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

print(build_person("john", "hooker"))

print(build_person("john", "hooker", 21))