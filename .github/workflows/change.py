from sys import argv
with open("om.py", 'w',encoding = 'utf-8') as f:
  f.write("print('Evil!')")

print("I wrote to om.py")

print(argv)
print(list(argv[1]))
print(argv[1] + "HELLO WOROL")
print("HELLO WORLD" + argv[1] + "HELLO WOROL")
print(argv[1][::-1])
