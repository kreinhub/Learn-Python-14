with open("referat.txt", "r") as in_file, open("output.txt", "w") as out_file:
    content = in_file.read()
    print(f"The length of string is {len(content)}")
    
    in_file.seek(0)
    line = ""
    for i in in_file:
        s = i.replace("\n", " ").lstrip(" ").replace(".","!")
        line += s
    words = line.split()
    print(f"The count of words is {len(words)}")
    
    out_file.write(line)