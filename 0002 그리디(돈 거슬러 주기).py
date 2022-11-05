# -*- coding: utf-8 -*-

import math

"돈 거슬러 주기"

n = 1670
count = 0

money_type = [1000, 500, 100, 50, 10]

for money in money_type:
    count += n // money
    n %= money

print(count)