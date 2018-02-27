# Sanic OOP

Lib for developing web applications with sanic using python Object Oriented programming.
This will help you to build large and scalable applications.

## Why?
Because you've gotta go fast... But you've gotta grow smart!

## Quick Start

```` python
from sanic_oop import SanicOOP
from app_setup import *


class AppSetup(SanicAppSetup):
    def __init__(self, app):
        super().__init__(app)
        self.app_middlewares = middlewares
        self.blueprints = blueprints
        # ...

def run():
    configuration = get_config_variables()
    app = SanicOOP()
    app.setup(AppSetup)
    app.run(**configuration)


if __name__ == "__main__":
    run()
````

## Examples of usage

* Check it out the [sanic_boilerplate]

## Requirements
- **python** >= 3.5.3
- sanic==0.7.0


[sanic_boilerplate]: ./examples/sanic_boilerplate