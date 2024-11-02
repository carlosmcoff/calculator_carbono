def calculoEmissaoCO2(km_distancia, potencia_motor, tipo_combustivel):
    # CO2 = (DISTANCIA * CONSUMO) / FATOR EMISSAO
    
    # Quanto gasta de combustível em litros de cada motor em média por KM rodado
    motor1_0_1_2 = 0.083 
    motor1_4_1_6 = 0.10
    motor1_8_2_0 = 0.125
    motor2_0acima = 0.167 

    # Liberação de kg CO2 de cada tipo de combustivel por litro gasto
    gasolina =  2.264
    diesel =  2.93
    etanol = 0.389
    eletricidadeBrasil = 0.084
    eletriciaMediaGlobal = 0.475

    distancia = int(km_distancia)

    motor = potencia_motor

    if motor == "1.0 a 1.2":
        consumo = motor1_0_1_2 * distancia

    if motor == "1.4 a 1.6":
        consumo = motor1_4_1_6 * distancia
        
    if motor == "1.8 a 2.0":
        consumo = motor1_8_2_0 * distancia
    
    if motor == "Acima de 2.0":
        consumo = motor2_0acima * distancia
        
    combustivel = tipo_combustivel

    if combustivel == "Gasolina":
        fatorEmissao = gasolina
        
    if combustivel == "Diesel":
        fatorEmissao = diesel

    if combustivel == "Etanol":    
        fatorEmissao = etanol

    if combustivel == "Elétrico":
        fatorEmissao = eletricidadeBrasil

    
    formula = consumo * fatorEmissao
    roundFormula = round(formula, 2)

    print(f"{roundFormula} kg de CO₂")

    return roundFormula


def creditosCO2():
    ...
    

