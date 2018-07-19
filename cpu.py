class CPU(object):
    def __init__(self):
        self.registers = {
            'A': 0,  # Accumulator register
            'X': 0,  # Index register
            'Y': 0,  # Index register
            'PC': 0,  # Program counter
            'S': 0,  # Stack pointer
            'P': 0   # Status register
        }

    def process_instruction(self, instruction: bytes):
        print(instruction)
