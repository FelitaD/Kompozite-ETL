import argparse

from config import logger
from processor.extractor.extractor import Extractor
from processor.transformer.transformer import Transformer


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a CSV file")
    parser.add_argument('--csv_file', '-f', type=str, help="Path to the CSV file")
    return parser.parse_args()


def main(args):
    logger.info('-------------- Extracting data --------------------')
    csv_file = args.csv_file
    original_meshes = Extractor(csv_file).extract()
    print('Original meshes:\n', original_meshes)

    logger.info('-------------- Transforming data --------------------')
    transformer = Transformer(original_meshes)
    transformer.transform()
    print('Transformed meshes:\n', transformer.meshes)


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
