def find_max_pizza_part():
    first_line = input().split()

    pizza_count = int(first_line[0])
    people_count = int(first_line[1])

    max_pizza_parts = 0
    pizza_parts = []

    for _ in range(pizza_count):
        current_pizza_parts = int(input())

        if current_pizza_parts > max_pizza_parts:
            max_pizza_parts = current_pizza_parts

        pizza_parts.append(current_pizza_parts)

    min = 0
    max = max_pizza_parts

    max_parts_per_human = 0

    while min <= max:
        mid = (min + max) // 2  # mid is how many parts does everyone get

        people_able_to_be_fed = (
            sum(parts // mid for parts in pizza_parts) if mid > 0 else 0
        )

        if people_able_to_be_fed >= people_count:
            max_parts_per_human = mid
            min = mid + 1

        else:
            max = mid - 1

    leftovers = sum(pizza_parts) - (people_count * max_parts_per_human)

    print(max_parts_per_human)
    print(leftovers)


if __name__ == "__main__":
    find_max_pizza_part()
