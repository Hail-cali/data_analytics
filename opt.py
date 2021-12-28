import argparse


def parse_opt():

    parser = argparse.ArgumentParser()

    parser.add_argument('--root_dir', type=str,
                        default='', help='root dir')

    parser.add_argument('--logger_path', type=str,
                        default='logs' )

    parser.add_argument('--result_path', type=str,
                        default='result', help='result path in root dir')

    parser.add_argument('--save_file', type=str,
                        default='selenium', help=' tasks name')

    parser.add_argument('--result_type', type=str,
                        default='text', help='result type | text img sound |')

    parser.add_argument('--tasks', type=str,
                        help='tasks csv file path')

    args = parser.parse_args()

    return args