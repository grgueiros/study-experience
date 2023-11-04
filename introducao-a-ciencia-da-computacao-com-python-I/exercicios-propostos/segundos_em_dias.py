segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "));

#dias
segundos_por_dia = 86400

dias = segundos // segundos_por_dia
segundos_restantes_do_dia = segundos % segundos_por_dia

#horas
segundos_por_hora = 3600

horas = segundos_restantes_do_dia // segundos_por_hora
segundos_restantes_da_hora = segundos_restantes_do_dia % segundos_por_hora

#minutos
segundos_por_minuto = 60

minutos = segundos_restantes_da_hora // segundos_por_minuto
segundos_restantes_do_minuto = segundos_restantes_da_hora % segundos_por_minuto

print(dias, "dias,",horas, "horas,",minutos,"minutos e", segundos_restantes_do_minuto, "segundos.")

