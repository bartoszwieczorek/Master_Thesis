import pandas as pd
import os


path = 'C:\\Users\\Bartek\\PycharmProjects\\Master_Thesis\\output\\new\\youtube'
path2 = 'C:\\Users\\Bartek\\PycharmProjects\\Master_Thesis\\output\\new\\creativeCommons'
files = os.listdir(path)
files2 = os.listdir(path2)
print(files)
all_df = []

for file in files:
    df = pd.read_csv(os.path.join(path, file))
    time, other = file[:-4].split('__')
    series, length, order, kind, licence, region = other.split('_')
    print(time, series, order, kind, licence, region)
    print(df.columns)

    df['order'] = order
    df['licence'] = licence
    df['length'] = length
    df['topic'] = kind
    df['region'] = region
    df['time'] = time
    all_df.append(df)

    print(df['order'])

for file in files2:
    df = pd.read_csv(os.path.join(path2, file))
    time, other = file[:-4].split('__')
    series, length, order, kind, licence, region = other.split('_')
    print(time, series, order, kind, licence, region)
    print(df.columns)

    df['order'] = order
    df['licence'] = licence
    df['length'] = length
    df['topic'] = kind
    df['region'] = region
    df['time'] = time
    all_df.append(df)

all_dataframes = pd.concat(all_df)

all_dataframes.to_csv('all_data.csv', index=False)
