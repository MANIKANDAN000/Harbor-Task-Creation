#!/bin/bash

# Run pytest using uvx to ensure dependencies are available
uvx --with pandas pytest tests/test_outputs.py
