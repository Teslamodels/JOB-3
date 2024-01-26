# Algorithm Questions


# SAVOL

# X ning manfiy bo'lmagan butun soni berilgan bo'lsa, x ning kvadrat ildizini eng yaqin butun songa aylantiring. Qaytarilgan butun son ham manfiy bo'lmasligi kerak.

# Hech qanday o'rnatilgan ko'rsatkich funksiyasi yoki operatoridan foydalanmasligingiz kerak.

# Masalan, c++ da pow(x, 0,5) yoki pythonda x ** 0,5 dan foydalanmang.

# 1-misol:

# Kirish: x = 4
# Chiqish: 2
# Izoh: 4 ning kvadrat ildizi 2 ga teng, shuning uchun biz 2 ni qaytaramiz.


# 2-misol:

# Kirish: x = 8
# Chiqish: 2
# Izoh: 8 ning kvadrat ildizi 2,82842... va biz uni eng yaqin butun songa yaxlitlaganimiz uchun 2 qaytariladi.


# YECHIM

# from math import *
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         a = sqrt(x)
#         return floor(a)

# solution1 = Solution()
# print(solution1.mySqrt(8))
