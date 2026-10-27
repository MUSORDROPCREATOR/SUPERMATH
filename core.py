class ZeroPowerError(Exception):
    pass

pi = 3.141592653589793
e = 2.718281828459045
tau = 2 * pi
inf = float('inf')
nan = float('nan')

def percent(a, b=None):
    if b is None:
        result = a / 100
    elif not b:
        result = 0
    else:
        result = a / 100 * b
    return result

def power(a, b=2):
    if b == 0:
        raise ZeroPowerError("Степень нулевая. В таких степнях нет смысла, будет 0!")
    else:
        return a ** b

def factorial(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def abs_val(x):
    return x if x >= 0 else -x

def sin(x):
    while x > pi:
        x -= 2 * pi
    while x < -pi:
        x += 2 * pi
    result = 0
    n = 0
    term = x
    while abs_val(term) > 1e-10:
        result += term
        n += 1
        term = term * (-1) * x * x / ((2 * n) * (2 * n + 1))
    return result

def cos(x):
    x = x % (2 * pi)
    if x > pi:
        x -= 2 * pi
    result = 1.0
    term = 1.0
    n = 1
    while abs(term) > 1e-15:
        term *= -1 * (x * x) / ((2 * n - 1) * (2 * n))
        result += term
        n += 1
    return result

def tan(x):
    c = cos(x)
    if c == 0:
        raise ValueError("Деление на ноль")
    return sin(x) / c

def sqrt(x):
    if x < 0:
        raise ValueError("Корень из отрицательного числа")
    return x ** 0.5

def cbrt(x):
    if x < 0:
        return -((-x) ** (1/3))
    return x ** (1/3)

def ln(x):
    if x <= 0:
        raise ValueError("Логарифм определен только для положительных чисел")
    
    # Приводим x к диапазону, где ряд сходится быстрее (оптимизация)
    # Если x очень большой, используем свойство ln(x) = ln(x/2) + ln(2)
    # Но для простоты оставим базовую формулу.
    
    z = (x - 1) / (x + 1)
    z2 = z * z
    term = z
    result = z
    n = 3
    
    while abs(term) > 1e-15:
        term *= z2
        result += term / n
        n += 2
        
    return 2 * result

def exp(x):
    """Возвращает число e в степени x (e^x)."""
    result = 1.0
    term = 1.0
    n = 1
    
    # Считаем сумму, пока слагаемое не станет слишком маленьким
    while abs(term) > 1e-15:
        term *= x / n  # Формула перехода к следующему члену ряда
        result += term
        n += 1
        
        # Защита от бесконечного цикла, если x очень большое
        # (например, для exp(1000) ряд будет сходиться очень долго)
        if n > 1000: 
            break
            
    return result

def log(x, base=None):
    """Логарифм x по основанию base. Если base не указан, считается натуральный логарифм."""
    if base is None:
        return ln(x)
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Недопустимые аргументы для логарифма")
    return ln(x) / ln(base)

def round_down(x):
    """Округляет вниз (аналог math.floor)."""
    i = int(x) # int() просто отбрасывает дробную часть (5.7 -> 5, -5.7 -> -5)
    
    # Если число отрицательное и дробное (например, -5.7), int даст -5.
    # А нам нужно -6. Значит, вычитаем 1.
    if x < 0 and x != i:
        return i - 1
    return i

def round_up(x):
    """Округляет вверх (аналог math.ceil)."""
    i = int(x)
    
    # Если число положительное и дробное (например, 5.1), int даст 5.
    # А нам нужно 6. Значит, прибавляем 1.
    if x > 0 and x != i:
        return i + 1
    return i

def fmod(x, y):
    """Возвращает остаток от деления x на y (с плавающей точкой)."""
    if y == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
        
    # Находим, сколько раз y целиком помещается в x (отбрасываем дробную часть)
    quotient = int(x / y)
    
    # Вычитаем это количество из x
    return x - (quotient * y)

def mean(numbers):
    """Возвращает среднее арифметическое списка чисел."""
    if not numbers:  # Если список пустой
        raise ValueError("Список не может быть пустым")
        
    total = 0
    for num in numbers:
        total += num
        
    return total / len(numbers)

def median(numbers):
    """Возвращает медиану списка чисел."""
    if not numbers:
        raise ValueError("Список не может быть пустым")
        
    # 1. Сначала отсортируем список (алгоритм "пузырька")
    arr = list(numbers)  # Копируем, чтобы не менять оригинал
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    # 2. Теперь ищем середину
    mid = n // 2  # Целочисленное деление (например, 5 // 2 = 2)
    
    if n % 2 != 0:
        # Если нечетное количество (например, 5), берем центральный элемент (индекс 2)
        return arr[mid]
    else:
        # Если четное (например, 4), берем среднее двух центральных (индексы 1 и 2)
        return (arr[mid - 1] + arr[mid]) / 2.0

def max_val(numbers):
    """Возвращает максимальное число из списка."""
    if not numbers:
        raise ValueError("Список не может быть пустым")
    
    max_num = numbers[0] # Берем первое число за эталон
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def min_val(numbers):
    """Возвращает минимальное число из списка."""
    if not numbers:
        raise ValueError("Список не может быть пустым")
        
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def variance(numbers):
    """Выборочная дисперсия (как в statistics.variance)."""
    n = len(numbers)
    if n < 2:
        raise ValueError("Для дисперсии нужно минимум 2 числа")
        
    # 1. Находим среднее (используем нашу функцию)
    avg = mean(numbers)
    
    # 2. Считаем сумму квадратов отклонений от среднего
    sum_sq_diff = 0
    for num in numbers:
        diff = num - avg
        sum_sq_diff += diff * diff  # Возводим в квадрат (можно было diff ** 2)
        
    # 3. Делим на (n - 1)
    return sum_sq_diff / (n - 1)


def stdev(numbers):
    """Стандартное отклонение (корень из дисперсии)."""
    # Используем нашу функцию sqrt, которую писали ранее!
    return sqrt(variance(numbers))

def hypot(x, y):
    """Возвращает длину гипотенузы (расстояние от точки (0,0) до (x,y))."""
    # Возводим в квадрат и складываем
    sum_sq = (x * x) + (y * y)
    # Используем нашу функцию sqrt (если она у тебя выдает ошибку для отрицательных, 
    # то тут всё ок, так как сумма квадратов всегда положительная)
    return sqrt(sum_sq)

def degrees(x):
    """Переводит радианы в градусы."""
    return x * 180 / pi

def radians(x):
    """Переводит градусы в радианы."""
    return x * pi / 180

def asin(x):
    """Возвращает арксинус числа x (в радианах)."""
    if x < -1 or x > 1:
        raise ValueError("Арксинус определен только от -1 до 1")
        
    # Если x == 1 или -1, ряд сходится очень медленно, 
    # поэтому обрабатываем эти случаи отдельно
    if x == 1:
        return pi / 2
    if x == -1:
        return -pi / 2
        
    result = x
    term = x
    n = 1
    
    # Формула перехода к следующему члену ряда
    while abs(term) > 1e-15:
        term *= (x * x) * (2 * n - 1) / (2 * n)
        result += term / (2 * n + 1)
        n += 1
        
    return result
