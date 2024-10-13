import argparse
import platform

from dataset import DATASET_NAMES, dataset_info

IS_LINUX = True if platform.system()=="Linux" else False

def parse_args():
    parser = argparse.ArgumentParser(description='프로그램 설명')
    parser.add_argument('--choose_data',
                        type=int,
                        default=-1, # test
                        help='Choose a dataset for testing: 0 - 1')

    dataset_names = DATASET_NAMES[parser.parse_args().choose_data]
    data_inf = dataset_info(dataset_names, is_linux=IS_LINUX)
    option1 = data_inf['option1']
    option2 = data_inf['option2']
    option3 = data_inf['option3']
    is_testing = False

    # Data parameters
    parser.add_argument('--input_dir',
                        type=str,
                        default=option3,
                        help='the path to the directory with the input data.')
    parser.add_argument('--output_dir',
                        type=str,
                        default='ouput',
                        help='the path to output the results.')
    parser.add_argument('--data_name',
                        type=str,
                        choices=DATASET_NAMES,
                        default=dataset_names,
                        help='Name of the dataset.')
    parser.add_argument('--option2',
                        type=str,
                        default=option2,
                        help='just test')
    parser.add_argument('--input1',
                        type=str,
                        default='Hello World!',
                        help='just test')
    parser.add_argument('--is_testing',type=bool,
                        default=is_testing,
                        help='Script in testing mode.')

    args = parser.parse_args()
    return args