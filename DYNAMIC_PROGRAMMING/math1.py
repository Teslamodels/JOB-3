# Algorithm Questions


# SAVOL
# X butun soni berilgan bo'lsa, agar x palindrom bo'lsa rost, aks holda noto'g'ri qiymatini qaytaring.

# 1-misol:

# Kirish: x = 121
# Chiqish: rost
# Izoh: 121 chapdan o'ngga va o'ngdan chapga 121 deb o'qiladi.


# 2-misol:

# Kirish: x = -121
# Chiqish: noto'g'ri
# Izoh: Chapdan o'ngga qarab -121 deb o'qiladi. O'ngdan chapga 121- bo'ladi. Shuning uchun u palindrom emas.


# 3-misol:

# Kirish: x = 10
# Chiqish: noto'g'ri
# Tushuntirish: 01 ni o'ngdan chapga o'qiydi. Shuning uchun u palindrom emas.



# YECHIM

# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         if strs[0][0:2] == strs[1][0:2] == strs[2][0:2]:
#             return strs[0][0:2]
#         return ""
# solution1 = Solution()
# print(solution1.longestCommonPrefix(["flower","flow","flight"]))