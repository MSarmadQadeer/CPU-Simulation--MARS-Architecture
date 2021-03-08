from conversions import *

main_memory = {
    "0x100": "0001000100000100",
    "0x101": "0011000100000101",
    "0x102": "0100000100000110",
    "0x103": "0111000000000000",
    "0x104": "0000000000100011",
    "0x105": "1111111111101001",
    "0x106": "0000000000000000"
}


class CPU:
    def __init__(self):
        self.pc_tracker = 256
        self.PC = f"0x{decimal_to_hexa(self.pc_tracker)}"
        self.IR = ""
        self.MAR = ""
        self.MBR = ""
        self.AC = ""

    def load(self):
        self.get_operand()
        self.AC = self.MBR

    def store(self):
        main_memory[self.MAR] = hexa_to_binary(self.AC[2:])

    def add(self):
        self.get_operand()
        decimal_val_of_AC = hexa_to_decimal(self.AC[2:])
        decimal_val_of_MBR = hexa_to_decimal(self.MBR[2:])
        self.AC = f"0x{decimal_to_hexa(decimal_val_of_AC + decimal_val_of_MBR)}"

    def subtract(self):
        self.get_operand()
        decimal_val_of_AC = hexa_to_decimal(self.AC[2:])
        decimal_val_of_MBR = hexa_to_decimal(self.MBR[2:])
        self.AC = f"0x{decimal_to_hexa(decimal_val_of_AC - decimal_val_of_MBR)}"

    @staticmethod
    def halt():
        return -1

    def fetch(self):
        self.MAR = self.PC
        self.IR = main_memory[self.MAR]
        self.pc_tracker += 1
        self.PC = f"0x{decimal_to_hexa(self.pc_tracker)}"

    def get_operand(self):
        self.MBR = f"0x{binary_to_hexa(main_memory[self.MAR])}"

    def decode(self):
        instruction_table = {
            "0001": self.load,
            "0010": self.subtract,
            "0011": self.add,
            "0100": self.store,
            "0101": "input",
            "0110": "output",
            "0111": self.halt,
            "1000": "skipcond",
            "1001": "jump"
        }
        self.MAR = f"0x{binary_to_hexa(self.IR[4:])}"
        # noinspection PyAttributeOutsideInit
        self.operation = instruction_table[self.IR[0:4]]

    def execute(self):
        if self.operation() == -1:
            print("\n--- Program Ended ---")
            exit(0)

    def display(self):
        print(f"PC   = {self.PC}")
        print(f"IR   = {self.IR}")
        print(f"MAR  = {self.MAR}")
        print(f"MBR  = {self.MBR}")
        print(f"AC   = {self.AC}")


def main():
    cpu = CPU()
    print(f"\nState of Registers at start")
    cpu.display()

    i = 1
    while True:
        cpu.fetch()
        cpu.decode()
        cpu.execute()
        print(f"\nState of Registers after execution of {i} {'statements' if i > 1 else 'statement'}")
        cpu.display()
        i += 1


main()
