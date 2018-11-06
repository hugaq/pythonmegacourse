def string_length(mystring):
    if isinstance(mystring, (int, float)):
        print("Sorry numbers don't have length")
        return 0
    return len(mystring)

c = string_length(10)
