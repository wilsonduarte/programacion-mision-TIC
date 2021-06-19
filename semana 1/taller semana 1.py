print("Reto 1: Los cinco doses")

print("Como obtener el numero 5: 2 + 2 + 2 - (2/2) =", 2 + 2 + 2 - (2/2)) 
print("Como obtener el numero 6: 2 + 2 + 2 + 2 - 2 =", 2 + 2 + 2 + 2 - 2) 
print("Como obtener el numero 7: 2 + 2 + 2 + (2/2) =", 2 + 2 + 2 + (2/2)) 
print("Como obtener el numero 8: 2 * 2 * 2 - 2 +2  =", 2 * 2 * 2 - 2 +2) 
print("Como obtener el numero 9: 2 * 2 * 2 + (2/2) =", 2 * 2 * 2 + (2/2))
print("Como obtener el numero 10: 2 + (2*2) + (2*2) =", 2 + (2*2) + (2*2)) 
print('''

''')
print("Reto 2: ¿Cuanto costara el telefono?")
precio_total = 420
valor_impuesto = precio_total / 1.21
precio_neto = precio_total - valor_impuesto
print("precio total", precio_total)
print("valor impuesto", valor_impuesto)
print("precio neto", precio_neto)

#aumento el 20% al valor net
precio_neto_dia_siguiente = precio_neto + (precio_neto * 0.20)

#aplico el 21% de impuesto sobre el nuevo valor netro
print()
precio_final_dia_siguiente = precio_neto_dia_siguiente + (precio_neto_dia_siguiente * 0.21)
print("precio final al dia siguiente: ", precio_final_dia_siguiente)
print('''

''')
print("Reto 3: ¿Cuantas vueltas dará un fidget spinner?")
vueltas_minuto = 147
vueltas_segundo = vueltas_minuto / 60
print("vueltas por segundo: ", vueltas_segundo)
print("Numero de vueltas en 640 segundos: ", vueltas_segundo * 640)
print('''

''')
print("Reto 4: ¿Cuántas latas de refresco sobran?")
lata = 1
caja_refresco = lata * 24
total_refrescos = caja_refresco * 9
total_personas = 56
print("Tota de latas de refresco: ", total_refrescos)
print("Refrescos por persona", total_refrescos // total_personas)
print("Refescos restantes: ", total_refrescos % total_personas)