import argparse

parser = argparse.ArgumentParser()

"""
    Все параметры для add_argument
    
    Метод add_argument() объекта ArgumentParser определяет, как следует анализировать один аргумент командной строки
    
    name or flags - должен знать, ожидается ли необязательный параметр, например -f или --foo, или позиционный параметр командной строки, например список имен файлов.
    Например, необязательный параметр командной строки может быть создан следующим образом: parser.add_argument('-f', '--foo')
    Обязательный позиционный параметр командной строки может быть создан следующим образом: parser.add_argument('bar')
    
    action - The basic type of action to be taken when this argument is encountered at the command line.
    nargs - The number of command-line arguments that should be consumed.
    const - A constant value required by some action and nargs selections.
    default - The value produced if the argument is absent from the command line.
    type - The type to which the command-line argument should be converted.
    choices - A container of the allowable values for the argument.
    required - Whether or not the command-line option may be omitted (optionals only).
    help - A brief description of what the argument does.
    metavar - A name for the argument in usage messages.
    dest - The name of the attribute to be added to the object returned by parse_args().

"""

parser.add_argument('--method', '-m',
                    action='store',
                    help='Method to make request',
                    default='GET')

parser.add_argument('--url', '-u',
                    action='store',
                    help='Url to make request to',
                    required=True)

# Если параметр передан то True, иначе False
parser.add_argument('--true', '-t',
                    action='store_true',
                    help='True or false param',
                    required=False)

# Добавление значений в список по параметру
# python3 ArgparseMethod.py --url=ya.ru -s
parser.add_argument('--save', '-s',
                    action='append_const',
                    const='const_to_save',
                    dest='const_collection',
                    default=[],
                    help='Store params in list',
                    required=False)

# Добавление значений в список по параметру
# python3 ArgparseMethod.py --url=ya.ru -s -s2
parser.add_argument('--save2', '-s2',
                    action='append_const',
                    const='const_to_save2',
                    dest='const_collection',
                    default=[],
                    help='Store params in list',
                    required=False)

# Парсим всё что положили
args = parser.parse_args()

# Это словарь из которого аргументы можно доставать
print(args)
