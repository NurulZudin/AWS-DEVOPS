# def convert(decimal_num):
#     roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
#     num_to_roman = ''
#     for i in roman.keys():
#         num_to_roman += roman[i]*(decimal_num//i)
#         decimal_num %= i 
#     return num_to_roman



# def convert_to_roman(num):
#     roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
#     number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     romanvalue = ''
#     for i,d in enumerate(number):
#         while (num >= d): 
#             num -= d
#             romanvalue += roman[i]
#     return romanvalue

# print(convert_to_roman(3557))

A = '?435'
print(A.isnumeric())
