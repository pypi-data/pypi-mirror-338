from typing import Dict, Optional


class APIError(Exception):
    """
    Base exception for API errors
    """

    def __init__(
        self,
        message: str,
        code: str,
        http_status: Optional[int] = None,
        response: Optional[dict] = None,
    ):
        self.message = message
        self.code = code
        self.http_status = http_status
        self.response = response
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.code}: {self.message}"


class ErrorHandler:
    """
    Handler for API error responses
    """

    ERROR_MESSAGES: Dict[str, str] = {
        "estimating.swapped_coordinates": "There are no options in this area that can be booked with your selected payment method. Try checking that the latitude and longitude are in the correct order",
    }

    @classmethod
    def handle_error_response(cls, status_code: int, response_body: dict) -> None:
        """
        Обрабатывает ответ с ошибкой от API и выбрасывает соответствующее исключение

        Args:
            status_code: HTTP статус код
            response_body: тело ответа в виде словаря

        Raises:
            APIError: если получена ошибка от API
        """
        error_code = response_body.get("code")
        error_message = response_body.get("message") or cls.ERROR_MESSAGES.get(
            error_code, "Unknown error"
        )

        raise APIError(
            message=error_message,
            code=error_code,
            http_status=status_code,
            response=response_body,
        )
