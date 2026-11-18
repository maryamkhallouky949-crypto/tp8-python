import csv
from datetime import datetime


class BatchProcessor:

    def __init__(self, csv_file, log_file):
        self.csv_file = csv_file
        self.log_file = log_file

        self.csv = None
        self.log = None

 

    def __enter__(self):

        try:
            
            self.csv = open(
                self.csv_file,
                "r",
                encoding="utf-8",
                newline=""
            )

            
            self.log = open(
                self.log_file,
                "a",
                encoding="utf-8"
            )

            self.ecrire_log("Début du traitement.")

            print("Fichiers ouverts avec succès.")

            return self

        except OSError as e:

            print("Erreur lors de l'ouverture :", e)

            if self.csv is not None:
                self.csv.close()
                self.csv = None

            if self.log is not None:
                self.log.close()
                self.log = None

            raise


    def ecrire_log(self, message):

        try:
            date = datetime.now()

            self.log.write(
                f"[{date}] {message}\n"
            )

            self.log.flush()

        except OSError as e:

            print("Erreur d'écriture dans le journal :", e)
            raise


    def traiter(self):

        try:

            lecteur = csv.DictReader(self.csv)

            for ligne in lecteur:

                operation = ligne["operation"]

                print("Traitement :", operation)

                self.ecrire_log(
                    "Traitement de l'opération : " + operation
                )

             
                resultat = operation.upper()

                print("Résultat :", resultat)

            self.ecrire_log("Fin du traitement des opérations.")

        except (OSError, csv.Error, KeyError) as e:

            self.ecrire_log(
                "Erreur pendant le traitement : " + str(e)
            )

            print("Erreur de traitement :", e)

            raise


    def __exit__(self, exc_type, exc_value, traceback):

        try:

            if exc_type is not None:

                self.ecrire_log(
                    "Traitement interrompu par une erreur : "
                    + str(exc_value)
                )

            else:

                self.ecrire_log(
                    "Traitement terminé normalement."
                )

        finally:

            if self.csv is not None and not self.csv.closed:
                self.csv.close()
                print("Fichier CSV fermé.")

            
            if self.log is not None and not self.log.closed:
                self.log.close()
                print("Fichier journal fermé.")

       
        return False




print(" DEBUT DU PROGRAMME ")

try:

    with BatchProcessor(
        "operations.csv",
        "journal.log"
    ) as processor:

        processor.traiter()

except (OSError, csv.Error, KeyError) as e:

    print("Une erreur a été détectée :", e)

print(" FIN DU PROGRAMME ")