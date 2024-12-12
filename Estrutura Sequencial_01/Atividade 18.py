#18) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo_mb = float(input("Insira o tamanho para download do arquivo: ")) #megabytes
velocidade_mbps = float(input("Insira a velocidade de internet: ")) #megabits por segundo

#Cálculo para converter megabits por segundo em megabytes por segundo.
conversao_MBps = velocidade_mbps / 8

#Cálculo para calcular o tempo de download em segundos.
calculo_tempo_segundos = arquivo_mb / conversao_MBps

#Cálculo para converter o resultado em segundos em minutos.
conversao_minutos = calculo_tempo_segundos / 60

print(f"O tempo aproximado em minutos é de {conversao_minutos:.2f} minutos.")
