from pathlib import Path
from contextlib import contextmanager, ExitStack




class TempFileWriter:

    def __enter__(self):
        self.filepath = Path("temp.txt")
        self.f = self.filepath.open("w", encoding="utf-8")
        print("Ouverture du fichier temporaire.")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

        if self.filepath.exists():
            self.filepath.unlink()

        print("Fichier temporaire fermé et supprimé.")

        return False


print(" PARTIE 1 ")

with TempFileWriter() as f:
    f.write("Contenu temporaire\n")
    f.write("Deuxième ligne\n")




@contextmanager
def temp_file():

    path = Path("temp.txt")
    f = path.open("w", encoding="utf-8")

    print("Ouverture avec contextmanager.")

    try:
        yield f

    finally:
        f.close()

        if path.exists():
            path.unlink()

        print("Fichier fermé et supprimé.")


print(" PARTIE 2 ")

with temp_file() as f:
    f.write("Autre test\n")



print("PARTIE 3 ")

paths = ["a.txt", "b.txt", "c.txt"]

with ExitStack() as stack:

    files = []

    for p in paths:
        f = stack.enter_context(
            open(p, "w", encoding="utf-8")
        )
        files.append(f)

    for f in files:
        f.write("test\n")

print("Tous les fichiers ont été fermés.")