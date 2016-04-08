# You have a function rand5() that generates a random integer from 1 to 5.
# Use it to write a function rand7() that generates a random integer from 1 to 7.
# rand5() returns each integer with equal probability.
# rand7() must also return each integer with equal probability.

# build possibility list to test theory

import random


def actual_solution_rand7():
    number = 27
    while number > 20:
        number = build_base_5_number()
    return (number % 7) + 1


def build_base_5_number():
    fives = (rand5() - 1) * 5
    ones = rand5() - 1
    number = fives + ones
    return number


def rand5():
    choose_from = [1, 2, 3, 4, 5]
    chosen = random.choice(choose_from)
    return chosen


print actual_solution_rand7()
print actual_solution_rand7()
print actual_solution_rand7()
print actual_solution_rand7()

# def determine_whether_equal_probability():
#     rand5 = [1, 2, 3, 4, 5]
#
#     product_of_2_rolls = []
#     product_of_3_rolls = []
#     product_of_4_rolls = []
#     product_of_5_rolls = []
#     product_of_6_rolls = []
#     product_of_7_rolls = []
#
#     for num1 in rand5:
#         for num2 in rand5:
#             product_of_2_rolls.append(num1*num2)
#
#     for num1 in rand5:
#         for num2 in product_of_2_rolls:
#             product_of_3_rolls.append(num1*num2)
#
#     for num1 in rand5:
#         for num2 in product_of_3_rolls:
#             product_of_4_rolls.append(num1*num2)
#
#     for num1 in rand5:
#         for num2 in product_of_4_rolls:
#             product_of_5_rolls.append(num1*num2)
#
#     for num1 in rand5:
#         for num2 in product_of_5_rolls:
#             product_of_6_rolls.append(num1*num2)
#
#     for num1 in rand5:
#         for num2 in product_of_6_rolls:
#             product_of_7_rolls.append(num1*num2)
#
#     two_rolls = determine_if_equal_prob(product_of_2_rolls)
#     three_rolls = determine_if_equal_prob(product_of_3_rolls)
#     four_rolls = determine_if_equal_prob(product_of_4_rolls)
#     five_rolls = determine_if_equal_prob(product_of_5_rolls)
#     six_rolls = determine_if_equal_prob(product_of_6_rolls)
#     seven_rolls = determine_if_equal_prob(product_of_7_rolls)
#
#     print two_rolls
#     print three_rolls
#     print four_rolls
#     print five_rolls
#     print six_rolls
#     print seven_rolls
#
#
# def determine_if_equal_prob(product_list):
#     all_mods = {}
#     for num in product_list:
#         mod7 = num%7
#         if mod7 in all_mods:
#             all_mods[mod7] += 1
#         else:
#             all_mods[mod7] = 1
#     if len(all_mods) > 7:
#         return "Error"
#     mods = all_mods.keys()
#     count = mods[0]
#     for i in range (1, len(mods)):
#         if mods[i] != count:
#             return False
#     return True
#
#
# determine_whether_equal_probability()
