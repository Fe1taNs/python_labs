# python_labs

# Лабороторная работа 1

## Задание 1

```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет,{name}! Через год тебе, {age+1} ')
```
![Картинка 1](/images/1.1.png)

## Задание 2

```python
a = float(input('a: ').replace(',', '.'))
b = float(input('b: ').replace(',', '.'))
avg = (a+b)/2
sum = a + b
print(f'sum={sum}; avg={round(avg, 2)}')
```
![Картинка 2](/images/1.2.png)

## Задание 3

```python
price = float(input('price= ').replace(',', '.'))
discount = float(input('discount= ').replace(',', '.'))
vat = float(input('vat=1000 ').replace(',', '.'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vat_amount:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')
```
![Картинка 3](/images/1.3.png)

## Задание 4

```python
m = int(input('Минуты: '))
hour = m // 60
min = m % 60
print(f'{hour}:{min}')
```
![Картинка 4](/images/1.4.png)

## Задание 5

```python
name = input("ФИО: ")
f_name = ' '.join(name.strip().split())
name_parts = f_name.split()

i_list = [part[0].upper() for part in name_parts]

i = ''.join(i_list)

print(f"Инициалы: {i}.")
print(f"Длина (символов): {len(f_name)}")
```
![Картинка 5](/images/1.5.png)

# Вывод

Освоил базовый синтаксис Python. Теперь могу применять эти знания на практике, создавая простые консольные программы.
