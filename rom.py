HEADER_SIZE = 16
KB = 1024

class ROM(object):
    def __init__(self):
        self.rom_content = None
        self.header = {             # https://wiki.nesdev.com/w/index.php/INES
            'Magic': None,          # 0-3, Constant $4E $45 $53 $1A ("NES" followed by MS-DOS end-of-file)
            'Size_PRG_ROM': None,   # 4, Size of PRG ROM in 16 KB units
            'Size_CHR_ROM': None,   # 5, Size of CHR ROM in 8 KB units (Value 0 means the board uses CHR RAM)
            '6': None,              # Flag 6
            '7': None,              # Flag 7
            'Size_PRG_RAM': None,   # 8, Size of PRG RAM in 8 KB units (Value 0 infers 8 KB for compatibility
            '9': None,              # 9
            '10': None,             # 10
        }                           # 11-15: Zero filled

        self.PRG_ROM = None  # The instructions, connected to CPU
        self.CHR_ROM = None  # The sprites etc, connected to PPU

    def load_rom(self, rom_content):
        # First read in the ROM header
        self.rom_content = rom_content
        self.process_header(rom_content[:HEADER_SIZE])

        self.PRG_ROM = self.rom_content[HEADER_SIZE:self.header['Size_PRG_ROM']]
        self.CHR_ROM = self.rom_content[HEADER_SIZE:self.header['Size_CHR_ROM']]

    def process_header(self, header_bytes):
        # Raise an exception if not a valid NES ROM is loaded
        if header_bytes[0:3] != b'NES':
            raise Exception('Not a valid NES ROM loaded')

        # Read in the header
        self.header['Magic'] = header_bytes[0:4]
        self.header['Size_PRG_ROM'] = header_bytes[4]*(KB*16)
        self.header['Size_CHR_ROM'] = header_bytes[5]*(KB*8)
        self.header['6'] = header_bytes[6]
        self.header['7'] = header_bytes[7]
        self.header['Size_PRG_RAM'] = header_bytes[8]*(KB*8)  # This might need more...
        self.header['9'] = header_bytes[9]
        self.header['10'] = header_bytes[10]
