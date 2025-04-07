#!/bin/bash

. .venv/bin/activate
gunicorn app:app --bind 0.0.0.0:2426
