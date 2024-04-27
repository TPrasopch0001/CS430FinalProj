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

def checkOffer(offer: Tuple[int,int],cost, items: list[Tuple[int,int]]):
    total_cost = 0
    items_list = [tuple(item) for item in items]
    if len(items_list) == 0:
        return 0
    else:
        for pair in items_list:
                print('Pair: {}'.format(pair))
                if pair[0] == offer[0]:
                    if pair[1] - offer[1] > 0:
                        newPair = (pair[0],(pair[1] - offer[1]))
                        items_list.remove(tuple(pair))
                        items_list.append(newPair)
                        print("offer remaining: {} ".format(items_list))
                        total_cost += cost
                    elif pair[1] - offer[1] == 0:
                        items_list.remove(tuple(pair))
                        print("offer completes: {} ".format(items_list))
                        total_cost += cost
    return total_cost, items_list

checkOffer((7,1),2, ((7, 1), (8, 1)))

def get_plan(total_items: int, items: list[Tuple[int, int]]):

    # check if result is in cache i.e. already computed
    if tuple(items) in cache:
        return cache[tuple(items)]

    # calculate value of items
    items_list = [tuple(item) for item in items]
    print("Item list: {}".format(items_list))
    total_cost = 0

    if len(items_list) == 0:
        return 0
    else:
        for offer, cost in offers.items():
            payment = 0
            remaining_items = items_list.copy()
            print("current offer: {}, current item list: {}".format(offer,items_list))
            if isinstance(offer[0], int):
                for i, pair in enumerate(items_list):
                    if pair[0] == offer[0]:
                        amount_to_buy = min(offer[1], pair[1])
                        payment += amount_to_buy * offers(offer)
                        remaining_items[i] = 
            else:
                if(checkMultiOffer(items_list, offer)):
                    for offerItem in offer:
                        for pair in items_list:
                            if pair[1] - offerItem[1] > 0:
                                newPair = (pair[0],(pair[1] - offerItem[1]))
                                deltaItems = [tuple(items) for items in items_list]
                                deltaItems.remove(tuple(pair))
                                deltaItems.append(newPair)
                                print("multi offer remaining: {} ".format(deltaItems))
                                total_cost += cost
                            elif pair[1] - offerItem[1] == 0:
                                deltaItems = [tuple(items) for items in items_list]
                                deltaItems.remove(tuple(pair))
                                print("multi offer complete: {} ".format(deltaItems))
                                total_cost += cost
    cache[tuple(items)] = total_cost
    return cache[tuple(items)]

def checkMultiOffer(items: list[Tuple[int,int]], offers: list[Tuple[int,int]]):
    return is_sublist(offers, items)

def is_sublist(A, B):
    if not A:
        return True
    if not B:
        return False
    if A[0] == B[0]:
        return is_sublist(A[1:], B[1:])
    return is_sublist(A, B[1:])

# print(get_plan(2, ((7, 0), (8, 0))))
#print(get_plan(2, ((7, 3), (8, -1))))
# print(get_plan(2, ((7, 3), (8, 1))))
# print(get_plan(2, ((7, 3), (8, 2))))
# print(get_plan(2, ((7, 1), (8, 1))))
