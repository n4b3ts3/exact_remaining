"""
  I dont know if this formula has any other name, i am just using this in some repos and for reference sake i created this one
"""
number = float(input("Please input the desired number: "))
percent = float(input("Please input the percent you need to add: "))
exact_remaining = number + (number*percent)/(100-percent)
print(f"For getting {number} after substracting {(number*percent)/100} you need to use {exact_remaining}")
print(f"The resulting value then will be {(exact_remaining*percent)/100}")
