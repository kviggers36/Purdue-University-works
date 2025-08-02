import math


def decimal_addition(decimal1,decimal2):
    return float(decimal1) + float(decimal2)


def calc_simp_inter(p,r,t):
    return int(p) * float(r) * int(t)


def c_to_f(c):
    fahrenheit = (int(c)* 1.8) + 32.
    return fahrenheit


def main():
    decimal1 = float(input("enter your first number: "))
    decimal2 = float(input("enter your second number:"))
    answer = decimal_addition(decimal1,decimal2)
    print (f"the sum is {answer}.")
    p = int(input("what is your princple amount: "))
    r = float(input("what is your rate of interest: "))
    t = int(input("what is your time in years: "))
    answer = calc_simp_inter(p,r,t)
    print(f" the overalll total is ${answer}.")
    c = input("what is your temp?: ")
    answer = c_to_f(c)
    print(f"{c} equals to {answer} degrees in fahrenheit")


if __name__ == "__main__":
    main()
