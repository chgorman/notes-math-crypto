#!/usr/bin/env python3

from gmpy2 import mpfr

big_power = 1024
# 2**1024 will cause overflow when attempting to convert from int to float64

print("Approximate Size of 2**k")
print("#"*72)
print()

power_list = [32, 64, 128, 256, 512, 1024]
for k in power_list:
    if k < big_power:
        print("2**(%4d) = %.1e" % (k, 2.0**k))
    else:
        a = mpfr(2**k, 100)
        print("2**(%d) = %s" % (k, "{0:1.1e}".format(a)))

