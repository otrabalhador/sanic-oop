from sanic.response import json
from sanic.views import HTTPMethodView


class PetStore(HTTPMethodView):
    @staticmethod
    def get(request):
        response = json({
            "hello": "pet store",
            "url": request.url
        })

        return response
