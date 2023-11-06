#Returns True or False based on whether the Personal Identity Codes given as an argument is valid or not.
#The first half of the code is a valid, existing date in the format ddmmyy.
#The century marker is either + (1800s), - (1900s) or A (2000s).
#The control character is valid.

from datetime import datetime
 
def is_it_valid(pic: str):
    year_prefixes = {'+': '18', '-': '19', 'A': '20'}
    valid_cmarker = pic[6] in year_prefixes
    
    year = year_prefixes.get(pic[6], '') + pic[4:6]
    try:
        date = datetime(int(year), int(pic[2:4]),  int(pic[0:2]))
    except ValueError:
        date = None
        
    valid_date = bool(date)
    
    cstring = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    valid_control = cstring[int(pic[0:6] + pic[7:10]) % 31] == pic[-1]
    valid_pic = valid_date and valid_cmarker and valid_control and len(pic) == 11
 
    return valid_pic