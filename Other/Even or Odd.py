input_number=17
if(input_number%2==0):
    print("This is an even number.")

number=5
if(number):
    print("This number is truthy.")

zero=0
if(not zero):
    print("Zero is considered falsy.")

text="hello"
if(text):
    print("This string has content (truthy).")

empty_text=""
if(not empty_text):
    print("This string is empty (falsy).")