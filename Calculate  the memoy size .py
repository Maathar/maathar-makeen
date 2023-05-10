memory_size=int(input("please enter memory size:"))
file_size=int(input("please enter file size:"))
number_of_file=int(input("please enter number of file:"))
                   
size_of_files=number_of_file*file_size


if size_of_files<memory_size:
    print("The size is enough")
    
else:
    print("The size is not enough")
                      