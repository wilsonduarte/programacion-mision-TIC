




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





def catalogacion_biblioteca(inventario):
	mantener = []
	eliminar_libros = []
	eliminar_revistas = []

	for item in inventario:
		eliminar = True

		if item['tipo'] == 'Libro':
			if item['tema'] == 'Administración' or item['tema'] == 'Física' or item['tema'] == 'Matemáticas':
				eliminar = False
			if item['tema'] == 'Tecnología' and item['año'] >= 2011:
				eliminar = False

		if item['tipo'] == 'Revista':
			if item['tema'] == 'Tecnología' and item['año'] >= 2018:
				eliminar = False
			elif item['tema'] != 'Tecnología' and item['año'] >= 2016:
				eliminar = False


		if not eliminar:
			final_autores = ''
			autores_list = item['autor'].split(',')
			for autor in autores_list:
				aux_list = autor.split(" ")
				for aux in aux_list[::-1]:
					final_autores += aux + ','
				final_autores += ";"

			item['autor'] = final_autores
			mantener.append(item)
		else:
			if item['tipo'] == 'Revista':
				eliminar_revistas.append( item['id'] )
			if item['tipo'] == 'Libro':
				eliminar_libros.append( item['id'] )


	return [mantener, eliminar_libros, eliminar_revistas] 







if __name__ == '__main__':
	# entrada = {
	#  "venta": 1500000.0,
	#  "cuota inicial": 200000.0,
	#  "cuotas": 12,
	#  "interes anual": 25.13
	# }
	# salida = simulador_financiacion_yo_le_fio(entrada)
	# print( salida )


	inventario = [{'id': '9786074386202',
		'nombre': 'Administración de compras',
		'tipo': 'Libro', 'tema':
		'Administración', 'autor': 'César Díaz,Andrés García', 'año': 2005,
		'paginas': 325}, {'id': '9786457821452',
		'nombre': 'Fundamentos de programación',
		'tipo': 'Libro', 'tema': 'Tecnología',
		'autor': 'César Díaz', 'año': 2006,
		'paginas': 500}, {'id': '7541258962456',
		'nombre': 'Actualidad matemática',
		'tipo': 'Revista', 'tema':
		'Matemáticas', 'autor': '', 'año': 1987,
		'paginas': 60}, {'id': '7541524784123',
		'nombre': 'Actualidad matemática',
		'tipo': 'Revista', 'tema': 'Tecnología',
		'autor': '', 'año': 2019, 'paginas':
		54}, {'id': '9786000515455', 'nombre':
		'Atomic Physics for Dummies', 'tipo':
		'Libro', 'tema': 'Física', 'autor':
		'Albert Einstein', 'año': 1975,
		'paginas': 50}]
	salida = catalogacion_biblioteca( inventario )
	print( salida  )

