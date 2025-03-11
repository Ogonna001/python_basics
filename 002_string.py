my_sentence = "Python is fun and powerful!"
print(len(my_sentence))
print(my_sentence[0])
print(my_sentence[10:0])
print(my_sentence.lower())
print(my_sentence.count("o"))
print(my_sentence.find("fun"))
my_sentence = my_sentence.replace("powerful","amazing")
print(my_sentence)
new_message = "Learning Python is exciting!"
my_code = my_sentence + new_message
print(my_code)
my_code_format = "{}, {}".format(my_sentence,new_message)
print(my_code_format)
my_code_fstring = f'{my_sentence}, {new_message}'
print(my_code_fstring)
print(dir(my_sentence))
print(help(str.replace))
