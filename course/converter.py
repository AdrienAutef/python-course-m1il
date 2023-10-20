vitesse_kmh = float(input("Entrez la vitesse en kilomètres par heure (km/h) : "))
vitesse_mph = vitesse_kmh * 0.621371
vitesse_mph_arrondie = round(vitesse_mph, 2)
print(f"La vitesse est d'environ {vitesse_mph_arrondie} milles par heure (mph).")