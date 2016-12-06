import argparse

parser = argparse.ArgumentParser(description='ayuda de mi programa')

parser.add_argument('-module', dest='module_name', metavar='<module name>', help='ayuda del modulo')
parser.add_argument('-number', dest='number_name', default='5')

comandos = parser.parse_args()

print(comandos)
