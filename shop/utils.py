from typing import Union, List

class CalculateMoney:
    def sum_price_count(self, price: Union[float, int], count: Union[float, int], discount: int = None) -> float:
        result = round(count * price, 2)
        if discount is not None:
            result = round(result * (1 - (discount / 100)), 2)
        return result

    def sum_price(self, prices: List[Union[float, int]], discount: int = None) -> float:
        result = sum(prices)
        if discount is not None:
            result = round(result * (1 - (discount / 100)), 2)
        return result

def sum_price_count(price: Union[float, int], count: Union[float, int], discount: int = None) -> float:
    return CalculateMoney().sum_price_count(price, count, discount)

 