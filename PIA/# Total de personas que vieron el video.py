# Total de personas que vieron el video
espectadores = 20000000
# Segundos en una semana (7 días * 24 horas * 60 minutos * 60 segundos)
segundos_semana = 7 * 24 * 60 * 60

llamadas_por_segundo = espectadores / segundos_semana
print(f"Llamadas por segundo: {llamadas_por_segundo:.2f}")
