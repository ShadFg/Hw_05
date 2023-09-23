import  colorama
import inspect

print(help(colorama), "\n")
print(type(colorama.Back))
print(inspect.isclass(colorama.Back))
print(inspect.isclass(colorama.ansi.AnsiBack))

print(type(colorama.Cursor))
print(inspect.isclass(colorama.Cursor))
print(inspect.isclass(colorama.ansi.AnsiCursor))

print(type(colorama.Fore))
print(inspect.isclass(colorama.Fore))
print(inspect.isclass(colorama.ansi.AnsiFore))

print(type(colorama.Style))
print(inspect.isclass(colorama.Style))
print(inspect.isclass(colorama.ansi.AnsiStyle))