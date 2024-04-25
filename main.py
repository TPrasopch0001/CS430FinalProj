from typing import List, Tuple


# itemID -> price
price = {7: 2, 8: 5}

# All 2-tuples are read as: (itemID, quantity)
# ((itemID, qty), ... ) -> price
promos = {
    ((7, 3), (8, 2)): 10,
    (7, 3): 5,
}

cache = {}


def get_plan(total_items: int, items: Tuple[Tuple[int, int], ...]):

    # check if any quantity is negative
    completed_items = 0
    for _, qty in items:
        if qty < 0:
            return 0
        if qty == 0:
            completed_items += 1

    # check if all quantities are 0 i.e. we don't need to buy anything
    if completed_items == total_items:
        return 0

    # check if result is in cache i.e. already computed
    if items in cache:
        return cache[items]

    # calculate value of items


print(get_plan(2, ((7, 0), (8, 0))))
print(get_plan(2, ((7, 3), (8, -1))))
print(get_plan(2, ((7, 3), (8, 1))))
