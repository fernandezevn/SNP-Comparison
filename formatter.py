import re, sys                                                                                                                                                                                                  

in_file = open(sys.argv[1], "r")
out_file = open(sys.argv[2], "w")


for str in in_file:

    match = re.search(r"(\d{1}|\.)(:\S+)\s+", str)
    st = str
    if(match):
        st = str.replace(match.group(2), "")

    while(str != st):
        str = st
        match = re.search(r"(\d{1}|\.)(:\S+)", str)
        if(match):
            st = str.replace(match.group(2), "")


    gen = re.search(r"\d{1}(\/)\d{1}", str)
    st = str
    if(gen):
        st = str.replace(gen.group(1), "|")

    while(str != st):
        str = st
        gen = re.search(r"\d{1}(\/)\d{1}", str)
        if(match):
            st = str.replace(gen.group(1), "|")


    out_file.write(str)

in_file.close()
out_file.close()
