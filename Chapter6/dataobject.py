def sanitize(time_string):
# create a function to produce standardized time format. xx.xx
# erase anyother marks wihin each value.
    if '-' in time_string:
        splitter= '-'
    elif ':' in time_string:
        splitter= ':'
    else:
        return(time_string)
    (mins, secs)= time_string.split(splitter)
    return(mins+'.'+secs)

def create_dict(source):
    try:
        with open(source, 'r') as file:
            data= file.readline()
            temp= data.strip().split(',')
            return({'name':temp[0],
                    'dob':temp[1],
                    'time':sorted(set([sanitize(x) for x in temp[2:]]))[0:3]})
            
    except IOError as ioerr:
        print('file error'+ str(ioerr))
        return None

print(create_dict('sarah2.txt'))
print(create_dict('julie2.txt'))
print(create_dict('mikey2.txt'))
print(create_dict('james2.txt'))
