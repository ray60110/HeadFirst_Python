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

def create_data(source):
    try:
        with open(source, 'r') as file:
            data= file.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('file error'+ str(ioerr))
        return None

def adding_data(messy,clean):
    for x in messy:
        x= sanitize(x)
        if x not in clean:
            clean.append(x)
    clean.sort()
    three= clean[0:3]
    return three

james= create_data('james.txt')
julie= create_data('julie.txt')
mikey= create_data('mikey.txt')
sarah= create_data('sarah.txt')

clean_jam=[]
clean_jul=[]
clean_mike=[]
clean_sara=[]

print(adding_data(james, clean_jam))
print(adding_data(julie, clean_jul))
print(adding_data(mikey, clean_mike))
print(adding_data(sarah, clean_sara))
