import json

def calcular_estatisticas_faturamento(json_file):
    with open(json_file, 'r') as file:
        dados_faturamento = json.load(file)

    faturamento_diario = [dia['valor'] for dia in dados_faturamento]
    dias_faturamento = [faturamento for faturamento in faturamento_diario if faturamento > 0]
    
    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)
    media_mensal = sum(dias_faturamento) / len(dias_faturamento)

    dias_acima_media = sum(1 for faturamento in faturamento_diario if faturamento > media_mensal)

    return menor_valor, maior_valor, dias_acima_media

resultado = calcular_estatisticas_faturamento('dados.json')
print("Menor valor de faturamento:", resultado[0])
print("Maior valor de faturamento:", resultado[1])
print("Número de dias com faturamento acima da média mensal:", resultado[2])
