class SanicMiddleware:
    def __init__(self, middleware, attach_to):
        self.middleware = middleware
        self.attach_to = attach_to
