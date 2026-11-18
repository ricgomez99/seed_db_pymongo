from services.gen_products import generate_products
from pymongo.errors import BulkWriteError
from pymongo.database import Database

def run_seed(db: Database):
    documents = generate_products(100)
    try:
        result = db.products.insert_many(documents, ordered=False)
        print(f"Se insertaron {len(result.inserted_ids)} productos correctamente.")
        print(f"Ejemplo de ID generado: {result.inserted_ids[0]}")
    except BulkWriteError as exc:
        inserted = exc.details.get("nInserted", 0)
        print(f"Inserción parcial: {inserted} documentos nuevos insertados (algunos SKUs ya existían).")

        