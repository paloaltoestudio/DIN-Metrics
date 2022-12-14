#Python
from datetime import date, datetime

def age(birthdate):
    if type(birthdate) == str:
        birthdate = birthdate
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age