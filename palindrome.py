def palindrome():
    st = input("Enter a string:  ")
    reverse_string = st [::-1]
    if st == reverse_string:
        print("palindrome:")
    else:
        print("NOT")