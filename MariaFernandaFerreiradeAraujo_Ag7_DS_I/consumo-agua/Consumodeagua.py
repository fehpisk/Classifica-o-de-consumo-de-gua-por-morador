#Entrada das informações
Imovel = input ("Informe o tipo do imovel (casa, comercial ou apartamento):")
Consumo = float (input ("Informe o consumo mensal de agua do imovel (em m³):"))

#Classificações
if Imovel == "comercial":
   print("Tarifa comercial aplicada - consulte o plano corporativo.")

elif Imovel == "apartamento" and Consumo < 10:
   print("Consumo econômico - excelente controle de água!")

elif Imovel == "apartamento" and Consumo <= 25 or (Imovel == "casa" and Consumo <= 25):
 print("Consumo moderado - dentro do padrão residencial.")

else: 
  print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")






