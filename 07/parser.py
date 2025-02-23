def parse(inp):
    contents_list=inp.copy()
    i=0
    while True:

        try:
            contents_list[i]=contents_list[i].replace('\n', '')
            if '//' in contents_list[i]:
                contents_list[i]= contents_list[i][:contents_list[i].index('//')]

            if (contents_list[i].replace(' ', '')).replace('\t', '') =='' :
                contents_list.pop(i)

                continue

            contents_list[i]=contents_list[i].split()

            i+=1
        except Exception as e:
            break
    return contents_list