DATASET_NAMES = [
    'FIRST',  # 0
    'SECOND', # 1
    'CLASSIC' # -1 just for testing
]

def dataset_info(dataset_name, is_linux=True):
    if is_linux:

        config = {
            'FIRST': {
                'option1': 123,
                'option2': 'hello',
                'option3': '/rud/fh',
            },
            'SECOND': {
                'option1': 456,
                'option2': 'hello2',
                'option3': '/rud/fh',
            },
            'CLASSIC': {
                'option1': 777,
                'option2': 'test',
                'option3': '/rud/fh',
            }
        }
    else:
        config = {
            'FIRST': {
                'option1': 123,
                'option2': 'hello',
                'option3': '/rud/fh',
            },
            'SECOND': {
                'option1': 456,
                'option2': 'hello2',
                'option3': '/rud/fh',
            },
            'CLASSIC': {
                'option1': 777,
                'option2': 'test',
                'option3': '/rud/fh',
            }
        }
    return config[dataset_name]