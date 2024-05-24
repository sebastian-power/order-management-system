import csv
from pathlib import Path


class Products:
    def __init__(self) -> None:
        products_path = [i for i in Path(__file__).resolve().parents][2].joinpath(
            str(Path("assets/data_files/products.csv"))
        )
        with open(str(products_path), "r") as products:
            reader = csv.DictReader(products)
            self._products_dicts = [row for row in reader]
        self._products_string = [
            {
                f"{counter+1}. {'name':4}": f"{product['name']:25}",
                f"{'unit_price':10}": f"${int(product['unit_price']):4d}",
            }
            for counter, product in enumerate(self._products_dicts)
        ]

    def get_attr(self, attr: str, item_id: int):
        return self._products_dicts[item_id - 1][attr]

    def __str__(self) -> type[str]:
        star_line = "\n" + "-" * 100 + "\n"
        product_details = "Available products details are:\n" + "\n".join(
            map(str, self._products_string)
        )
        return star_line + product_details + star_line
