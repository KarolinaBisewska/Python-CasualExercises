# All f-string functions
# The general shape is: f"{value:<alignment>signwidth,group.typeprecision}"

# 1. Alignment (<  >  ^  =)
# < Left-align (default for strings)
# > Right-align (default for numbers)
# ^ Center
# = Force the padding to be placed between the sign and the digits (numbers only)

print(f"{'abc':<10}+r")  # output:  |abc       +r|
print(f"{'abc':>10}+r")  # output:  |       abc+r|
print(f"{'abc':^10}+r")  # output:  |   abc    +r|
print(f"{-123:=10}+r")   # output:  |-      123+r|


