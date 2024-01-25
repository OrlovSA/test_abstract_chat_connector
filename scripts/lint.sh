#!/bin/sh -e

flake8 сhat_transport/
black сhat_transport/
mypy сhat_transport/