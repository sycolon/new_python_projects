import sqlite3

#db_name = "bibliothek.db"

def get_connection(db_name = "bibliothek.db"):
        return sqlite3.connect(db_name)

def initialisiere_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS buecher(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    gelesen INTEGER DEFAULT 0
                    )
        """)
        #conn.commit()

#bibliothek.db
    #table: buecher
        # id: INTEGER A. P.S.
        # title: Text
        # autor: TEXT
        #  gelesen: 0 für nein, 1 für ja


def buch_hinzufuegen(titel, autor):
    """Fügt ein neues Buch zur Datenbank hinzu."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO buecher (title, autor) VALUES (?,?)",(titel,autor))
        
        print(f"Buch '{titel}' würde hinzugefügt. ")


def bibliothek_zeigen():
    """Liest alle Bücher aus und druckt sie aus."""
    print("\n------ Mini Bibliothek ------")
    
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM buecher")
        result = cursor.fetchall()

        if not result:
            print("Die Mini-Bib ist noch leer")
        else:
            for id, title, autor, gelesen in result:
                print(f"[{id}] {"Gelesen" if gelesen else "Noch nicht gelesen"} {title}-{autor}")
        

def als_gelesen_markieren(buch_id):
    """Setze den Status gelsen auf 1 für eine bestimmte ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE buecher SET gelesen =1 WHERE id = ?",(buch_id,))

        if cursor.rowcount > 0:
            print(f"Buch ID {buch_id} als gelesen markiert.")
        else:
            print(f"Kein Buch mit ID {buch_id} gefunden.")

def buch_loeschen(buch_id):
    """Löcht ein Buch anhand seiner ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM buecher WHERE id = ?",(buch_id,))
        print(f"Buch ID {buch_id} wurde gelöscht.")



if __name__== "__main__":
    initialisiere_db()

    buch_hinzufuegen("Der Alchemist","Paulo Coilo")
    buch_hinzufuegen("Der alte Mann und das Meer","Ernest Hemingway")
    buch_hinzufuegen("The Red Book","Carl Gostav")

    bibliothek_zeigen()
    
    als_gelesen_markieren(1)

    bibliothek_zeigen()

    buch_loeschen(2)

    bibliothek_zeigen()