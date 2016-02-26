def sanitize(time_string):
    if '-' in time_string:
        splitter= '-'
    elif ':' in time_string:
        splitter= ':'
    else:
        return time_string
    (mins, secs)= time_string.split(splitter)
    return(mins+'.'+secs)

try:
    with open('james.txt', 'r') as jam:
        record= jam.readline()
        james= record.strip().split(',')
    with open('julie.txt', 'r') as jul:
        record= jul.readline()
        julie= record.strip().split(',')
    with open('mikey.txt', 'r') as mike:
        record= mike.readline()
        mikey= record.strip().split(',')
    with open('sarah.txt', 'r') as sara:
        record= sara.readline()
        sarah= record.strip().split(',')

except IOError as ioerr:
    print('error', str(ioerr))

clean_jam=[sanitize(each_jam) for each_jam in james]
clean_jul=[sanitize(each_jul) for each_jul in julie]
clean_mike=[sanitize(each_mike) for each_mike in mikey]
clean_sara=[sanitize(each_sara) for each_sara in sarah]

print(sorted(clean_jam), end='\n')
print(sorted(clean_jul), end='\n')
print(sorted(clean_mike), end='\n')
print(sorted(clean_sara), end='\n')
