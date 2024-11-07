import os
import django
import sqlite3
import sys
sys.path.append("/app")


# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from apps.pages.models import DreData

# Percorso relativo al file SQLite
#sqlite_file_path =

# Connessione al database SQLite
conn = sqlite3.connect(sqlite_file_path)
cursor = conn.cursor()

# Query per recuperare i dati dalla tabella dreapp_document e dreapp_documenttext
cursor.execute("""
    SELECT
        doc.id AS id,
        doc.date AS date,
        doc.doc_type AS type,
        doc.part AS part,
        doc.notes AS summary,
        text.text AS body
    FROM dreapp_document AS doc
    JOIN dreapp_documenttext AS text ON doc.id = text.document_id
""")

# Inserimento dei dati nella tabella dre_data in PostgreSQL tramite Django
for row in cursor.fetchall():
    DreData.objects.create(
        id=row[0],
        date=row[1],
        type=row[2],
        part=row[3],
        summary=row[4],
        body=row[5]
    )

# Chiudi la connessione a SQLite
conn.close()
print("Dati importati con successo nella tabella dre_data su PostgreSQL")