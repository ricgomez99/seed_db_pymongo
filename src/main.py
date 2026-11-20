import os
from dotenv import load_dotenv
from services.create_connection import create_connection
from services.seed_data import run_seed
from utils.print_table import print_table

load_dotenv()

URL = os.getenv('URL')
DB_NAME = 'inventory'

def main():
    if not URL:
        raise ValueError('URL not defined')
    db = create_connection(URL, DB_NAME)
    bogota_available_stock = list(db.products.find({
        'stock.by_warehouse.bogota': {'$gte': 20},
        'price': {'$lt': 500000}
    }).limit(5))

    average_prices = list(db.products.aggregate([
        {
            '$group': {
                '_id': None,
                'avgAmount': { '$avg': { '$multiply': ["$price", "$stock.total"] } },
                'avgQuantity': {'$avg': "$stock.total"}
            }
        }]))

    print_table(bogota_available_stock)
    print_table(average_prices)

if __name__ == '__main__':
    main()