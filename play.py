from imp import reload
from rear_end_services import load_csv

def play(num):
    while True:
        try:
            load_csv.load_td('terrorism_rear_end/data/data.csv', num)
            break
        except Exception as e:
            reload(load_csv)
            num = int(e.args[0])
            print('Break', e)
            continue

    