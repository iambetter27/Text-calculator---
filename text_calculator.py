import time

print("Text Calculator! Operators: \"+, -, *, /, ^\"")
equation = input("Enter Here: ")

start = time.time()
emdas = ["*", "/", "+", "-", "^"]

math_phrase = []
n = []
previous_char = str()

# Adding the mathematical equation
for j in equation:
    # If it is an operator
    if j in emdas and previous_char not in emdas:
        # For the decimals
        if n[-1] != ".":
            math_phrase.append(float("".join(n))) # Append the list n converted to a string 
            math_phrase.append(j) # Append the operator
            n = []
        else:
            raise Exception("Sorry, a misstype with the decimals has occured in the equation.")
    # If it is an digit
    elif j.isdigit() :
        n.append(j) 
    # If it is an decimal
    elif j == ".":
        if j in n:
            raise Exception("Sorry, a misstype with the decimals has occured in the equation.")
        else:
            n.append(j)
    # For the useless spaces
    elif j == " ":
        continue
    
    else:
        raise Exception("Sorry, a misstype has occured in the equation.")
    
    previous_char = j

# Adding the last number
if len(n) > 0 and n[-1] != ".":
    math_phrase.append(float("".join(n)))
    del n
elif len(n) > 0 and n[-1] == ".":
    raise Exception("Sorry, a misstype with the decimals has occured in the equation.")
else:
    raise Exception("Sorry, a misstype has occured in the equation")

print(math_phrase)

def EMDAS(math_equation):
    try: 
        ########### EXPONANTS ################
        exponant_lst = math_equation
        muldiv_lst = []
        n = exponant_lst[0]
        i = 1
        while i < len(exponant_lst):
            if exponant_lst[i] == "^":
                n **= exponant_lst[i+1]
            else:
                muldiv_lst.append(n)
                muldiv_lst.append(exponant_lst[i])
                n = exponant_lst[i+1]
            i += 2
        # Add the last number depending on the last operator sign
        muldiv_lst.append(n)

        print(muldiv_lst)

        ########### MULTIPLY AND DIVIDE ################

        addsub_lst = []
        n = muldiv_lst[0]
        i = 1
        while i < len(muldiv_lst):
            if muldiv_lst[i] == "*":
                n *= muldiv_lst[i+1]
            elif muldiv_lst[i] == "/":
                n /= muldiv_lst[i+1]
            else:
                addsub_lst.append(n)
                addsub_lst.append(muldiv_lst[i])
                n = muldiv_lst[i+1]
            i += 2
        # Add the last number depending on the last operator sign
        addsub_lst.append(n)

        print(addsub_lst)

        ############### ADDITION AND SUBSTRACTION ####################

        n = addsub_lst[0]
        i = 1
        while i < len(addsub_lst):
            if addsub_lst[i] == "+":
                n += addsub_lst[i+1]
            elif addsub_lst[i] == "-":
                n -= addsub_lst[i+1]
            i += 2

        return n

    except ZeroDivisionError:
        raise Exception("Error in calculations (maybe with 0!). Try again!")

def PEMDAS(math_equation):
    count_opening_parentheses = 0
    count_ending_parentheses = 0


result = EMDAS(math_phrase)
if int(result) == result:
    result = int(result)
    
print("Result: "+str(result))

end = time.time()
t = end - start
print(f"Time: {t} seconds")
