string_list = ["apple", "banana", "cherry", "date", "fig"]
int_list = [5, 3, 8, 1, 9, 2]
print(string_list + int_list)
print(len(string_list))
print(string_list[0:-1])
print(int_list[1:4])
string_list = ["apple", "banana", "cherry", "date", "fig"]
string_list.append("grape")
print(string_list)
string_list = ["apple", "banana", "cherry", "date", "fig"]
string_list.insert(2,"orange")
print(string_list)
int_list = [5, 3, 8, 1, 9, 2]
int_list_2 = [10, 11, 12]
int_list.extend(int_list_2)
print(int_list)
string_list = ["apple", "banana", "cherry", "date", "fig"]
string_list.remove("banana")
print(string_list)
string_list = ["apple", "banana", "cherry", "date", "fig"]
string_list.pop()
print(string_list)
string_list = ["apple", "banana", "cherry", "date", "fig"]
string_list.reverse()
print(string_list)
int_list = [5, 3, 8, 1, 9, 2]
int_list.sort()
print(int_list)
int_list = [5, 3, 8, 1, 9, 2]
int_list.sort(reverse=True)
print(int_list)
int_list = [5, 3, 8, 1, 9, 2]
print(min(int_list))
print(max(int_list))
print(sum(int_list))
string_list = ["apple", "banana", "cherry", "date", "fig"]
print(string_list.index("cherry"))
print("fig" in string_list)
for item in int_list:
    print(int_list)
string_list = ["apple", "banana", "cherry", "date", "fig"]
for index,string_list in enumerate(string_list):
    print(index,string_list)
string_list = ' - '.join(string_list)
print(string_list)
string_list = ["apple", "banana", "cherry", "date", "fig"]
new_list = "apple-banana-cherry-date"
new_list = new_list.split('-')
print(new_list)
fruit_tuple = ("mango", "pineapple", "papaya", "guava")
print(fruit_tuple)
for item in fruit_tuple:
    print(fruit_tuple)
print(fruit_tuple[0:])
set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8, 9}
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_1.union(set_2))
