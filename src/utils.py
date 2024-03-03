import json
import os

def load_data(fn: str):
    """Загружает даннные из json файла"""
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    PATH = os.path.join(ROOT_DIR, "data", fn)
    # print(f'ROOT_DIR = {ROOT_DIR}')
    # print(f'PATH = {PATH}')
    #  Должно быть: /home/alexcy/sky-pro/py_project/ch13_OOP_HW_001/data/products.json
    with open(PATH, encoding='UTF-8') as read_data:
        data = json.load(read_data)
        return data

#
# dt = load_data('products.json')
# print(dt)