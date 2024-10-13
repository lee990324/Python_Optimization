from parse_args import parse_args

def main(args):
    print('-------------------------------------------------------')
    print('dataset_names:', args.data_name)
    print('Option2:', args.option2)
    print('Input1:', args.input1)
    print('-------------------------------------------------------')


if __name__ == '__main__':
    args = parse_args()
    main(args)