status_code = int(input("please input the code:"))
match status_code:
    case 400: descrp = 'bad'
    case 401: descrp = 'unauthorized'
    case 402: descrp = 'forbidden'
    case 403: descrp = 'not found'
    case 404: descrp = 'not allowed'
    case _: descrp = 'unknown code'
print('description:', descrp)