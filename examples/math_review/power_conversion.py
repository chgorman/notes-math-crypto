#!/usr/bin/env python3

import math as m

power_list = [10, 100, 1000]

print("Approximate Power Conversion")
print("#"*72)
print()

for k in power_list:
    print("    %4d ~ 2**(%2.1f)" % (k, m.log2(k)))

two_power = 86
ten_power_total = two_power*m.log10(2)
exponent = int(ten_power_total)
base = 10.0**(ten_power_total - exponent)
print()
print(" 2**(%d) ~ %1.1f*10**(%d)" % (two_power, base, exponent))

ten_power = 86

print()
print("10**(%d) ~ 2**(%3.1f)" % (ten_power, ten_power*m.log2(10)))
