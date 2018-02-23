from sanic import Blueprint

from api.v1.controllers.pet_store import PetStore


class PetStoreRoutes:
    def __init__(self, blueprint: Blueprint):
        self.blueprint = blueprint
        super().__init__()

    def add_routes(self):
        self.blueprint.add_route(PetStore.as_view(), "/pet-store")
