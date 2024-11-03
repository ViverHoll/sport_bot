#!/bin/sh

set -e

make migrate
exec make run


