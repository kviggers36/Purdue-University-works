import math


def cal_area_value(num2):
  return 3.14 * int(num2) ** 2


def sum_and_multi(sqrt_value, area_value):
  sum_result = float(sqrt_value) + float(area_value)
  product_result = float(sqrt_value) * float(area_value)
  return sum_result, product_result


def main():
 num1 = int(input("what is num1?:"))
 num2 = int(input("what is num2?:"))
 sqrt_value = math.sqrt(num1)
 area_value = cal_area_value(num2)
 answer1, answer2 = sum_and_multi(sqrt_value, area_value)
 print(f"The sum is {answer1}, and the product is {answer2}")


if __name__ == "__main__":
  main()


