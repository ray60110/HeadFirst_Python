import pickle
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
except IOError as ioerr:
    print('something is missing' , str(ioerr))

try:
    with open('man_data.txt','wb') as out_man_data:
        pickle.dump(man, out_man_data)
    with open('other_data.txt','wb') as out_other_data:
        pickle.dump(other, out_other_data)
except pickle.PickleError as perr:
    print('PickleError', str(perr))
