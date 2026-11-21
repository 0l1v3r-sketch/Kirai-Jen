# Densidad típica de una estrella de neutrones / neutronio: ~ 4e17 kg/m^3 a 1e18 kg/m^3
# Densidad nuclear saturada: ~ 2.3e17 kg/m^3

rho_min = 2.3e17 # kg/m^3
rho_avg = 4.0e17 # kg/m^3
rho_max = 1.0e18 # kg/m^3

# Volumen de 1 cm^3 = 1e-6 m^3
vol_cm3 = 1e-6
mass_cm3_min = rho_min * vol_cm3 / 1000 # en toneladas métricas
mass_cm3_avg = rho_avg * vol_cm3 / 1000
mass_cm3_max = rho_max * vol_cm3 / 1000

# Volumen de 1 cucharadita (5 cm^3 = 5e-6 m^3)
vol_tsp = 5e-6
mass_tsp_avg = rho_avg * vol_tsp / 1000
mass_tsp_max = rho_max * vol_tsp / 1000

print(f"1 cm3 (toneladas): {mass_cm3_min:,.0f} - {mass_cm3_max:,.0f} (promedio: {mass_cm3_avg:,.0f})")
print(f"1 cucharadita 5cm3 (toneladas): promedio {mass_tsp_avg:,.0f}, max {mass_tsp_max:,.0f}")