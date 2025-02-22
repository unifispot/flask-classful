from flask import Flask
from .view_classes import BasicView, RoutePrefixView, RouteBaseView

app = Flask('route_base')

RoutePrefixView.register(app)
RouteBaseView.register(app, route_prefix='/prefix/')
BasicView.register(app, route_prefix='/prefix/')


def test_route_prefix():
    client = app.test_client()
    resp = client.get('/my_prefix/route-prefix/')
    assert b"Index" == resp.data


def test_route_prefix_override():
    client = app.test_client()
    resp = client.get('/prefix/basic/')
    assert b"Index" == resp.data


def test_route_prefix_with_route_base():
    client = app.test_client()
    resp = client.get('/prefix/base-routed/')
    assert b"Index" == resp.data
