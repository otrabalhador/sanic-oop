from api.v1.blueprints.pet_store.exceptions import PetStoreExceptions
from api.v1.blueprints.pet_store.listeners import PetStoreListeners
from api.v1.blueprints.pet_store.middlewares import PetStoreMiddlewares
from api.v1.blueprints.pet_store.routes import PetStoreRoutes
from sanic_oop import BlueprintController


class PetStoreBlueprint(BlueprintController):
    def __init__(self):
        name = "PetStore"
        pet_store_routes = PetStoreRoutes
        pet_store_exceptions = PetStoreExceptions
        pet_store_middlewares = PetStoreMiddlewares
        pet_store_listeners = PetStoreListeners
        super().__init__(name=name,
                         routes=pet_store_routes,
                         exceptions=pet_store_exceptions,
                         middlewares=pet_store_middlewares,
                         listeners=pet_store_listeners)
