import json

from src.adapters.inbound.serverless.errors.exception_handler_strategy import ExceptionHandlerStrategy
from src.adapters.inbound.serverless.response.response import Response


class KeyErrorHandler(ExceptionHandlerStrategy):
    def handle(self, exception, event):
        method = event.get("requestContext", {}).get("http", {}).get("method", "UNKNOWN")
        headers = event.get("headers", {})
        headers_list = [(key, value) for key, value in headers.items()]
        body = json.dumps({"error": f"Chave nao encontrada: {exception}"})
        return Response(
            status_code=404,
            body=body,
            headers=headers_list,
            method=method
        ).to_dict()