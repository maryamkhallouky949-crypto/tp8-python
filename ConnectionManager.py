from datetime import datetime
from contextlib import ExitStack




class ConnectionManager:

    def __init__(self, service_name):
        self.service_name = service_name

    def __enter__(self):

        print(
            f"[{datetime.now()}] "
            f"Connexion à {self.service_name} établie."
        )

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print(
            f"[{datetime.now()}] "
            f"Déconnexion de {self.service_name}."
        )

        if exc_type:
            print(
                f"Erreur détectée : "
                f"{exc_type.__name__} — {exc_value}"
            )

        return False


print(" PARTIE 2 ")

with ExitStack() as stack:

    log = stack.enter_context(
        open("log.txt", "a", encoding="utf-8")
    )

    conn = stack.enter_context(
        ConnectionManager("Serveur X")
    )

    log.write(
        f"[{datetime.now()}] "
        f"Tâche effectuée sur {conn.service_name}\n"
    )

print("Fin de la tâche.")



print(" PARTIE 3")

try:

    with ExitStack() as stack:

        log = stack.enter_context(
            open("log.txt", "a", encoding="utf-8")
        )

        conn = stack.enter_context(
            ConnectionManager("Base Y")
        )

        log.write(
            f"[{datetime.now()}] "
            f"Traitement de la base Y commencé.\n"
        )

        raise RuntimeError("Erreur de traitement")

except RuntimeError as e:

    print("Exception récupérée :", e)

print("Programme terminé.")