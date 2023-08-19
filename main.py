import math
import decimal
from fractions import  Fraction
from decimal import Decimal, ROUND_HALF_UP
from collections import defaultdict, deque
import sys

math.log(sys.maxsize, 2)
print(sys.int_info)
mt = math.frexp(8.066E+67)
print(mt)
# (bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)


tax_rate = Decimal("7.25")/Decimal(100)
purchase_amount = Decimal("2.95")
penny = Decimal("0.01")
ts = tax_rate * purchase_amount
print(ts)


total_amount  = purchase_amount + tax_rate * purchase_amount
tty = total_amount.quantize(penny)
tt = total_amount.quantize(penny, decimal.ROUND_UP)
print(tt)
print(tty)



sugar_cups = Fraction("2.5")
scale_factor = Fraction(5/8)
total_sugar = sugar_cups * scale_factor
print(total_sugar)


print((19/155) * (155/19))

answer = (19/155)*(155/19)
print(round(answer )) # 1-answer

inps = float(total_amount)
print(inps)
inp = float(sugar_cups * scale_factor)
print(inp)

print(8.066e+67)
# (87862989090 / (2**43))*(2**344)




# seconds
total_seconds = 7385
hours = total_seconds/3600 # //
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds  = divmod(remaining_seconds, 60) # // 60
# seconds = remaining_seconds%60
print("{}:{}:{}".format(hours , minutes ,minutes)) #seconds ) )
print(round(hours, 4))


# fractions
total_seconds = Fraction(7385)
hours = total_seconds/ 3600 # int(total_seconds /Fraction('3600'))
print(f"hours",{hours})
