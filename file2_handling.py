my_file=open("reya_files/file.txt","a+")

my_file.write("hello world! \n")
my_file.seek(0)
print(my_file.read())
my_file.close()