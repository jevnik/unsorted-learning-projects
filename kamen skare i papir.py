import random as rand

print("Pozdrav, dobrodošli u igru kamen, skare i papir")

mogucnosti = ["kamen", "skare", "papir"]
odabir_ply = str(input("Upišite svoj odabir: "))
pobjeda_ply = "Pobjedili ste!"
pobjeda_ai = "računalo pobjeđuje"

if not odabir_ply in mogucnosti:
    print("morate odabrati jednu od tri moguće opcije: kamen, skare ili papir. Pokusajte ponovo")
    odabir_ply = str(input("Upišite svoj odabir: "))


print("vaš odabir je: " + odabir_ply)


odabir_ai = mogucnosti[rand.randint(0,2)]

print("Računalo je odabralo: " + odabir_ai)

if odabir_ply  == odabir_ai:
    print("Izjednaceno")
    quit()

if odabir_ply == "kamen" and odabir_ai == "papir":
    print(pobjeda_ai)
    quit()
elif odabir_ply == "kamen" and odabir_ai == "skare":
    print(pobjeda_ply)
    quit()
elif odabir_ply == "skare" and odabir_ai == "kamen":
    print(pobjeda_ai)
    quit()
elif odabir_ply == "skare" and odabir_ai == "papir":
    print(pobjeda_ply)
    quit()
elif odabir_ply == "papir" and odabir_ai == "kamen":
    print(pobjeda_ply)
    quit()
elif odabir_ply == "papir" and odabir_ai == "skare":
    print(pobjeda_ai)
    quit()   



