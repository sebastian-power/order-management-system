import csv


class Products:
    def __init__(self) -> None:
        with open("../assets/data_files/products.csv", "r") as products:
            reader = csv.DictReader(products)
            self._products_dicts = [row for row in reader]
        self._products_string = [
            {
                f"{counter+1}. {'name':4}": f"{product['name']:25}",
                f"{'unit_price':10}": f"${int(product['unit_price']):4d}",
            }
            for counter, product in enumerate(self._products_dicts)
        ]

    ALL_PRODUCTS_F = [
        {f'1. {"name":4}': f'{"Pen":25}', f'{"unit_price":10}': f"${2:4d}"},
        {f'2. {"name":4}': f'{"Computer Disk":25}', f'{"unit_price":10}': f"${200:4d}"},
        {
            f'3. {"name":4}': f'{"Scientific Calculator":25}',
            f'{"unit_price":10}': f"${100:4d}",
        },
        {f'4. {"name":4}': f'{"Sun Glasses":25}', f'{"unit_price":10}': f"${300:4d}"},
    ]

    def get_attr(self, attr: str, item_id: int):
        return self._products_dicts[item_id-1][attr]

    def __str__(self) -> type[str]:
        star_line = "\n" + "-" * 100 + "\n"
        product_details = "Available products details are:\n" + "\n".join(
            map(str, self._products_string)
        )
        return star_line + product_details + star_line
