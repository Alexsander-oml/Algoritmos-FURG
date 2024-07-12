OP = int(input("Você quer converter de:\nCelsius para Fahrenheit pressione: 1\nFahrenheit para Celsius pressione: 2: "))
while (OP != 1 and OP != 2):
       OP = int(input("Número inváido, digite um válido:\nCelsius para Fahrenheit pressione: 1\nFahrenheit para Celsius pressione: 2: "))

if OP == 1:
	TC = float(input('Coloque o valor em celsius: '))
	TF = (((TC * 9)/5)+32)
	print(f'O valor {TC}°C convertido é {TF:.2f}°F')

elif OP == 2:
	TF = float(input('Coloque o valor em Fahrenheit: '))
	TC = (((TF - 32) * (5/9)))
	print(f'O valor {TF}°F convertido é {TC:.2f}°C')

