from typing import List, Tuple


# itemID -> price
# price = {7: 2, 8: 5}

# All 2-tuples are read as: (itemID, quantity)
# ((itemID, qty), ... ) -> price
offers = {
    (7, 1): 2,
    (8, 1): 5,
    ((7, 3), (8, 2)): 10,
    (7, 3): 5,
}

cache = {}


def get_plan(total_items: int, items: List[Tuple[int, int]]):

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
    if tuple(items) in cache:
        return cache[tuple(items)]

    # calculate value of items
    items = [list(item) for item in items]
    bill = 0

    # iterate over every purchase we can make (promos or individual items)
    for offer, cost in offers.items():
        # if it is just the price of a single item i.e. a single tuple with 2 integers e.g. (7,1)
        if isinstance(offer[0], int):
            for i, item in enumerate(items):
                if item[0] == offer[0] and item[1] > 0:
                    items[i] = [item[0], item[1] - offer[1]]
                    bill += cost

        # if it is a promotion including multiple items i.e. a tuple of tuples e.g. ((7,3), (8,2), ...)
        else:
            for pair in offer:
                for i, item in enumerate(items):
                    if item[0] == pair[0] and item[1] > 0:
                        items[i] = [item[0], item[1] - pair[1]]
                        bill += cost

    cache[tuple(items)] = bill
    return cache[items]


# print(get_plan(2, ((7, 0), (8, 0))))
# print(get_plan(2, ((7, 3), (8, -1))))
# print(get_plan(2, ((7, 3), (8, 1))))
print(get_plan(2, ((7, 3), (8, 2))))
