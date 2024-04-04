import linecache
import ast

modified_op_file = "deepsara_20_output_modified.txt"
f = open(modified_op_file, "r")
line_number = 3
line = ast.literal_eval(linecache.getline(modified_op_file, line_number))
print(type(line))
print(len(line))
# print(f.read())