import os
import sqlite3
from django.db import migrations
import datetime

def load_data(apps, schema_editor):
    # Import the DrePublication model for this migration
    DrePublication = apps.get_model('dre', 'DrePublication')
    DrePublicationType = apps.get_model('dre', 'DrePublicationType')
    
    DrePublication.objects.all().delete()
    DrePublicationType.objects.all().delete()

    # Define the path to your SQLite file
    sqlite_file_path = os.path.join(os.path.dirname(__file__), 'data/2024-10-27-DRE.sqlite3')

    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_file_path)
    cursor = conn.cursor()

    # SQL query to retrieve data from SQLite tables from year 2024
    cursor.execute("""
        SELECT
            doc.date AS date,
            doc.doc_type AS type,
            doc.part AS part,
            doc.notes AS summary,
            text.text AS body
        FROM dreapp_document AS doc
        JOIN dreapp_documenttext AS text ON doc.id = text.document_id
        WHERE doc.date >= '2024-01-01' AND doc.date < '2025-01-01'
    """)

    # Insert data into PostgreSQL using Django ORM in batches
    batch_size = 1000
    objects = []


    for row in cursor.fetchall():
        current_type = DrePublicationType.objects.get_or_create(name=row[1])[0]
        
        objects.append(
            DrePublication(
                date=row[0],
                type=current_type,
                part=row[2],
                summary=row[3],
                body=row[4]
            )
        )

        if len(objects) >= batch_size:
            DrePublication.objects.bulk_create(objects)
            objects = []  # Clear the batch after insertion

    # Insert any remaining objects
    if objects:
        DrePublication.objects.bulk_create(objects)

    # Close the SQLite connection
    conn.close()
    print("Data successfully imported into the DrePublication table in PostgreSQL")
    
def clean_data(apps, schema_editor):
    # Import the DrePublication model for this migration
    DrePublication = apps.get_model('dre', 'DrePublication')
    
    DrePublication.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('dre', '0001_initial'),
    ]
    
    operations = [   
        migrations.RunPython(load_data, clean_data),
    ]