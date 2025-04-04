# FreeKassa Python SDK

![FreeKassa Logo](https://cdn.freekassa.com/images/logo.svg)

## Описание

FreeKassa Python SDK — это библиотека для интеграции с API FreeKassa, позволяющая легко управлять платежами, заказами и выплатами. С помощью этого SDK вы сможете быстро создать платежные ссылки, получать информацию о заказах и управлять своим балансом.

## Установка

```bash
pip install fkassa
```

## Использование

### Инициализация

Для начала работы с библиотекой, вам необходимо инициализировать класс `FreeKassa` с вашими учетными данными:

```python
from fkassa import FreeKassa

free_kassa = FreeKassa(
    shop_id=12345,
    api_key='your_api_key',
    secret_word_1='your_secret_word'
)
```

### Создание ссылки на оплату
Чтобы создать ссылку на оплату, используйте метод `create_payment_link`:

```python
payment_link = free_kassa.create_payment_link(
    order_id='order_001',
    amount=100.0,
    currency='RUB'
)

print(f"Ссылка на оплату: {payment_link}")
```

### Получение списка заказов

Вы можете получить список заказов с помощью метода `get_orders`:

```python
orders_response = free_kassa.get_orders()

for order in orders_response.orders:
    print(f"Заказ ID: {order.id}, Статус: {order.status}")
```

### Создание заказа

Для создания нового заказа используйте метод `create_order`:

```python
order_response = free_kassa.create_order(
    order_id='order_002',
    amount=150.0,
    currency='USD',
    email='customer@example.com'
)

print(f"Созданный заказ ID: {order_response.fk_id}, Ссылка: {order_response.url}")
```

### Проверка статуса платежной системы

Чтобы проверить доступность платежной системы, используйте метод `check_payment_system_status`:

```python
status_response = free_kassa.check_payment_system_status(PaymentSystem.SBP)

if status_response.type == "success":
    print("Платежная система доступна.")
else:
    print(f"Ошибка: {status_response.description}")
```