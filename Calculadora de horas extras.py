def dinero(tarifa, hora):
	
	ganancia_total  = (tarifa * hora)
	
	return (ganancia_total)

try:
	
	ganancia = int(input("¿cuanto cobras por hora? \n> "))
	
	tiempo = int(input("¿cuantas horas trabajas? \n> "))
	
	
	if (tiempo) <= (40):
		
		resultado = dinero(ganancia, tiempo)
		
		print (resultado)
		
		
	elif (tiempo) >= (41):
		
		horas_extras = (tiempo - 40)
		
		aumento = (ganancia * 1.5)
		
		aumento_total = (horas_extras * aumento)
		
		resultado = dinero (ganancia, tiempo)
		
		print (resultado + aumento_total)
		
		
except:
	print("solo numeros")
