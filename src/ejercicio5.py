from datetime import date


def calcula_dia_semana(fecha):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia_numero = fecha.weekday() # NUMERO CORRESPONDIENTE AL DIA DE LA SEMANA
    return dias_semana[dia_numero]

dia = int(input("Introduce el día de tu nacimiento: "))
mes = int(input("Introduce el mes de tu nacimiento: "))
año = int(input("Introduce el año de tu nacimiento: "))

fecha_nacimiento = date(año, mes, dia)

dia_semana = calcula_dia_semana(fecha_nacimiento)

print(f"Naciste un {dia_semana}.")




