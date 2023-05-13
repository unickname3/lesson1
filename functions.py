def get_summ(one, two, delimeter="&"):
    return f"{one}{delimeter}{two}".upper()


result = get_summ("learn", "python")
print(result)
