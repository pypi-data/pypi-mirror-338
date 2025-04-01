import datetime
from dataclasses import dataclass
from typing import Dict, List, Optional, Union


@dataclass
class ItemSizes:
    """
    Габариты товара в метрах. В полях следует передавать актуальные значения.

    Если габариты не были переданы, заказ оформляется с учетом
    максимально допустимых габаритов для выбранного тарифа.

    Если фактические характеристики товара превысят допустимые,
    курьер вправе отказаться от выполнения такого заказа на месте.
    В этом случае будет удержана стоимость подачи.

    Курьер (courier): до 0.80 м × 0.50 м × 0.50 м
    Экспресс (express): до 1.00 м × 0.60 м × 0.50 м
    Грузовой (cargo):

    Маленький кузов: до 1.70 м × 0.96 м × 0.90 м
    Средний кузов: до 2.60 м × 1.30 м × 1.50 м
    Большой кузов: до 3.80 м × 1.80 м × 1.80 м

    Атрибуты:
        length (float): Длина товара в метрах.
        width (float): Ширина товара в метрах.
        height (float): Высота товара в метрах.

    Примечание:
        Класс реализован согласно документации API Яндекс.Доставки:
        https://yandex.ru/support/delivery-profile/ru/api/express/openapi/IntegrationV2CheckPrice#cargoitemsizes
    """

    length: float
    width: float
    height: float


@dataclass
class Item:
    """
    Класс, представляющий товар в заказе.

    Атрибуты:
        extra_id (str): Краткий уникальный идентификатор товара (номер заказа в рамках заявки, как правило идентичен external_order_id)
        pickup_point (int): Идентификатор точки (int64), откуда нужно забрать товар. Отличается от идентификатора в заявке.
        droppof_point (int): Идентификатор точки (int64), куда нужно доставить товар (отличается от идентификатора в заявке).
        title (str): Наименование единицы товара
        cost_value (str): Цена за единицу товара в валюте cost_currency. Для страхования стоимости передайте фактическую цену груза
        cost_currency (str): Трехзначный код валюты, в которой ведется расчет. Допустимые значения в enum Currency.
        quantity (int): Количество товара в единицах (int64)
        size (Optional[ItemSizes]):Габариты товара в метрах. В полях следует передавать актуальные значения.
        weight (int): Вес единицы товара в кг. В поле следует передавать актуальные значения.

    Примечание:
        Класс реализован согласно документации API Яндекс.Доставки:
        https://yandex.ru/support/delivery-profile/ru/api/express/openapi/IntegrationV2ClaimsCreate#cargopointaddress
    """

    extra_id: str
    pickup_point: int
    droppof_point: int
    title: str
    cost_value: str
    cost_currency: str
    quantity: int
    size: Optional[ItemSizes] = None
    weight: int = None


@dataclass
class Address:
    """
    Адрес точки

    Атрибуты:
        coordinates (list): Географические координаты в формате [долгота, широта].
        fullname (str): Полный адрес с указанием города, улицы и номера дома.
        shortname (Optional[str]): Краткий адрес в пределах города (как на Таксометре)
        country (Optional[str]): Название страны
        city (Optional[str]): Название города
        building_name (Optional[str]): Название здания
        street (Optional[str]): Название улицы
        building (Optional[str]): Строение
        porch (Optional[str]): Подъезд
        sfloor (Optional[str]): Этаж
        sflat (Optional[str]): Квартира
        door_code (Optional[str]): Код домофона
        door_code_extra (Optional[str]): Дополнительный код домофона
        doorbell_name (Optional[str]): Имя на дверном звонке
        comment (Optional[str]): Комментарий к адресу
        uri (Optional[str]): URI геообъекта на картах
    """
    coordinates: list
    fullname: str
    shortname: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    building_name: Optional[str] = None
    street: Optional[str] = None
    building: Optional[str] = None
    porch: Optional[str] = None
    sfloor: Optional[str] = None
    sflat: Optional[str] = None
    door_code: Optional[str] = None
    door_code_extra: Optional[str] = None
    doorbell_name: Optional[str] = None
    comment: Optional[str] = None
    uri: Optional[str] = None
    description: Optional[str] = None


