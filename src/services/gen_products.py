import random
from schemas.data_schemas import ProductSchema, StockInfo
from datetime import datetime, timezone

CATEGORIES = [
    ("CAF", "Café Especial", ["Huila", "Antioquia", "Quindío", "Nariño", "Sierra Nevada"], ["250g", "500g", "1kg"]),
    ("TEC", "Teclado Mecánico", ["Switch Red", "Switch Blue", "Switch Brown", "Inalámbrico", "60% Compacto"], ["Negro", "Blanco", "Gris"]),
    ("MOU", "Mouse Ergonómico", ["Óptico Pro", "Vertical", "Inalámbrico", "Gaming RGB", "Silencioso"], ["Negro", "Blanco"]),
    ("AUD", "Audífonos", ["Cancelación Ruido", "Studio Monitor", "Bluetooth", "In-Ear", "Diadema"], ["Negro", "Plata", "Azul"]),
    ("MON", "Monitor IPS", ["24 Pulgadas", "27 Pulgadas", "32 Curvo", "4K UHD", "144Hz Gaming"], ["Negro"]),
    ("MOC", "Mochila Antirrobo", ["Laptop 15\"", "Laptop 17\"", "Impermeable", "Ejecutiva", "Viaje"], ["Gris", "Negro", "Azul Marino"]),
    ("TER", "Termo Acero", ["500ml", "750ml", "1 Litro", "Térmico Café", "Deportivo"], ["Mate", "Acero", "Verde"]),
]

WAREHOUSES = ["bogota", "medellin", "cali"]


def generate_products(count: int = 100) -> list[dict]:
    products_to_insert = []
    index = 1

    while len(products_to_insert) < count:
        prefix, base_name, variants, presentations = random.choice(CATEGORIES)
        variant = random.choice(variants)
        presentation = random.choice(presentations)

        sku = f"{prefix}-{index:04d}"
        name = f"{base_name} {variant} ({presentation})"
        price = round(random.uniform(25000, 950000), -2) 

        
        by_warehouse = {
            wh: random.randint(0, 60)
            for wh in random.sample(WAREHOUSES, k=random.randint(1, len(WAREHOUSES)))
        }
        total_stock = sum(by_warehouse.values())

       
        product = ProductSchema(
            sku=sku,
            name=name,
            price=price,
            stock=StockInfo(
                total=total_stock,
                min_alert=random.choice([5, 10, 15]),
                by_warehouse=by_warehouse,
            ),
            updated_at=datetime.now(timezone.utc),
        )

       
        products_to_insert.append(product.model_dump(by_alias=True, exclude_none=True))
        index += 1

    return products_to_insert