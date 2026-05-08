class Buch:
    def __init__(self, id = None, titel="", autor = "", gelesen = 0):
        self.id = id
        self.titel = titel
        self.autor = autor
        self.gelesen = gelesen
    
    def __str__(self):
        status = "Gelesen" if self.gelesen else "Noch nicht gelesen"
        return f"[{self.id}] {status} {self.titel}-{self.autor}"