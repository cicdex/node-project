from sys import argv
with open("om.py", 'w',encoding = 'utf-8') as f:
  f.write("print('Evil!')")

print("I wrote to om.py")

print(argv)