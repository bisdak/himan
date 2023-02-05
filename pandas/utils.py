import pandas as pd




def load_file(filepath, header=0):
    '''It should load any kind of file formats'''

    ext = file_ext(filepath)

    if ext == 'csv':
        df = pd.read_csv(filepath, header=header)

    return df.to_dict('list')


def file_ext(filepath):
    filename = filepath.name
    return filename.split('.')[-1]