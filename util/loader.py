


def load_csv(path):
    import csv


    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        file = list(reader)
    return file

if __name__=='__main__':
    from opt import parse_opt

    opts = parse_opt()
    opts.tasks = '/Users/george/PycharmProjects/dbmodel/tasks.csv'

    print(opts.tasks)
    file = load_csv(opts.tasks)
    url = [link[0] for link in file]
    print(url)
