from enum import Enum


class RoutePointType(str, Enum):
    """
    Тип точки:

    source - точка отправления, где курьер забирает товар
    destination – точки назначения, где курьер передает товар
    return - точка возврата товара (добавляется автоматически и по умолчанию совпадает с точкой отправления, но также можно определить другую точку)
    """

    SOURCE = "source"
    DESTINATION = "destination"
    RETURN = "return"


class TaxiClasses(str, Enum):
    """
    Класс автомобиля для доставки.
    Возможные значения: courier, express, cargo.

    Точный список возможных значений для конкретной точки уточните с помощью метода получения тарифов v2/tariffs
    """

    COURIER = "courier"
    EXPRESS = "express"
    CARGO = "cargo"


class CargoType(str, Enum):
    """
    Тип (размер) кузова для грузового тарифа.
    Точный список возможных значений для конкретной геоточки уточните с помощью метода получения тарифов v2/tariffs
    """

    VAN = "van"
    LCV_M = "lcv_m"
    LCV_L = "lcv_l"


class CargoOptions(str, Enum):
    """
    Список дополнительных опций тарифа.

    Возможные отдельные опции:

    auto_courier (курьер только на машине)
    thermobag (курьер с термосумкой)

    Точный список возможных значений для конкретной геоточки уточните с помощью метода получения тарифов v1/tariffs
    """

    AUTO_COURIER = "auto_courier"
    THERMOBAG = "thermobag"


class ClaimStatuses(str, Enum):
    """
    Список статусов заявки
    """

    NEW = "new"
    ESTIMATING = "estimating"
    READY_FOR_APPROVAL = "ready_for_approval"
    ACCEPTED = "accepted"
    PERFORMER_LOOKUP = "performer_lookup"
    PERFORMER_DRAFT = "performer_draft"
    PERFORMER_FOUND = "performer_found"
    PICKUP_ARRIVED = "pickup_arrived"
    READY_FOR_PICKUP_CONF = "ready_for_pickup_confirmation"
    PICKUPED = "pickuped"
    DELIVERY_ARRIVED = "delivery_arrived"
    READY_FOR_DELIVERY_CONF = "ready_for_delivery_confirmation"
    PAY_WAITING = "pay_waiting"
    DELIVERED = "delivered"
    DELIVERED_FINISH = "delivered_finish"
    RETURNING = "returning"
    RETURN_ARRIVED = "return_arrived"
    READY_FOR_RETURN_CONF = "ready_for_return_confirmation"
    RETURNED = "returned"
    RETURNED_FINISH = "returned_finish"


class ClaimCanceledStatuses(str, Enum):
    """
    Статусы при отмене заказа
    """

    CANCELLED_BY_TAXI = "cancelled_by_taxi"
    CANCELLED = "cancelled"
    CANCELLED_WITH_PAYMENT = "cancelled_with_payment"
    CANCELLED_WITH_ITEMS_ON_HANDS = "cancelled_with_items_on_hands"


class ClaimErrorStatuses(str, Enum):
    """
    Статусы при отмене заказа
    """

    FAILED = "failed"
    ESTIMATING_FAILED = "estimating_failed"
    PERFORMER_NOT_FOUND = "performer_not_found"


class Currency(str, Enum):
    """
    Валюта
    """

    RUB = "RUB"
    USD = "USD"
    KGS = "KGS"


class CancelState(str, Enum):
    """
    Статус отмены заказа
    """

    FREE = "free"
    PAID = "paid"
