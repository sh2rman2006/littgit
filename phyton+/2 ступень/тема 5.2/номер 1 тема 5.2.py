def month(n, l):
    ru=['',"январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    en=['',"January","February ","March ","April","May ","June ","July ","August ","September ","October ","November ","December "]
    if l=="ru":
        return ru[n]
    if l=="en":
        return en[n]
    else:
        return "ERROR"
print(month(int(input("-")), input("-")))

