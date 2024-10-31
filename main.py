#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-10-28 11:05
# describe：

import click
import uvicorn
from src.app import app
import src.api as api

@click.command()
@click.option("--host", "-H", default="0.0.0.0", help="Host to run the app on")
@click.option("--port", "-p", default=17781, type=int, help="Port to run the app on")
def main(port: int, host: str):
    """Run the FastAPI app."""
    api.get_f5tts()
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    main()
