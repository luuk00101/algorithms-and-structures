def generate_layer(
    layer: int, number: list[int], used_nums: list[int], n: int, k: int
) -> None:
    if layer == n:
        print(number)
        return

    for num in range(1, k + 1):
        if (used_nums[num - 1]) == 1:
            continue

        number[layer] = num

        used_nums[num - 1] = True
        generate_layer(layer + 1, number, used_nums, n, k)
        used_nums[num - 1] = False


def generate_number_without_repetition(n: int, k: int) -> None:
    """
    Print the numbers of length n with each digit going from 1-k

    Parameters:
    n (int): Number length
    k: (int): Digit upper bound

    Raises:
    ValueError: If n > k - cannot generate any
    ValueError: If n or k are negative
    """

    if n > k:
        raise ValueError("Cannot generate numbers! Must have options >= places!")
    if n < 0 or k < 0:
        raise ValueError("Both length and upper bound must be positive!")

    generate_layer(0, [1] * n, [False] * k, n, k)


if __name__ == "__main__":
    try:
        places = int(input("Input number of places to generate: "))
        upper_bound = int(input("Input the upper number bound: "))
        generate_number_without_repetition(places, upper_bound)
    except ValueError as e:
        print(e)
