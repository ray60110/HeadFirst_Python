man=[]
other=[]
# creating 2 lists for saving the strings that about to print to outmandata/
# outotherdata.

try:
    data=open('sketch.txt', 'r')

# using try & except to avoid IO/ Value error rather than expand codes.

    for each_line in data:
        try:
            (role, spoken_line)= each_line.split(':',1)
            spoken_line=spoken_line.strip()
            if role=='Man':
                man.append(spoken_line)
            elif role=='Other Man':
                other.append(spoken_line)
# go through all the lines in sketch, get the speakers and lines.
# put both values into role and spoken line. and into man and other list

        except ValueError:
            pass

    data.close()

except IOError:
    print('something is missing')

try:
    with open('man_data.txt','w') as out_man_data:
        print(man, file=out_man_data)
    with open('other_data.txt','w') as out_other_data:
        print(other, file=out_other_data)

except IOError as err:
    print('can not save, please check'+str(err))
