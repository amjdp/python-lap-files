def name_processing(list_of_names):
    prefix = ["Mr.", "Dr.", "Ms."]
    result = []
    for name in list_of_names:
        name = name.split(" ")
        check = any(item in prefix for item in name)
        if check:
            name.pop(0)
        for idx, n in enumerate(name):
            name[idx]=n.capitalize()

        if len(name)==3:
            name[1]=name[1][0]+"."

        name = " ".join(name)
        result.append(name)
    return(result)
        


names=["Mr. robert allen zimmerman", "GEORGE ORWELL", "muhammed ali",
       'Ms. viriginia woolfe']

print(name_processing(names))
