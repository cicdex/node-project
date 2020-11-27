from sys import argv

print(argv)
print(list(argv[1]))
print(argv[1] + "HELLO WOROL")
print(argv[1].split('.'))

for i in argv:
  print(list(i))
  
