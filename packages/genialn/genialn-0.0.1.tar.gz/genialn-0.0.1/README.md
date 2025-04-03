bash
  pip install genialn
  
  
Genialn - это простая библиотека Python, предоставляющая классы для управления
скоростью выполнения кода (как для ускорения, так и для замедления).

```

▌Использование

▌Класс Slowed: Замедление кода

Импортируйте класс Slowed из библиотеки genialn и используйте его для замедления выполнения кода.

Пример с использованием контекстного менеджера:


```

python
from genialn import Slowed
import time

start_time = time.time()
with Slowed(delay=0.5) as genial:
  # Код, который нужно замедлить
  print("Начало выполнения...")
  time.sleep(0.2) # Дополнительная задержка (пример)
  print("Продолжение выполнения...")
end_time = time.time()
print(f"Время выполнения (с замедлением): {end_time - start_time:.4f} секунд")

```

Пример без использования контекстного менеджера:


```

python
from genialn import Slowed
import time

slowed = Slowed(delay=0.3)
print("Начало выполнения...")
slowed.slowed() # Задержка
print("Продолжение выполнения...")
slowed.slowed() # Еще одна задержка

```

▌Класс Speed: (Потенциальное) ускорение кода

Импортируйте класс Speed из библиотеки genialn и используйте его для (потенциального) ускорения выполнения кода.

Пример с кэшированием:


```
python
from genialn import Speed
import time

def long_running_function(x):
    time.sleep(0.1)  # Имитация долгой операции
    return x * 2

with Speed(use_cache=True) as genial:
    cached_function = genial.cache(long_running_function)

    start_time = time.time()
    result1 = cached_function(5)
    print(f"Первый вызов: {result1}")
    end_time = time.time()
    print(f"Время первого вызова: {end_time - start_time:.4f} секунд")

    start_time = time.time()
    result2 = cached_function(5)  # Результат берется из кэша
    print(f"Второй вызов: {result2}")
    end_time = time.time()
    print(f"Время второго вызова: {end_time - start_time:.4f} секунд")

```

Пример с многопоточностью:


```

python
from genialn import Speed
import time
import threading

def io_bound_function(url):
  time.sleep(0.2) # Имитация задержки при чтении данных
  print(f"Данные с URL {url} обработаны")

with Speed(use_threads=True) as genial:
  urls = ["url1", "url2", "url3"]
  for url in urls:
    genial.run_in_thread(io_bound_function, url)

print("Все задачи отправлены в потоки. Ожидание завершения...")


```

▌Зависимости

•  time (встроенный модуль Python)
•  platform (встроенный модуль Python)
•  functools (встроенный модуль Python)
•  threading (встроенный модуль Python)

▌Лицензия

Этот проект лицензирован в соответствии с условиями лицензии MIT. Подробнее см. в файле [LICENSE](LICENSE).

▌Автор

[NEFOR]

```
