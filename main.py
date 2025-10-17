# 从键盘获取输入的一行字符
input_str = input()
# 初始化英文字符、数字、空格、其他字符的计数为 0
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0
# 遍历输入字符串中的每个字符
for char in input_str:
    # 如果字符是英文字母（包括大小写）
    if char.isalpha():
        letter_count += 1
    # 如果字符是数字
    elif char.isdigit():
        digit_count += 1
    # 如果字符是空格
    elif char.isspace():
        space_count += 1
    # 否则为其他字符
    else:
        other_count += 1
# 按照要求的格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
