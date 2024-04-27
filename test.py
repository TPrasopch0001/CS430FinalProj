def read_input(file_name):
    with open(file_name, 'r') as file:
        file.seek(0)
        lines = file.readlines()
        num_items = int(lines[0])
        items = []
        for line in lines[1:]:
            item_info = line.strip().split()
            items.append((int(item_info[0]), float(item_info[1])))
        return num_items, items

def read_promotions(file_name):
    with open(file_name, "r") as file:
        file.seek(0)
        lines = file.readlines()
        num_promotions = int(lines[0])
        promotions = []
        for line in lines[1:]:
            promo_info = line.strip().split()
            promo = []
            if(int(promo_info[0]) > 1):
                for i in range(1, len(promo_info[0]), 2):
                    promo.append((int(promo_info[i]), int(promo_info[i+1])))
            else:
                promo.append((int(promo_info[1]), int(promo_info[2])))
            promotions.append(promo)
    return num_promotions, promotions

def calculate_min_payment(num_items, items, num_promotions, promotions):
    min_payment = float('inf')
    optimal_plan = []
    for promo in promotions:
        remaining_items = items.copy()
        payment = 0
        for p_id, p_amount in promo:
            for i, (item_id, item_price) in enumerate(remaining_items):
                if item_id == p_id:
                    amount_to_buy = min(p_amount, remaining_items[i][0])
                    payment += amount_to_buy * item_price
                    remaining_items[i] = (remaining_items[i][0] - amount_to_buy, item_price)
        for item_id, item_price in remaining_items:
            payment += item_id * item_price
        if payment < min_payment:
            min_payment = payment
            optimal_plan = promo
    return min_payment, optimal_plan

def write_output(file_name, min_payment, optimal_plan):
    with open(file_name, 'w') as file:
        file.write("Optimal Purchase Plan:\n")
        for item_id, amount in optimal_plan:
            file.write(f"Item ID: {item_id}, Amount: {amount}\n")
        file.write(f"Total Payment: {min_payment}\n")

def main():
    input_file = "input.txt"
    promotions_file = "promotions.txt"
    output_file = "output.txt"

    num_items, items = read_input(input_file)
    num_promotions, promotions = read_promotions(promotions_file)
    min_payment, optimal_plan = calculate_min_payment(num_items, items, num_promotions, promotions)
    write_output(output_file, min_payment, optimal_plan)

if __name__ == "__main__":
    main()