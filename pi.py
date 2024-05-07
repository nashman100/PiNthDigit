import decimal
# This solution uses the Chudnovsky Algorithm
def compute_pi(n):
    decimal.getcontext().prec = n + 1

    C = 426880 * decimal.Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, n):
        M = (K**3-16*K)*M//i**3
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
        K += 12

    pi = C/S
    return pi


def main():
    while True:
        user_input = input('Enter number of digits: ')
        try:
            num_digits = int(user_input)
            if num_digits < 1:
                print("Please enter a number that is greater than 0.")
                continue
            if num_digits > 100:
                print('Maximum number of digits limit is exceeded! Setting digits to 100 decimal places.')
                num_digits = 100
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    pi_calc = compute_pi(num_digits)

    print(f"Pi to {num_digits} decimal places is {pi_calc}")


if __name__ == '__main__':
    main()

