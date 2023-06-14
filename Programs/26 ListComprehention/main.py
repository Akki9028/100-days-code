
import pandas

file1_data = pandas.read_csv("file1.txt",names=['colA'], header=None)["colA"].to_list()
print(file1_data)

file2_data = pandas.read_csv("file2.txt",names=['colA'], header=None)["colA"].to_list()
print(file2_data)

list = [item for item in file1_data if item in file2_data ]

print(list)



# Write your code above 👆

# print(result)