@dataclass
class Contact:
    """
    Информация о контактном лице

    Атрибуты:
        name (str): Имя контактного лица
        phone (str): Номер телефона контактного лица
        phone_additional_code (Optional[str]): Дополнительный код телефона
        email (Optional[str]): Адрес электронной почты
    """
    name: str
    phone: str
    phone_additional_code: Optional[str] = None
    email: Optional[str] = None


@dataclass
class ExternalOrderCost:
    """
    Стоимость внешнего заказа, привязанного к точке

    Атрибуты:
        value (str): Стоимость внешнего заказа
        currency (str): Валюта стоимости внешнего заказа. Допустимые значения в enum Currency.
    """
    value: str
    currency: str


@dataclass
class RoutePoint:
    """
    Точка маршрута доставки

    Атрибуты:
        point_id (int): Целочисленный идентификатор точки (int64), уникальна в рамках создания заявки
        visit_order (int): Порядок посещения точки (нумерация начинается с 1) (int64)
        contact (Contact): Информация о контактном лице
        address (Address): Адрес точки
        type (str): Тип точки. Допустимые значения в enum RoutePointType
        external_order_id (Optional[str]): Идентификатор внешнего заказа, привязанного к точке
        external_order_cost (Optional[ExternalOrderCost]): Стоимость внешнего заказа, привязанного к точке
        pickup_code (Optional[str]): Код для самовывоза
        skip_confirmation (bool): Пропустить подтверждение
        leave_under_door (bool): Оставить под дверью
        meet_outside (bool): Встретить на улице
        no_door_call (bool): Не звонить в домофон

    Примечание:
        Класс реализован согласно документации API Яндекс.Доставки:
        https://yandex.ru/support/delivery-profile/ru/api/express/openapi/IntegrationV2ClaimsCreate#requestpoint
    """
    point_id: int
    visit_order: int
    contact: Contact
    address: Address
    type: str
    external_order_id: Optional[str] = None
    external_order_cost: Optional[ExternalOrderCost] = None
    pickup_code: Optional[str] = None
    skip_confirmation: bool = True
    leave_under_door: bool = False
    meet_outside: bool = False
    no_door_call: bool = False


@dataclass
class RoutePointWithAddress:
    """Класс, представляющий точку маршрута доставки с полным адресом.

    Этот класс используется для определения точек маршрута доставки, отсортированных в порядке посещения (А-Б1...БN).
    Соответствует спецификации API Яндекс.Доставки.

    Атрибуты:
        id (int): Уникальный идентификатор точки маршрута (int64). Обязателен, если в заказе
            несколько точек доставки.
        coordinates (List[float]): Географические координаты в формате [долгота, широта].
        building (Optional[str]): Номер или идентификатор здания.
        city (Optional[str]): Название города.
        country (Optional[str]): Название страны.
        fullname (Optional[str]): Полный адрес, включающий город, улицу и номер дома.
            Не должен включать номер квартиры, подъезда или этажа.
        porch (Optional[str]): Идентификатор подъезда (может быть буквенным, например 'А').
        sflat (Optional[str]): Номер квартиры или помещения.
        sfloor (Optional[str]): Номер этажа.
        street (Optional[str]): Название улицы.

    Примечание:
        Класс реализован согласно документации API Яндекс.Доставки:
        https://yandex.ru/support/delivery-profile/ru/api/express/openapi/IntegrationV2CheckPrice#routepointwithaddress
    """

    id: int
    coordinates: List[float]
    building: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    fullname: Optional[str] = None
    porch: Optional[str] = None
    sflat: Optional[str] = None
    sfloor: Optional[str] = None
    street: Optional[str] = None


@dataclass
class ClientRequirements:
    """Класс, определяющий требования к доставке, включая тип транспорта и дополнительные услуги.

    Используется для указания параметров доставки, таких как класс автомобиля, тип кузова,
    дополнительные опции и количество грузчиков.

    Атрибуты:
        taxi_class (str): Класс автомобиля для доставки. Значение должно соответствовать
            enum TaxiClasses.
        cargo_type (Optional[str]): Тип (размер) кузова для грузового тарифа.
            Значение должно соответствовать enum CargoType.
        cargo_options (Optional[List[str]]): Список дополнительных опций тарифа.
            Значения должны соответствовать enum CargoOptions.
        cargo_loaders (int): Количество грузчиков для грузового тарифа.
            Допустимые значения: 0, 1, 2. По умолчанию: 0.

    Примечание:
        Класс реализован согласно документации API Яндекс.Доставки:
        https://yandex.ru/support/delivery-profile/ru/api/express/openapi/IntegrationV2CheckPrice#requirements
    """

    taxi_class: str
    cargo_type: Optional[str] = None
    cargo_options: Optional[List[str]] = None
    cargo_loaders: int = 0


