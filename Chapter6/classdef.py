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


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name= a_name
        self.dob= a_dob
        self.extend(a_times)

    def top3(self):
        return( sorted(set([sanitize(x) for x in self]))[0:3])
    

def create_data(source):
    try:
        with open(source, 'r') as file:
            data= file.readline()
        temp= data.strip().split(',')
        return(AthleteList(temp.pop(0),temp.pop(0),temp))
               
    except IOError as ioerr:
        print('file error'+ str(ioerr))
        return None
