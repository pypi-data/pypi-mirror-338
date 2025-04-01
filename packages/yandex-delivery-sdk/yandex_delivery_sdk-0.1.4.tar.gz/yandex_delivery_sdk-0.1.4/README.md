# Yandex.Delivery API Client

Клиентская библиотека для работы с API Яндекс.Доставки.

## Описание

Данная библиотека предоставляет удобный интерфейс для взаимодействия с API Яндекс.Доставки v2. Она позволяет создавать заявки на доставку, проверять стоимость доставки и управлять процессом доставки.

## Основные возможности

- Проверка стоимости доставки
- Создание заявок на доставку
- Подтверждение заявок
- Поддержка различных типов транспорта (курьер, экспресс, грузовой)
- Обработка ошибок API

## Использование

### Инициализация клиента

```python
from yandex_delivery.client import YandexDeliveryClient

client = YandexDeliveryClient(api_key="ваш_api_ключ")
```

### Проверка стоимости доставки

```python
from yandex_delivery.objects import RoutePointWithAddress, ClientRequirements
from yandex_delivery.enums import TaxiClasses

# Создание точек маршрута
route_points = [
    RoutePointWithAddress(
        id=1,
        coordinates=[74.635061, 42.856681],
        fullname="Бишкек, ул. Горького, 1/2"
    ),
    RoutePointWithAddress(
        id=2,
        coordinates=[74.590261, 42.874537],
        fullname="Бишкек, ул. Горького, 1/2"
    )
]

# Требования к доставке
requirements = ClientRequirements(
    taxi_class=TaxiClasses.EXPRESS
)

# Получение стоимости
price = client.check_price(
    route_points=route_points,
    client_requirements=requirements
)
print(f"Стоимость доставки: {price} сом.")
```

### Создание заявки на доставку

```python
from uuid import uuid4

from yandex_delivery.objects import (
    Item, RoutePoint, Contact, Address, 
    ClientRequirements
)
from yandex_delivery.enums import RoutePointType, TaxiClasses


# Создание товара
item = Item(
    extra_id="ORDER-123",
    pickup_point=1,
    droppof_point=2,
    title="Товар 1",
    cost_value="1000",
    cost_currency="KGS",
    quantity=1
)

# Создание точек маршрута
route_points = [
    RoutePoint(
        point_id=1,
        visit_order=1,
        contact=Contact(
            name="Yryskeldi",
            phone="+996999999999"
        ),
        address=Address(
            coordinates=[74.635061, 42.856681],
            fullname="Бишкек, ул. Горького, 1/2"
        ),
        type=RoutePointType.SOURCE.value
    ),
    RoutePoint(
        point_id=2,
        visit_order=2,
        contact=Contact(
            name="Eldos",
            phone="+996999999999"
        ),
        address=Address(
            coordinates=[74.590261, 42.874537],
            fullname="Бишкек, ул. Горького, 1/2"
        ),
        type=RoutePointType.DESTINATION.value
    )
]

# Создание заявки
claim_id = client.create_claim(
    request_id=uuid4(),
    items=[item],
    route_points=route_points,
    client_requirements=ClientRequirements(
        taxi_class=TaxiClasses.EXPRESS
    ),
    comment="Комментарий к заказу",
    skip_door_to_door=False
)
```

## Статусы заявок

Библиотека поддерживает все статусы заявок Яндекс.Доставки:

- `new` - новая заявка
- `estimating` - расчет стоимости
- `accepted` - заявка принята
- `performer_lookup` - поиск исполнителя
- `performer_found` - исполнитель найден
- `pickuped` - груз забран
- `delivered` - доставлено
- И другие (полный список в `ClaimStatuses`)

## Обработка ошибок

Библиотека предоставляет специальный класс `APIError` для обработки ошибок API:

```python
from yandex_delivery.exceptions import APIError

try:
    price = client.check_price(route_points, requirements)
except APIError as e:
    print(f"Ошибка API: {e.code} - {e.message}")
    if e.response:
        print(f"Детали ответа: {e.response}")
```

## Типы данных

### RoutePointWithAddress

Используется для описания точек маршрута при проверке стоимости:
> Детали адреса не обязательны и могут быть пустыми. Подробнее в RoutePointWithAddress
```python
route_point = RoutePointWithAddress(
    id=1,
    coordinates=[74.635061, 42.856681],
    building="1",
    city="Бишкек",
    country="Кыргызстан",
    fullname="Бишкек ул. Горького 1/2",
    street="Горького",
)
```

### ClientRequirements

Определяет требования к доставке:

```python
requirements = ClientRequirements(
    taxi_class=TaxiClasses.EXPRESS,
    cargo_type=CargoType.VAN,
    cargo_options=[CargoOptions.THERMOBAG],
    cargo_loaders=1
)
```

## Ограничения

### Габариты груза

- Курьер (courier): до 0.80 м × 0.50 м × 0.50 м
- Экспресс (express): до 1.00 м × 0.60 м × 0.50 м
- Грузовой (cargo):
  - Маленький кузов: до 1.70 м × 0.96 м × 0.90 м
  - Средний кузов: до 2.60 м × 1.30 м × 1.50 м
  - Большой кузов: до 3.80 м × 1.80 м × 1.80 м

## Лицензия

MIT

## Поддержка

При возникновении проблем или вопросов создавайте issue в репозитории проекта.


### [Частые вопросы](docs/FAQ.md)
