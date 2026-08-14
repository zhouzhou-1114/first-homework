f = open("test.txt", "w")
f.write("hello,python!")
f.close()

f = open("test.txt", "r")
content = f.read()
f.close()

print("文件里是: ", content)