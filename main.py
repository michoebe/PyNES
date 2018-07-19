import argparse

from nes import NES


def main():
    # Set up the args and parse them
    parser = argparse.ArgumentParser(description='NES emulator')
    parser.add_argument('rom_path',
                        metavar='ROM_PATH',
                        type=str,
                        help='Path to ROM')
    args = parser.parse_args()

    # Create/initialize a NES object
    nes = NES()

    # Load the ROM into the NES
    nes.load_rom(args.rom_path)

    # Start the NES
    nes.start()


if __name__ == '__main__':
    main()
