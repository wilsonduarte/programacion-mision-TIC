




def simulador_financiacion_yo_le_fio(entrada):
	salida = {}
	
	financiar = entrada['venta'] - entrada['cuota inicial']
	interes_anual = entrada['interes anual']
	interes_mensual = (1+(interes_anual/100))**(1/12) - 1

	salida['saldo financiar'] = financiar

	total_intere = ( 1 - (1+interes_mensual)**-entrada['cuotas']) / interes_mensual
	salida['cuota'] = financiar / total_intere
	salida['cuota'] = round( salida['cuota'], 0)

	salida['amortizacion'] = []
	mes = 0
	while financiar > 0:
		mes += 1

		interes = financiar * interes_mensual
		c_abonado =  salida['cuota'] - interes

		if (financiar+interes) >= (salida['cuota']+1):
			cuota = salida['cuota']
			c_abonado = c_abonado
			financiar =  financiar - c_abonado
		else:
			cuota = financiar + interes
			c_abonado = financiar
			financiar = 0
		
		financiar = float(round(financiar, 2))
		tupla = (mes, round(c_abonado,2), round(interes, 2), round(cuota, 2), round(financiar, 2) )
		salida['amortizacion'].append( tupla )

	return salida



if __name__ == '__main__':
	entrada = {
	 "venta": 1500000.0,
	 "cuota inicial": 200000.0,
	 "cuotas": 12,
	 "interes anual": 25.13
	}
	salida = simulador_financiacion_yo_le_fio(entrada)
	print( salida )
	