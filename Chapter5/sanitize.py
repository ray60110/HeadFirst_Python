def sanitize(time_string):
    if '-' in record:
        splitter= '-'
    elif ':' in record:
        splitter= ':'
    else:
        return(time_string)
    (mins, secs)= time_string.split(splitter)
    return(mins+'.'+secs)
    
        
