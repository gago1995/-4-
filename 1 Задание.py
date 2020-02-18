from sys import argv
def wages (hour, rate):
    wages = float(hour)*float(rate) + float(hour)*float(rate)*0.2
    return print(f'ЗП соаставила: {round(wages,2)} ')
wages(argv[1], argv[2])