@dataclass
class DeliveryInterval:
    from_date: datetime.datetime
    to: datetime.date


@dataclass
class SameDayData:
    """
    Дополнительная информация для заявок "В течение дня"

    Атрибуты:
        delivery_interval (DeliveryInterval): Интервал забора и доставки посылки
    Примечание:
        Класс реализован согласно документации API Яндекс.Доставки:
        https://yandex.ru/support/delivery-profile/ru/api/express/openapi/IntegrationV2ClaimsCreate#samedaydata
    """
    delivery_interval: DeliveryInterval


@dataclass
class EmergencyContact:
    """
    Информация о контактном лице с номером телефона

    Атрибуты:
        name (str): Имя контактного лица
        phone (str): Номер телефона контактного лица
        phone_additional_code (Optional[str]): Дополнительный код телеф

    Примечание:
        Класс реализован согласно документации API Яндекс.Доставки:
        https://yandex.ru/support/delivery-profile/ru/api/express/openapi/IntegrationV2ClaimsCreate#contactwithphone
    """
    name: str
    phone: str
    phone_additional_code: Optional[str] = None


@dataclass
class CallbackProperties:
    """
    Параметры уведомления сервера клиента о смене статуса заявки.
    Данный механизм устарел, вместо него следует использовать операцию

    Атрибуты:
        callback_url (str): URL, который вызывается при смене статусов по заявке.

    """
    callback_url: str


@dataclass
class Claim:
    """
    Класс, представляющий заявку на доставку.

    Атрибуты:
        items (Optional[List[Item]]): Список товаров в заказе.
        route_points (Union[List[RoutePoint], List[Dict], List[RoutePointWithAddress]]): Список точек маршрута доставки.
        requirements (ClientRequirements): Требования к доставке.
        due (Optional[datetime.datetime]): Ожидаемое время прибытия курьера. (В РФ отложить расчетное время прибытия можно на 30-60 минут от текущего момента).
                                           Если этот параметр не указан, поиск курьера будет осуществлен на ближайшее время.
        auto_accept (bool): Включить автоматическое подтверждение заявки после создания. Для использования данной опции требуется согласование менеджера
        same_day_data (Optional[SameDayData]): Дополнительная информация для заявок "В течение дня"
        emergency_contact (Optional[EmergencyContact]): Информация о контактном лице для экстренной связи
        client_requirements (Optional[Union[ClientRequirements, Dict]]): Требования к доставке.
        callback_properties (Optional[CallbackProperties]): Параметры уведомления сервера клиента о смене статуса заявки.
        offer_payload (Optional[str]): Payload, полученный методом offers/calculate
        comment (Optional[str]): Комментарий к заказу
        skip_act (bool): Пропустить акт (doesn't work)
        optional_return (bool): Отключить возврат товаров в случае отмены заказа. (doesn't work)
        skip_door_to_door (bool): Пропустить дверь-дверь (doesn't work)
        skip_client_notify (bool): Пропустить уведомление клиента (doesn't work)
        skip_emergency_notify (bool): Пропустить экстренное уведомление (doesn't work)
        shipping_document (Optional[str]): Сопроводительные документы
    """

    items: Optional[List[Item]]
    route_points: Union[List[RoutePoint], List[Dict], List[RoutePointWithAddress]]
    requirements: ClientRequirements
    due: Optional[datetime.datetime] = None
    auto_accept: bool = False
    same_day_data: Optional[SameDayData] = None
    emergency_contact: Optional[EmergencyContact] = None
    client_requirements: Optional[Union[ClientRequirements, Dict]] = None
    callback_properties: Optional[CallbackProperties] = None
    offer_payload: Optional[str] = None
    comment: Optional[str] = None
    skip_act: bool = False
    optional_return: bool = False
    skip_door_to_door: bool = False
    skip_client_notify: bool = False
    skip_emergency_notify: bool = False
    shipping_document: Optional[str] = None
