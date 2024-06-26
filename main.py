import argparse
import pandas as pd

from config import logger
from processor.extractor.extractor import Extractor
from processor.transformer.transformer import Transformer
from processor.loader.loader import Loader


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


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
    transformed_meshes = transformer.meshes
    print('Transformed meshes:\n', transformed_meshes)

    logger.info('-------------- Loading data --------------------')
    loader = Loader()
    loader.load(transformed_meshes)
    data = loader.query()
    print(data)


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
