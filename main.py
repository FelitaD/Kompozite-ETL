import argparse

from config import logger
from processor.extractor.extractor import Extractor


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a CSV file")
    parser.add_argument('--csv_file', '-f', type=str, help="Path to the CSV file")
    return parser.parse_args()


def main(args):
    logger.info('-------------- Extracting data --------------------')

    csv_file = args.csv_file
    original_meshes = Extractor(csv_file).extract()
    print(original_meshes)


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
