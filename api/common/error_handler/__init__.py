from api.common.error_handler.not_found_handler import Error404Handler
from api.common.error_handler.server_error_handler import ServerErrorHandler

error_handlers = [Error404Handler, ServerErrorHandler]
