# Начать

**БЕЗ ООП**
```
# ипморт библиотеки
import time
import ErCore


def example_func():
    time.sleep(10)


core = ErCore.ECore()
core.info()  # информация
core.make_runner()  # создает start.bat(.sh)
core.logger(example_func)  # логирование
```
