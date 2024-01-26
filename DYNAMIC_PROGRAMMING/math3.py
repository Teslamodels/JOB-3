# Algorithm Questions


# SAVOL

# Sizda string buyrug'ini sharhlay oladigan Goal Parser mavjud. Buyruq qandaydir tartibda "G", "()" va/yoki "(al)" alifbosidan iborat. Maqsad tahlilchisi "G"ni "G" qatori, "()" qatorini "o" va "(al)"ni "al" qatori sifatida izohlaydi. Keyin izohlangan satrlar asl tartibda birlashtiriladi.

# String buyrug'ini hisobga olgan holda, Goal Parserning buyruq talqinini qaytaring.


# 1-misol:

# Kirish: buyruq = "G()(al)"
# Natija: "Maqsad"
# Izoh: Maqsad tahlilchisi buyruqni quyidagicha izohlaydi:
# G -> G
# () -> o
# (al) -> al
# Yakuniy birlashtirilgan natija - "Gol".


# 2-misol:

# Kirish: buyruq = "G()()()()(al)"
# Chiqish: "Gooooal"
# 3-misol:

# Kirish: buyruq = "(al)G(al)()()G"
# Chiqish: "alGalooG"


# YECHIM

# class Solution:
#     def interpret(self, command: str) -> str:
#         return command.replace('()', 'o').replace('(', '').replace(')', '')
# solution1 = Solution()
# print(solution1.interpret("(al)G(al)()()G"))