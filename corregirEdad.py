class Edad: 
    def __init__(self):
    	self.year = 0
    	self.month = 0
    	self.day = 0

def corregirEdad(ev, en, w):

	edadCorregida = Edad()

	edadCorregida.year = ev.year
	edadCorregida.month = ev.month

	if(en.month > ev.month):
		edadCorregida.month = (ev.month + 12)
		edadCorregida.year = (ev.year - 1)

	edadCorregida.month = edadCorregida.month - en.month - 2	
	edadCorregida.year -= en.year

	if(en.day > ev.day):
		ev.day += 30

	days = ev.day - en.day + 60
	res = (40 - w) * 7

	edadCorregida.day = days - res

	print("Edad corrregida:" + str(edadCorregida.year) + " " + str(edadCorregida.month) + " " + str(edadCorregida.day))

if __name__ == "__main__":
	
	ev_year = input("ano de evaluacion:") 
	ev_month = input("mes de evaluacion:") 
	ev_day = input("dia de evaluacion:") 

	edadEV = Edad()
	edadEV.year = ev_year
	edadEV.month = ev_month
	edadEV.day = ev_day

	en_year = input("ano de nacimiento:") 
	en_month = input("mes de nacimiento:") 
	en_day = input("dia de nacimiento:") 

	weeks = input("semanas de gestacion:") 

	edadN = Edad()
	edadN.year = en_year
	edadN.month = en_month
	edadN.day = en_day

	corregirEdad(edadEV, edadN, weeks)
