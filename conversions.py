binary_to_hexa_map = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}


def binary_to_hexa(binary):
    """
    It will convert decimal number to binary
    :param binary:
    :return hexa:
    """

    def add_zeros(binary_num, flag):
        """
        It will convert decimal number to binary
        :param flag: 'right' / 'left'
        :param binary_num:
        :return updated binary:
        """
        remainder = len(binary_num) % 4
        adder = 0
        if remainder != 0:
            adder += 4 - remainder
        if flag == "left":
            return adder * "0" + binary_num
        if flag == "right":
            return binary_num + adder * "0"

    def convert_to_hexa(binary_num):
        """
        It will convert decimal number to binary
        :param binary_num:
        :return hexa_num:
        """
        hexa_num = ""
        start_index = 0
        end_index = 4
        while not end_index > len(binary_num):
            hexa_num += binary_to_hexa_map[binary_num[start_index: end_index]]
            start_index += 4
            end_index += 4
        return hexa_num

    # logic of the outer function starts here
    hexa = ""
    if binary.find(".") == -1:
        binary = add_zeros(binary, flag="left")
        hexa += convert_to_hexa(binary)
    else:
        dot_index = binary.find(".")
        int_binary = add_zeros(binary[0: dot_index], flag="left")
        fraction_binary = add_zeros(binary[dot_index+1:], flag="right")
        int_hexa = convert_to_hexa(int_binary)
        fraction_hexa = convert_to_hexa(fraction_binary)
        hexa += f"{int_hexa}.{fraction_hexa}"

    return hexa


def hexa_to_binary(hexa):
    """
    It will convert decimal number to binary
    :param hexa:
    :return binary:
    """
    binary = ""
    for i in hexa:
        if i == ".":
            binary += i
            continue
        for key in binary_to_hexa_map.keys():
            if binary_to_hexa_map[key] == i:
                binary += key
                break
    return binary


def binary_to_decimal(binary_num):
    """
    It will convert binary number to decimal
    :param binary_num:
    :return decimal_num:
    """
    decimal_num = 0
    power = binary_num.index(".") - 1 if binary_num.find(".") != -1 else len(binary_num) - 1
    for i in binary_num:
        if i == ".":
            continue
        decimal_num += int(i) * 2 ** power
        power -= 1
    return decimal_num


def decimal_to_binary(decimal_num):
    """
    It will convert decimal number to binary
    :param decimal_num:
    :return binary_num:
    """
    int_decimal = int(decimal_num)
    fraction_decimal = decimal_num - int_decimal
    int_binary = ""
    while int_decimal != 0:
        int_binary = str(int_decimal % 2) + int_binary
        int_decimal = int(int_decimal / 2)
    fraction_binary = ""
    while fraction_decimal != 0:
        fraction_decimal *= 2
        int_part = int(fraction_decimal)
        fraction_decimal -= int_part
        fraction_binary += str(int_part)

    binary_num = int_binary if fraction_binary.find("1") == -1 else f"{int_binary}.{fraction_binary}"
    return binary_num


def hexa_to_decimal(hexa):
    """
    It will convert decimal number to binary
    :param hexa:
    :return decimal:
    """
    key_value = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    decimal = 0
    power = len(hexa) - 1
    for i in hexa:
        try:
            decimal += key_value[i]*16**power
        except KeyError:
            decimal += int(i)*16**power
        power -= 1
    return decimal


def decimal_to_hexa(decimal):
    """
    It will convert decimal number to binary
    :param decimal:
    :return hexa:
    """
    key_value = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    hexa = ""
    while decimal != 0:
        remainder = decimal % 16
        decimal = int(decimal / 16)
        try:
            hexa = key_value[remainder] + hexa
        except KeyError:
            hexa = str(remainder) + hexa
    return hexa
