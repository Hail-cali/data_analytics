import os


def save_result(opt, *args, **kwargs):
    dir_path = os.path.join('..', opt.result_path)
    file_name = f"{prefix_name(term='short')}{suffix_name(opt.save_file)}"
    data = None
    if kwargs:
        data = kwargs
    if args:
        data = args

    if opt.result_path not in os.listdir('../'):
        os.mkdir(dir_path)
        print(f'logger:: make dir in {dir_path}')

    if opt.result_type == 'text':
        import csv
        file_name += '.csv'

        with open(os.path.join(dir_path, file_name), 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            if isinstance(data, dict):
                for line in data:
                    print(data[line])
                    writer.writerow(data[line])
            else:
                for line in data:
                    print(line)
                    writer.writerow([line])


    elif opt.result_type == 'img':
        file_name += '.png'

    print(f'logger:: saved in save_dir {dir_path}/{file_name}')


def prefix_name(term='long'):
    from datetime import datetime
    import os
    name = ''
    if term == 'long':
        done_time = datetime.today().strftime("%Y-%m-%d::%H:%M:%S:%p")
        name = os.name + '_' + done_time

    elif term == 'short':
        done_time = datetime.today().strftime("%m-%d")
        name = os.name + '_' + done_time

    return name


def suffix_name(suffix):

    def wrap(name):
        return '(' + name + ')'

    return wrap(suffix)





if __name__ == '__main__':
    import opt
    opts = opt.parse_opt()
    l = list(range(0,10))
    le = dict(zip(['a','b'], l))
    mi = {'c':10,'d':20}

    save_result(opts, *l)