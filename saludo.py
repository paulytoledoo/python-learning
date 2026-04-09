import argparse

#todos los scripts con argparser arrancan igual primero importamos el módulo, luego creamos el parser y por último llamamos a parse_args()

parser = argparse.ArgumentParser(description = "Script que saluda a alguien")
parser.add_argument("nombre" , help = "El nombre de la persona a saludar")
args = parser.parse_args()
print(f"Hola {args.nombre}!")



