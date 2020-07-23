def fib_even(n):
    number_0 = 0
    number_1 = 1

    fib_list = list()

    if n == 0:
        return "The sequence is empty"

    if n == 1:
        return number_0

    fib_list.append(number_0)
    while len(fib_list) < n:
        n_temp = number_0 + number_1
        number_0 = number_1
        number_1 = n_temp

        if number_1 % 2 == 0:
            fib_list.append(number_1)

    return fib_list


if __name__ == "__main__":
    fibonacci_count = int(input("Please, input how much even fibonacci number do you want to return --> "))
    print(fib_even(fibonacci_count))
