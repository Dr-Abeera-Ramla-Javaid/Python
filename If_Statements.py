# IF STATEMENT
is_female = True
is_tall = True
if is_female and is_tall:
    print("You are a tall female.")
elif is_female and not is_tall:
    print("You are a short female.")
elif not is_female and  is_tall:
    print("You are not a female but are tall.")
else:
    print("You are either not female or not tall or both.")

# IF STATEMENT AND COMPARISONS
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 40, 5))