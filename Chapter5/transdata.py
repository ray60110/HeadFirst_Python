def sanitize(time_string):
    if '-' in record:
        splitter= '-'
    elif ':' in record:
        splitter= ':'
    else:
        return(time_string)
    (mins, secs)= time_string.split(splitter)
    return(mins+'.'+secs)

clean_jam=[]
clean_jul=[]
clean_mike=[]
clean_sara=[]

try:
    with open('james.txt', 'r') as jam:
        record= jam.readline()
        james= record.strip().split(',')
        for jamesItem in james:
            clean_jam.append(sanitize(jamesItem))
    with open('julie.txt', 'r') as jul:
        record= jul.readline()
        julie= record.strip().split(',')
        for julieItem in julie:
            clean_jul.append(sanitize(julieItem))
    with open('mikey.txt', 'r') as mike:
        record= mike.readline()
        mikey= record.strip().split(',')
        for mikeyItem in mikey:
            clean_mike.append(sanitize(mikeyItem))
    with open('sarah.txt', 'r') as sara:
        record= sara.readline()
        sarah= record.strip().split(',')
        for sarahItem in sarah:
            clean_sara.append(sanitize(sarahItem))
except IOError as ioerr:
    print('error', str(ioerr))


print(sorted(clean_jam), end='\n')
print(sorted(clean_jul), end='\n')
print(sorted(clean_mike), end='\n')
print(sorted(clean_sara), end='\n')
