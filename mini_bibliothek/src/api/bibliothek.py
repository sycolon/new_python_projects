import sqlite3
from .buch import Buch

class BibliothekDB:

    def __init__(self, db_name="bibliothek.db"):
        self.db_name = db_name
        self._initialisiere_db()

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def _initialisiere_db(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS buecher(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titel TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        gelesen INTEGER DEFAULT 0
                        )
            """)
    
    def speichern(self,buch):
        """Fügt ein neues Buch zur Datenbank hinzu."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO buecher (titel, autor, gelesen) VALUES (?,?,?)",(buch.titel,buch.autor,buch.gelesen))
            buch.id = cursor.lastrowid
            #print(f"Buch '{buch.titel}' würde hinzugefügt. ")


    def alle_laden(self):
        """Liest alle Bücher aus und druckt sie aus."""
        print("\n------ Mini Bibliothek ------")
        
        buecher_liste = []
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM buecher")
            result = cursor.fetchall()

            if not result:
                print("Die Mini-Bib ist noch leer")
            else:
                for id, titel, autor, gelesen in result:
                    neues_buch = Buch(id,titel,autor,gelesen)
                    buecher_liste.append(neues_buch)
                    #print(f"[{id}] {"Gelesen" if gelesen else "Noch nicht gelesen"} {titel}-{autor}")
        return buecher_liste

    def markiere_als_gelesen(self,buch) -> str:
        """Setze den Status gelsen auf 1 für eine bestimmte ID."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE buecher SET gelesen =1 WHERE id = ?",(buch.id,))

            if cursor.rowcount > 0:
                return f"Buch ID {buch.id} als gelesen markiert."
            else:
                return f"Kein Buch mit ID {buch.id} gefunden."

    def buch_loeschen(self, buch):
        """Löcht ein Buch anhand seiner ID."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM buecher WHERE id = ?",(buch.id,))
            print(f"Buch ID {buch.id} wurde gelöscht.")