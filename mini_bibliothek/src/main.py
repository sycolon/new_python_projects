from api import BibliothekDB, Buch

db = BibliothekDB()

buch1= Buch(titel="Der Alchemist",autor="Paulo Coilo")
buch2 = Buch(titel="Der alte Mann und das Meer",autor="Ernest Hemingway")
buch3 = Buch(titel="The Red Book",autor="Carl Gostav")

db.speichern(buch1)
db.speichern(buch2)
db.speichern(buch3)

meiner_buecher = db.alle_laden()

for b in meiner_buecher:
    print(b)

db.markiere_als_gelesen(buch2)

print("-"*30)

meiner_buecher = db.alle_laden()

for b in meiner_buecher:
    print(b)