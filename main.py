meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "Leggera disapprovazione",
            "CREEPY": "Spaventoso,inquietante",
            "PARA": "Peoccuparsi per qualcosa,paranoiarsi",
            "BRO": "Amico",
            "FRA": "Amico",
            "SUS": "Sospetto, sospettoso"
            }
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
if parola in meme_dict.keys():
    print(meme_dict[parola])
else:
    print("La parola in questione non ce l abbiamo")
