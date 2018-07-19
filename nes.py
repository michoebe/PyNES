from cpu import CPU
from rom import ROM


class NES(object):
    def __init__(self):
        self.cpu = CPU()
        self.rom = ROM()

    def load_rom(self, rom_path):
        with open(rom_path, 'rb') as f:
            self.rom.load_rom(f.read())

    def start(self):
        for instruction in self.rom.PRG_ROM:
            self.cpu.process_instruction(instruction)
