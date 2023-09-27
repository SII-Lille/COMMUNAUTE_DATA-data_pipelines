import duckdb
import random
import json
import pandas as pd
from datetime import date
from pydantic import BaseModel, ValidationError, Field
from typing import Optional

class SaleItem(BaseModel):
    product_id: str
    store_id: str
    date: date
    sales: Optional[float] = Field(...)
    revenue: Optional[float] = Field(...)
    stock: Optional[float] = Field(...)
    price: Optional[float] = Field(...)

if __name__ == "__main__":
    con = duckdb.connect(database='../duckdb/sales_bdd.duckdb', read_only=False)

    con.execute(
        'CREATE TABLE IF NOT EXISTS Sales('
        'product_id VARCHAR(50),'
        'store_id VARCHAR(50),'
        'date DATE,'
        'sales FLOAT,'
        'revenue FLOAT,'
        'stock FLOAT,'
        'price FLOAT)'
    )

    for i in range(1, 13):
        df = pd.read_csv(f'../dataset/sales_{i:02d}_2019.csv')
        result = df.to_json(orient="records")
        dict_sales = json.loads(result)

        random.shuffle(dict_sales)

        try:
            nb_rows = 0
            limit_rows = 10000
            for item in dict_sales:
                if nb_rows == limit_rows:
                    break
                else:
                    SaleItem(**item)

                    con.execute(
                        'INSERT INTO Sales VALUES (?, ?, ?, ?, ?, ?, ?)',
                        (
                            item["product_id"],
                            item["store_id"],
                            item["date"],
                            item["sales"],
                            item["revenue"],
                            item["stock"],
                            item["price"]
                        )
                    )

                    nb_rows += 1
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except Exception as e:
            print(f"Error inserting data: {e}")

    con.close()


