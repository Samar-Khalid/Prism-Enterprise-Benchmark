"""Synthetic data generator for enterprise benchmark."""

import csv
import json
import random
from datetime import datetime, timedelta
from typing import List, Dict


class SyntheticDataGenerator:
    """Generate synthetic manufacturing data."""
    
    def __init__(self, seed: int = 42):
        random.seed(seed)
        self.customers = []
        self.products = []
        self.orders = []
    
    def generate_customers(self, count: int = 500) -> List[Dict]:
        """Generate synthetic customers."""
        regions = ["Middle East", "Africa", "Asia", "Europe", "Americas"]
        industries = [
            "Manufacturing", "Construction", "Agriculture",
            "Mining", "Chemical", "Food & Beverage",
        ]
        
        for i in range(1, count + 1):
            customer = {
                "id": i,
                "name": f"Customer_{i:04d}",
                "email": f"customer{i}@example.com",
                "region": random.choice(regions),
                "industry": random.choice(industries),
                "credit_limit": round(random.uniform(10000, 500000), 2),
                "created_at": (
                    datetime.now() - timedelta(days=random.randint(30, 1000))
                ).isoformat(),
            }
            self.customers.append(customer)
        
        return self.customers
    
    def generate_products(self, count: int = 50) -> List[Dict]:
        """Generate synthetic products."""
        categories = {
            "Fertilizer": ["Urea", "DAP", "NPK", "Potash", "Ammonium Sulfate"],
            "Chemical": ["Sulfuric Acid", "Ammonia", "Nitric Acid"],
            "Raw Material": ["Phosphate Rock", "Potassium Chloride", "Limestone"],
        }
        
        for i in range(1, count + 1):
            category = random.choice(list(categories.keys()))
            product_type = random.choice(categories[category])
            
            product = {
                "id": i,
                "name": f"{product_type}_{i:03d}",
                "category": category,
                "unit_price": round(random.uniform(100, 2000), 2),
                "unit": random.choice(["ton", "kg", "liter", "bag"]),
                "min_stock": random.randint(10, 100),
                "max_stock": random.randint(500, 5000),
            }
            self.products.append(product)
        
        return self.products
    
    def generate_orders(
        self, count: int = 50000, start_date: str = "2023-01-01"
    ) -> List[Dict]:
        """Generate synthetic sales orders."""
        statuses = ["pending", "confirmed", "shipped", "delivered", "cancelled"]
        status_weights = [0.1, 0.2, 0.3, 0.35, 0.05]
        
        start = datetime.fromisoformat(start_date)
        
        for i in range(1, count + 1):
            order_date = start + timedelta(
                days=random.randint(0, 1000),
                hours=random.randint(8, 18),
                minutes=random.randint(0, 59),
            )
            
            order = {
                "id": i,
                "customer_id": random.randint(1, len(self.customers) or 500),
                "order_date": order_date.isoformat(),
                "status": random.choices(statuses, weights=status_weights)[0],
                "total_amount": round(random.uniform(1000, 100000), 2),
                "items_count": random.randint(1, 20),
            }
            self.orders.append(order)
        
        return self.orders
    
    def save_to_csv(self, data: List[Dict], filename: str) -> None:
        """Save data to CSV file."""
        if not data:
            return
        
        keys = data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    
    def save_to_json(self, data: List[Dict], filename: str) -> None:
        """Save data to JSON file."""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    """Generate all synthetic data."""
    generator = SyntheticDataGenerator()
    
    print("Generating customers...")
    customers = generator.generate_customers(500)
    generator.save_to_csv(customers, "data/synthetic/customers.csv")
    
    print("Generating products...")
    products = generator.generate_products(50)
    generator.save_to_csv(products, "data/synthetic/products.csv")
    
    print("Generating orders...")
    orders = generator.generate_orders(50000)
    generator.save_to_csv(orders, "data/synthetic/orders.csv")
    
    print(f"Generated {len(customers)} customers")
    print(f"Generated {len(products)} products")
    print(f"Generated {len(orders)} orders")
    print("Done!")


if __name__ == "__main__":
    main()
