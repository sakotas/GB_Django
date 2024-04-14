### Домашнее задание 3
### Фильтрация товаров по дате заказа
Позволяет получить список товаров, заказанных за последние 7, 30 и 365 дней.

#### Примеры URL-маршрутов
- `/orders/<int:client_id>/`: Просмотр товаров по клиенту с возможностью указания ID клиента в URL.


### Домашнее задание 2

Создайте три модели Django: клиент, товар и заказ.

- **Клиент** может иметь несколько заказов. 
- **Заказ** может содержать несколько товаров. 
- **Товар** может входить в несколько заказов.

### Клиент
- **name**: Имя клиента.
- **email**: Электронная почта клиента.
- **phone**: Номер телефона клиента.
- **address**: Адрес клиента.
- **registered_on**: Дата регистрации клиента.

### Товар
- **item_name**: Название товара.
- **description**: Описание товара.
- **price**: Цена товара.
- **quantity**: Количество товара.
- **date_added**: Дата добавления товара.

### Заказ
- **client**: Связь с моделью `Client`, указывает на клиента, сделавшего заказ.
- **products**: Связь с моделью `Product`, указывает на товары, входящие в заказ.
- **total_sum**: Общая сумма заказа.
- **date_ordered**: Дата оформления заказа.

### Примеры функций CRUD

#### Создание клиента

```python
def create_client(name, email, phone, address):
    client = Client(name=name, email=email, phone=phone, address=address)
    client.save()
    return client
```

#### Получение информации о товаре по ID

```python
def get_product_by_id(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return product
    except Product.DoesNotExist:
        return None
```

#### Обновление данных заказа

```python
def update_order(order_id, client_id=None, product_ids=None, total_sum=None):
    order = Order.objects.get(id=order_id)
    if client_id is not None:
        order.client_id = client_id
    if product_ids is not None:
        order.products.clear()
        for pid in product_ids:
            product = Product.objects.get(id=pid)
            order.products.add(product)
    if total_sum is not None:
        order.total_sum = total_sum
    order.save()
    return order
```

#### Удаление клиента

```python
def delete_client(client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
```

Эти функции представляют базовый набор операций CRUD для работы с моделями в Django и могут быть расширены или модифицированы в зависимости от требований к приложению.