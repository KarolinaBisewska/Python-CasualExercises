# All f-string functions
# The general shape is: f"{value:<alignment>signwidth,group.typeprecision}"
# 1. Alignment (<  >  ^  =)
# < Left-align (default for strings)
# > Right-align (default for numbers)
# ^ Center
# = Force the padding to be placed between the sign and the digits (numbers only)



value = 123

print(f"{value:<10}")
