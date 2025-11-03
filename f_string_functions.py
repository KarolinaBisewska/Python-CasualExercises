    # All f-string functions
    # The general shape is: f"{value:<alignment>signwidth,group.typeprecision}"
  
    # 1. Alignment (<  >  ^  =)
    # < Left-align (default for strings)
    # > Right-align (default for numbers)
    # ^ Center
    # = Force the padding to be placed between the sign and the digits (numbers only)

amount = 5
print(f"{'abc':<10}+r")  # output:  |abc       +r|
print(f"{'abc':>10}+r")  # output:  |       abc+r|
print(f"{'abc':^10}+r")  # output:  |   abc    +r|
print(f"{-123:=10}+r")   # output:  |-      123+r|
print(f"{amount:>3} {'max':>10}")   # output:  |  5        max|

    # 2. Fill character (any char except { })

print(f"{amount:*>10}")   # output:  |*********5|

    # 3. Width (minimum field width)

print(f"{'view'}{amount:10}")    # output:  |view         5|

    # 4. Sign handling (+ - space)
    #     + Always show sign (+ for positive, - for negative)
    #     - Only show - for negative (default for numbers)






















