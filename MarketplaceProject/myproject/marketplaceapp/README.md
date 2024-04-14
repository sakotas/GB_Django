### Домашнее задание 5
### Задание
Настройте под свои нужды вывод информации о клиентах, товарах и заказах на страницах вывода информации об объекте и вывода списка объектов.
### Изменения в файле `admin.py`

Для каждой из моделей `Client`, `Product`, и `Order` создаются специализированные классы администратора, которые позволяют настроить отображение списка, поиск и фильтрацию.

#### Пример кода

1. **Импорты и регистрация моделей**:
   ```python
   from django.contrib import admin
   from .models import Client, Product, Order
   class ClientAdmin(admin.ModelAdmin):
       list_display = ['name', 'email', 'phone', 'address', 'registered_on']
       search_fields = ['name', 'email', 'phone']
   
   admin.site.register(Client, ClientAdmin)
   
   class ProductAdmin(admin.ModelAdmin):
       list_display = ['item_name', 'description', 'price', 'quantity', 'date_added']
       list_filter = ['date_added', 'price']
       search_fields = ['item_name']
   
   admin.site.register(Product, ProductAdmin)
   
   class OrderAdmin(admin.ModelAdmin):
       list_display = ['client', 'total_sum', 'date_ordered']
       list_filter = ['date_ordered']
       search_fields = ['client__name', 'client__email']
   
   admin.site.register(Order, OrderAdmin)
   ```
Параметры настройки:

`list_display`: Указывает поля, которые будут отображаться в списке объектов.

`list_filter`: Позволяет добавлять фильтры для удобной сортировки данных по указанным полям.

`search_fields`: Добавляет возможность поиска по указанным полям.


### Домашнее задание 4
### Расширение модели `Product` и загрузка изображений

#### Изменение модели
Модель `Product` была расширена для включения поля `image`, которое позволяет хранить изображения товаров.

```python
class Product(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
```
#### Создание формы для загрузки изображений
Для управления загрузкой изображений была создана форма `ProductForm` на основе модели `Product`.

```python
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item_name', 'description', 'price', 'quantity', 'image']
```

#### Представление для обработки формы
Форма обрабатывается в представлении `add_product`, которое сохраняет данные формы и изображение в базу данных.

```python
from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Убедитесь, что URL-адрес существует
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
```

#### Шаблон для формы
Шаблон `add_product.html` используется для отображения формы на веб-странице.

```html
{% extends 'base.html' %}

{% block content %}
<h2>Add Product</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save Product</button>
</form>
{% endblock %}
```

#### Настройка медиа-файлов
Убедитесь, что в настройках проекта (`settings.py`) корректно настроены `MEDIA_ROOT` и `MEDIA_URL` для обслуживания медиа-файлов.

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Эти изменения позволяют загружать и хранить изображения товаров, что расширяет функциональность приложения.

### Домашнее задание 3
### Фильтрация товаров по дате заказа
Позволяет получить список товаров, заказанных за последние 7, 30 и 365 дней.

#### Примеры URL-маршрутов
- `/orders/`: Просмотр товаров по клиенту по умолчанию (`client_id` = 1).
- `/orders/<int:client_id>/`: Просмотр товаров по клиенту с возможностью указания ID клиента в URL.

### Создание "dummy" данных

Для создания примерных данных, можно использовать Django shell для добавления данных в базу:

1. **Запустите Django shell:**
   ```bash
   python manage.py shell
   ```

Вводим следующие команды для создания данных:
```bash
from marketplaceapp.models import Client, Product, Order
client = Client(name="John Doe", email="john@example.com", phone="1234567890", address="123 Main St")
client.save()
product1 = Product(item_name="Product 1", description="A great product", price=19.99, quantity=10)
product1.save()
product2 = Product(item_name="Product 2", description="Another great product", price=29.99, quantity=5)
product2.save()
order = Order(client=client, total_sum=0.00)
order.save()
order.products.add(product1, product2)
order.update_total_sum()  
```
Эти команды создадут клиента, два товара и заказ, связывая их между собой.



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