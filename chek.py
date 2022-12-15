import os
print(os.path.abspath(__file__))    # команда поиска пути ЭТОГО скрипта (файла с этим скриптом)
print(os.path.abspath(os.path.dirname(__file__)))   # такая же + передача файла из этой директории по имени + расширение
