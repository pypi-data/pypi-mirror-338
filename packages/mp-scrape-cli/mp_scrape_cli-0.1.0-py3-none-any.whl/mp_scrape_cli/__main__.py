# SPDX-FileCopyrightText: 2025 Sofía Aritz <sofiaritz@fsfe.org>
#
# SPDX-License-Identifier: AGPL-3.0-only

from . import Workflow

from mp_scrape_core import Pipeline

import sys
import asyncio
import tomllib
import importlib
import inspect
import click

@click.command()
@click.option('--workflow', '-w')
@click.option('--log-level', '-l')
def mp_scrape(workflow, log_level = "INFO"):
    """Run modules in the CLI"""

    workflow = Workflow(workflow, warning_log=click.echo)

    sources = workflow.sources()   
    click.echo("All sources instantiated")

    processes = workflow.processes()
    click.echo("All processes instantiated")
    
    consumers = workflow.consumers()
    click.echo("All consumers instantiated")

    pipeline = Pipeline(sources=sources, processes=processes, consumers=consumers)
    asyncio.run(pipeline.run(log_level=log_level.upper() if log_level is not None else "INFO"))

    click.echo("Pipeline ran successfully!")

if __name__ == "__main__":
    mp_scrape()