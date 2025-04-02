from __future__ import annotations

from os import environ
from pathlib import Path

from piou import Cli, Option  # type: ignore[import-untyped]
from rich.console import Console
from rich.progress import Progress, TaskID
from rich.prompt import Prompt
from rich.table import Table

from ._version import version
from .core import DatabaseFaker, GrowthStrategy, context_debug

cli = Cli(description="LLM agent for filling a database with fake records")
DEFAULT_CACHE_PATH = str(Path.home().joinpath(".filgood.cache"))


async def database_overview(db_faker: DatabaseFaker, focus_table: str | None = None, focus_schema: str | None = None) -> None:
    assert db_faker._pg_dump is not None

    console = Console()

    table = Table(title="Database Overview")

    table.add_column("Schema", justify="right", style="cyan", no_wrap=True)
    table.add_column("Table", style="magenta")
    table.add_column("Depth / Layer", justify="right", style="green")
    table.add_column("Row Count", justify="right", style="green")

    async for current_schema_table, row_count in db_faker.stats(schema=focus_schema):
        listed_schema, listed_table = current_schema_table.split(".", maxsplit=1)

        if focus_table is not None and listed_table != focus_table:
            continue

        table.add_row(
            listed_schema,
            listed_table,
            str(await db_faker._pg_dump.get_priority(listed_schema, listed_table)),
            str(row_count),
        )

    console.print(table)


@cli.command(is_main=True)
async def main(
    database_dsn: str = Option(..., help="Postgres database DSN to be used (required)"),
    increase: str = Option("100%", "-i", help="Percentage increase or flat row count target for data injection"),
    schema: str | None = Option(None, "-s", "--schema", help="Target a specific schema"),
    table: str | None = Option(None, "-t", "--table", help="Target a specific table"),
    no_cache: bool = Option(False, "--no-cache", help="Disable the cache (LLM)"),
    skip_empty: bool = Option(False, "--skip-empty", help="Skip any empty table"),
    verbose: bool = Option(False, "-v", "--verbose", help="Enable advanced debugging"),
) -> None:
    print(
        rf"""
   _____                      _   ______    _
  / ____|      {version}        | | |  ____|  | |
 | (___  _ __ ___   __ _ _ __| |_| |__ __ _| | _____ _ __
  \___ \| '_ ` _ \ / _` | '__| __|  __/ _` | |/ / _ \ '__|
  ____) | | | | | | (_| | |  | |_| | | (_| |   <  __/ |
 |_____/|_| |_| |_|\__,_|_|   \__|_|  \__,_|_|\_\___|_|
"""
    )

    print("!> Welcome to the playground")
    print("!> This will help you to quickly fill a database", end="\n\n")

    if "OPENAI_API_KEY" not in environ:
        openai_key = Prompt.ask("(Warning) Provide OpenAI API Key: ", password=True)

        if not openai_key:
            exit(1)
    else:
        openai_key = None

    target_size: int | None = None

    strategy = GrowthStrategy.BY_PERCENT_INCREASE if increase.endswith("%") else GrowthStrategy.BY_ROW_COUNT

    if increase.endswith("%"):
        increase = increase[:-1]

    try:
        target_size = int(increase)
    except ValueError:
        print(f"> {target_size} is not a valid parameter for size increase. either set '300' or '300%' for example.")
        exit(1)

    if target_size <= 0:
        print(f"> {target_size} must be greater than 0")
        exit(1)

    ctx_debug = None

    if verbose:
        ctx_debug = context_debug()
        ctx_debug.__enter__()

    async with DatabaseFaker(
        database_dsn,
        cache_path=DEFAULT_CACHE_PATH if no_cache is False else None,
        openai_key=openai_key,
    ) as db_faker:
        await database_overview(db_faker, focus_table=table, focus_schema=schema)

        with Progress() as progress:
            progress_matrix: dict[str, TaskID] = {}

            def _inner_task_watch(s, t, failure_count, success_count, total):
                progress_key = f"{s}.{t}"

                if f"{s}.{t}" not in progress_matrix:
                    progress_matrix[progress_key] = progress.add_task(f"[cyan]{progress_key}", total=total)

                progress.update(progress_matrix[progress_key], completed=failure_count + success_count)

            await db_faker.load(
                target_schema=schema,
                target_table=table,
                strategy=strategy,
                callback_progress=_inner_task_watch if not verbose else None,
                increase=target_size,
                ignore_empty_table=skip_empty,
            )

        await database_overview(db_faker, focus_table=table, focus_schema=schema)

    if ctx_debug is not None:
        ctx_debug.__exit__(None, None, None)

    exit(0)


def boot() -> None:
    cli.run()


if __name__ == "__main__":
    boot()
