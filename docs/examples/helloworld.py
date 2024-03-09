# helloworld.py
from rhino import Mapper
from rhino.response import ok

mapper = Mapper()


@mapper.get("/")
def index(ctx):
    return ok("Hello, world!")


app = mapper.make_wsgi_app()
