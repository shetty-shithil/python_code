import os

os.rename('file1.txt','file2.txt')
os.mkdir('dir2')
if os.path.exists("file3.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
