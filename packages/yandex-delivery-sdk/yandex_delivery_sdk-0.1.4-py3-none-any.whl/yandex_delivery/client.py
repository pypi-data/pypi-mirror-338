import decimal
from dataclasses import asdict
from typing import List, Optional, Dict, Any
from uuid import UUID

import requests
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed, retry_if_exception_type,
)

from yandex_delivery.exceptions import APIError, ErrorHandler
from yandex_delivery.objects import (
    CallbackProperties,
    Claim,
    ClientRequirements,
    EmergencyContact,
    Item,
    RoutePoint,
    RoutePointWithAddress,
)


class YandexDeliveryClient:
    """
    Клиент для работы с API Яндекс Доставка
    """

    API_BASE_URL = "https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/"
    DEFAULT_TIMEOUT = 10
    DEFAULT_LANGUAGE = "ru/ru"

    def __init__(self, api_key: str, timeout: int = DEFAULT_TIMEOUT):
        """
        Инициализация клиента Яндекс Доставки.

        Аргументы:
            api_key: Ключ API для аутентификации с Яндекс Доставкой
            timeout: Таймаут запросов в секундах (по умолчанию: 10)
        """
        self.api_key = api_key
        self.timeout = timeout
        self._session = self._create_session()

    def _create_session(self) -> requests.Session:
        """Создание и настройка сессии requests с необходимыми заголовками."""
        session = requests.Session()
        session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Accept-Language": self.DEFAULT_LANGUAGE,
            "Content-Type": "application/json",
        })
        return session

    def _make_request(
            self,
            endpoint: str,
            method: str = "POST",
            json_data: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Выполнение API запроса к Яндекс Доставке.

        Аргументы:
            endpoint: Путь к конечной точке API (без базового URL)
            method: HTTP метод (по умолчанию: POST)
            json_data: JSON данные для тела запроса
            params: URL параметры запроса

        Возвращает:
            Словарь с ответом API

        Вызывает:
            APIError: Если API возвращает ошибку или происходит ошибка сети/парсинга
        """
        url = f"{self.API_BASE_URL}{endpoint}"

        try:
            response = self._session.request(
                method=method,
                url=url,
                json=json_data,
                params=params,
                timeout=self.timeout,
            )

            response_data = response.json()

            if response.status_code >= 400:
                ErrorHandler.handle_error_response(response.status_code, response_data)

            return response_data

        except requests.exceptions.RequestException as e:
            raise APIError(
                message=f"Произошла сетевая ошибка: {str(e)}",
                code="network_error",
                http_status=None,
            ) from e

        except (ValueError, TypeError) as e:
            raise APIError(
                message=f"Не удалось разобрать ответ API: {str(e)}",
                code="parse_error",
                http_status=response.status_code if 'response' in locals() else None,
            ) from e

    def check_price(
            self,
            route_points: List[RoutePointWithAddress],
            client_requirements: ClientRequirements,
            skip_door_to_door: bool = False,
    ) -> decimal.Decimal:
        """
        Предварительная оценка стоимости доставки без создания заявки.

        Аргументы:
            route_points: Список точек маршрута с координатами и ID
            client_requirements: Требования клиента к доставке
            skip_door_to_door: Флаг пропуска опции доставки до двери (по умолчанию: False)

        Возвращает:
            Decimal: Стоимость доставки

        Вызывает:
            APIError: Если API возвращает ошибку или происходит ошибка сети/парсинга
            ValueError: Если в ответе отсутствуют необходимые данные

        Примеры:
            >>> price = client.check_price(
            ...     route_points=route_points,
            ...     client_requirements=requirements
            ... )
            >>> print(f"Стоимость доставки: {price} руб.")
        """
        claim = Claim(
            items=None,
            route_points=route_points,
            requirements=client_requirements,
            skip_door_to_door=skip_door_to_door,
        )

        response_data = self._make_request(
            endpoint="check-price",
            json_data=asdict(claim),
        )

        price = response_data.get("price")
        if price is None:
            raise ValueError("В ответе API отсутствует стоимость")

        return decimal.Decimal(str(price))

    def create_claim(
            self,
            request_id: UUID,
            items: List[Item],
            route_points: List[RoutePoint],
            client_requirements: ClientRequirements,
            comment: Optional[str] = None,
            callback_properties: Optional[CallbackProperties] = None,
            emergency_contact: Optional[EmergencyContact] = None,
            shipping_document: Optional[str] = None,
            skip_door_to_door: bool = False,
    ) -> str:
        """
        Создание заявки на доставку.

        Аргументы:
            request_id: Уникальный идентификатор запроса
            items: Список предметов для доставки
            route_points: Список точек маршрута
            client_requirements: Требования клиента к доставке
            comment: Опциональный комментарий к заявке
            callback_properties: Опциональная конфигурация колбэков
            emergency_contact: Опциональная контактная информация для экстренных случаев
            shipping_document: Опциональная информация о документах доставки
            skip_door_to_door: Флаг пропуска опции доставки до двери (по умолчанию: False)

        Возвращает:
            str: ID заявки от Яндекс Доставки

        Вызывает:
            APIError: Если API возвращает ошибку или происходит ошибка сети/парсинга
            ValueError: Если в ответе отсутствуют необходимые данные
        """
        claim = Claim(
            items=items,
            route_points=route_points,
            client_requirements=client_requirements,
            callback_properties=callback_properties,
            requirements=client_requirements,
            skip_door_to_door=skip_door_to_door,
            comment=comment,
            emergency_contact=emergency_contact,
            shipping_document=shipping_document,
        )

        response_data = self._make_request(
            endpoint="claims/create/",
            params={"request_id": str(request_id)},
            json_data=asdict(claim),
        )

        claim_id = response_data.get("id")
        if claim_id is None:
            raise ValueError("В ответе API отсутствует ID заявки")

        return claim_id

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(2),
        retry=retry_if_exception_type(requests.exceptions.RequestException)
    )
    def accept(self, claim_id: str, version: int) -> Dict[str, Any]:
        """
        Подтверждение ранее созданной заявки.

        Документация: https://yandex.ru/support2/delivery-profile/ru/api/express/openapi/IntegrationV2ClaimsAccept

        Аргументы:
            claim_id: Идентификатор заявки, полученный на этапе создания заявки
            version: Версия заявки (изменяется после редактирования)

        Возвращает:
            Dict: Данные ответа API

        Вызывает:
            APIError: Если API возвращает ошибку или происходит ошибка сети/парсинга
        """
        return self._make_request(
            endpoint="claims/accept",
            params={"claim_id": claim_id},
            json_data={"version": version},
        )

    def get_info(self, claim_id: str) -> Dict[str, Any]:
        """
        Получение информации о доставке.

        Документация: https://yandex.ru/support2/delivery-profile/ru/api/express/openapi/IntegrationV2ClaimsInfo

        Аргументы:
            claim_id: Идентификатор заявки, полученный на этапе создания заявки

        Возвращает:
            Dict: Информация о заявке

        Вызывает:
            APIError: Если API возвращает ошибку или происходит ошибка сети/парсинга
        """
        return self._make_request(
            endpoint="claims/info",
            params={"claim_id": claim_id},
        )

    def get_performer_phone(self, claim_id: str, point_id: int) -> Dict[str, Any]:
        """
        Получение номера телефона курьера после того, как курьер нашелся.

        Документация: https://yandex.ru/support2/delivery-profile/ru/api/express/openapi/IntegrationV2DriverVoiceForwarding

        Аргументы:
            claim_id: Идентификатор заявки, полученный на этапе создания заявки
            point_id: Целочисленный идентификатор точки, генерируемый на стороне Яндекс Доставки.
                     Содержится в поле route_points[].id.
                     Применимо к точкам с типом source, destination, return.

        Возвращает:
            Dict: Ответ API с информацией о телефоне

        Вызывает:
            APIError: Если API возвращает ошибку или происходит ошибка сети/парсинга
        """
        return self._make_request(
            endpoint="driver-voiceforwarding",
            json_data={"claim_id": claim_id, "point_id": point_id},
        )

    def get_points_eta(self, claim_id: str) -> str:
        """
        Возвращает список точек и оценку времени прибытия на точку курьером.

        Документация: https://yandex.ru/support2/delivery-profile/ru/api/express/openapi/IntegrationV2ClaimsPointsEta

        Аргументы:
            claim_id: Идентификатор заявки, полученный на этапе создания заявки

        Возвращает:
            str: Ожидаемое время доставки для первой точки маршрута

        Вызывает:
            APIError: Если API возвращает ошибку или происходит ошибка сети/парсинга
            KeyError: Если в ответе не найдена ожидаемая структура данных
        """
        response_data = self._make_request(
            endpoint="claims/points-eta",
            params={"claim_id": claim_id},
        )

        try:
            return response_data["route_points"][0]["visited_at"]["expected"]
        except (KeyError, IndexError) as e:
            raise APIError(
                message=f"Не удалось извлечь ожидаемое время прибытия из ответа: {str(e)}",
                code="parse_error",
                http_status=None,
            ) from e

    def cancel_claim(self, claim_id: str, version: int, cancel_state: str) -> str:
        """
        Отмена заявки.

        Документация: https://yandex.ru/support2/delivery-profile/ru/api/express/openapi/IntegrationV2ClaimsCancel

        Аргументы:
            claim_id: Идентификатор заявки, полученный на этапе создания заявки
            version: Версия заявки (изменяется после редактирования)
            cancel_state: Статус отмены (платная или бесплатная), значения из перечисления CancelState

        Возвращает:
            str: Обновленный статус заявки

        Вызывает:
            APIError: Если API возвращает ошибку или происходит ошибка сети/парсинга
            KeyError: Если в ответе не найдено поле status
        """
        response_data = self._make_request(
            endpoint="claims/cancel",
            params={"claim_id": claim_id},
            json_data={"version": version, "cancel_state": cancel_state},
        )

        status = response_data.get("status")
        if status is None:
            raise APIError(
                message="В ответе API отсутствует поле status",
                code="parse_error",
                http_status=None,
            )

        return status
