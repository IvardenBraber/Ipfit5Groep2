def extension_check(path: str):
    path = path.split('.')
    extension = str(path[1])
    text = 'Wrong datatype'
    if(extension == 'dd'):
        type = 'raw'
    elif(extension == 'E01'):
        type = 'ewf'
    else:
        return text
    return(type)


