from __future__ import annotations

import typing
from json import dumps
from os import environ, unlink
from pathlib import Path

import aiofile
import asyncpg
import pytest_asyncio
from aiofile import async_open

from filgood import DatabaseFaker, version

CURRENT_DIRECTORY = Path(__file__).parent


@pytest_asyncio.fixture(scope="session", autouse=True)
async def use_fixture() -> typing.AsyncGenerator[None]:
    conn: asyncpg.Connection = await asyncpg.connect(environ.get("POSTGRES_DSN"))

    async with aiofile.async_open(CURRENT_DIRECTORY.joinpath("fixture.sql"), "r") as fp:
        await conn.execute(await fp.read())

    yield

    await conn.execute("DROP TABLE order_items CASCADE")
    await conn.execute("DROP TABLE shipping CASCADE")
    await conn.execute("DROP TABLE ratings CASCADE")
    await conn.execute("DROP TABLE orders CASCADE")
    await conn.execute("DROP TABLE products CASCADE")
    await conn.execute("DROP TABLE categories CASCADE")
    await conn.execute("DROP TABLE users CASCADE")

    await conn.close()


@pytest_asyncio.fixture(scope="function")
async def connection() -> typing.AsyncGenerator[asyncpg.Connection]:
    conn: asyncpg.Connection = await asyncpg.connect(environ.get("POSTGRES_DSN"))

    yield conn

    await conn.close()


@pytest_asyncio.fixture(scope="function")
async def pg_faker() -> typing.AsyncGenerator[DatabaseFaker]:
    async with DatabaseFaker(environ.get("POSTGRES_DSN"), cache_path=".filgood.mock.cache") as db_faker:
        yield db_faker


@pytest_asyncio.fixture(scope="session", autouse=True)
async def cache_mock() -> typing.AsyncGenerator[None]:
    async with async_open(".filgood.mock.cache", "w") as fp:
        await fp.write(
            dumps(
                {
                    "version": version,
                    "databases": {
                        "839194a454b90870e4f189d2be49f072cd33bfaf75fe7558fd60e9565d5460b3": {
                            "thread": "thread_qIZgohmjgRx0OMFKzd80Yhtz",
                            "definitions": {
                                "public.categories": {
                                    "fingerprint": "f5a498d8dde1bdc2e839856da41130406e04b848063dd7993e511f3658926466",
                                    "boilerplate": '```python\n# The connection is already instantiated higher in the stack\nasync def insert(conn: asyncpg.Connection) -> bool:\n    import random\n    import string\n    import asyncpg\n    import logging\n\n    logger = logging.getLogger(\'smartfaker.core\')\n\n    # Generate a random alphanumeric name\n    name = f"Category {\'\'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))}"\n\n    try:\n        await conn.execute(\n            """\n            INSERT INTO public.categories (name) VALUES ($1)\n            """,\n            name\n        )\n    except asyncpg.PostgresError as e:\n        logger.debug(str(e))\n        return str(e)\n    \n    return None\n```\n\nThis script uses standard Python libraries to generate random category names without relying on the `faker` library. It should work even if `faker` is not installed in your environment.',  # noqa: E501
                                },
                                "public.users": {
                                    "fingerprint": "3f90d89a295f0a87ed7b64bb890889adbe5fad6b843d5d1912d95fbaeff057d6",
                                    "boilerplate": '```python\n# The connection is already instantiated higher in the stack\nasync def insert(conn: asyncpg.Connection) -> bool:\n    import random\n    import string\n    import asyncpg\n    import logging\n    import hashlib\n\n    logger = logging.getLogger(\'smartfaker.core\')\n\n    # Generate random alphanumeric seed string for name\n    name = f"User {\'\'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))}"\n    \n    # Generate a unique email address\n    email = f"user{random.randint(1000, 9999)}@example.com"\n    \n    # Generate a random password and hash it using SHA256\n    password = \'\'.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))\n    password_hash = hashlib.sha256(password.encode(\'utf-8\')).hexdigest()\n\n    try:\n        await conn.execute(\n            """\n            INSERT INTO public.users (name, email, password_hash) VALUES ($1, $2, $3)\n            """,\n            name, email, password_hash\n        )\n    except asyncpg.PostgresError as e:\n        logger.debug(str(e))\n        return str(e)\n    \n    return None\n```\n\nI\'ve added the import statement for `hashlib` to the script. This will ensure the script can hash the password correctly. Make sure to have the necessary packages and imports correctly spelled and declared.',  # noqa: E501
                                },
                                "public.orders": {
                                    "fingerprint": "58c01c2820edac2766d18e0abe6cdc424db059490b12d78ddfff5c8ce7790d10",
                                    "boilerplate": '```python\n# The connection is already instantiated higher in the stack\nasync def insert(conn: asyncpg.Connection) -> bool:\n    import random\n    import asyncpg\n    import logging\n\n    logger = logging.getLogger(\'smartfaker.core\')\n\n    # Generate random data\n    total_price = round(random.uniform(10, 1000), 2)\n\n    try:\n        # Retrieve a random user_id from the users table\n        user_record = await conn.fetchrow(\n            """\n            SELECT id FROM public.users ORDER BY RANDOM() LIMIT 1\n            """\n        )\n\n        # Ensure user_id is retrieved\n        if user_record:\n            user_id = user_record[\'id\']\n        else:\n            # If no user found, log the error and return\n            logger.debug("No users found to associate with order.")\n            return "No users found to associate with order."\n\n        await conn.execute(\n            """\n            INSERT INTO public.orders (user_id, total_price) VALUES ($1, $2)\n            """,\n            user_id, total_price\n        )\n    except asyncpg.PostgresError as e:\n        logger.debug(str(e))\n        return str(e)\n    \n    return None\n```\n\nIn this version, I\'ve addressed the potential issue of not finding any users to associate with an order directly within the logic flow, ensuring that the error message is clearly logged and communicated when no users are present in the database.',  # noqa: E501
                                },
                                "public.products": {
                                    "fingerprint": "da0e5041ae9c2f5817188003fb219e15222924d147198c91306cc34630eff3d8",
                                    "boilerplate": '```python\n# The connection is already instantiated higher in the stack\nasync def insert(conn: asyncpg.Connection) -> bool:\n    import random\n    import string\n    import asyncpg\n    import logging\n\n    logger = logging.getLogger(\'smartfaker.core\')\n\n    # Generate random data\n    name = f"Product {\'\'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))}"\n    description = f"This is a description for {name}."\n    price = round(random.uniform(1, 1000), 2)\n    stock = random.randint(1, 100)\n\n    try:\n        # Retrieve a random category_id from the categories table\n        category_record = await conn.fetchrow(\n            """\n            SELECT id FROM public.categories ORDER BY RANDOM() LIMIT 1\n            """\n        )\n\n        # category_id can be NULL\n        category_id = category_record[\'id\'] if category_record else None\n\n        await conn.execute(\n            """\n            INSERT INTO public.products (name, description, price, stock, category_id) VALUES ($1, $2, $3, $4, $5)\n            """,\n            name, description, price, stock, category_id\n        )\n    except asyncpg.PostgresError as e:\n        logger.debug(str(e))\n        return str(e)\n    \n    return None\n```\n\nThis script creates a new product with random data, including a category that may be `NULL` if no categories exist. Ensure categories are present in the database if a foreign key association is desired.',  # noqa: E501
                                },
                                "public.order_items": {
                                    "fingerprint": "bfea559d9feea2da689613f21ea70d8166544ab216aa49fa3654d06a738bfe28",
                                    "boilerplate": '```python\n# The connection is already instantiated higher in the stack\nasync def insert(conn: asyncpg.Connection) -> bool:\n    import random\n    import asyncpg\n    import logging\n\n    logger = logging.getLogger(\'smartfaker.core\')\n\n    # Generate random data\n    quantity = random.randint(1, 10)\n    \n    try:\n        # Retrieve a random order_id from the orders table\n        order_record = await conn.fetchrow(\n            """\n            SELECT id FROM public.orders ORDER BY RANDOM() LIMIT 1\n            """\n        )\n\n        # Ensure order_id is retrieved\n        if not order_record:\n            raise asyncpg.PostgresError("No orders found to associate with order item.")\n\n        order_id = order_record[\'id\']\n\n        # Retrieve a random product_id and price from the products table\n        product_record = await conn.fetchrow(\n            """\n            SELECT id, price FROM public.products ORDER BY RANDOM() LIMIT 1\n            """\n        )\n\n        # Ensure product_id is retrieved\n        if not product_record:\n            raise asyncpg.PostgresError("No products found to associate with order item.")\n\n        product_id = product_record[\'id\']\n        price = product_record[\'price\']\n\n        await conn.execute(\n            """\n            INSERT INTO public.order_items (order_id, product_id, quantity, price) VALUES ($1, $2, $3, $4)\n            """,\n            order_id, product_id, quantity, price\n        )\n    except asyncpg.PostgresError as e:\n        logger.debug(str(e))\n        return str(e)\n    \n    return None\n```\n\nThis script fetches random `order_id` and `product_id` while setting the `price` from the product table. It ensures that constraints are satisfied and handles any potential errors if there are no orders or products available in the database.',  # noqa: E501
                                },
                                "public.shipping": {
                                    "fingerprint": "3c67bfc62fafc70a726359da1aecbedd851826df12122c682ed70e5d5a50b900",
                                    "boilerplate": "```python\n# The connection is already instantiated higher in the stack\nasync def insert(conn: asyncpg.Connection) -> bool:\n    import random\n    import string\n    import asyncpg\n    import logging\n    from datetime import datetime, timedelta\n\n    logger = logging.getLogger('smartfaker.core')\n\n    # Generate random data\n    tracking_number = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))\n    carrier = random.choice(['FedEx', 'UPS', 'DHL', 'USPS'])\n    estimated_delivery = datetime.now() + timedelta(days=random.randint(1, 10))\n    \n    try:\n        # Retrieve a random order_id from the orders table\n        order_record = await conn.fetchrow(\n            \"\"\"\n            SELECT id FROM public.orders ORDER BY RANDOM() LIMIT 1\n            \"\"\"\n        )\n\n        # Ensure order_id is retrieved\n        if not order_record:\n            raise asyncpg.PostgresError(\"No orders found to associate with shipping.\")\n\n        order_id = order_record['id']\n\n        await conn.execute(\n            \"\"\"\n            INSERT INTO public.shipping (order_id, tracking_number, carrier, estimated_delivery) VALUES ($1, $2, $3, $4)\n            \"\"\",\n            order_id, tracking_number, carrier, estimated_delivery\n        )\n    except asyncpg.PostgresError as e:\n        logger.debug(str(e))\n        return str(e)\n    \n    return None\n```\n\nThis script creates a shipping record with randomly generated data, including a tracking number, carrier, and estimated delivery date. It fetches an order ID to satisfy the foreign key constraint. Ensure there are pre-existing records in the `orders` table for successful insertion.",  # noqa: E501
                                },
                                "public.ratings": {
                                    "fingerprint": "2b8cce7e0739d00bbba12669e43d42cfb76f57d640238663189a6ac338cd1213",
                                    "boilerplate": '```python\n# The connection is already instantiated higher in the stack\nasync def insert(conn: asyncpg.Connection) -> bool:\n    import random\n    import asyncpg\n    import logging\n\n    logger = logging.getLogger(\'smartfaker.core\')\n\n    # Generate random data\n    rating = random.randint(1, 5)\n    review = f"This is a review for a rating of {rating}."\n\n    try:\n        # Retrieve a random user_id from the users table\n        user_record = await conn.fetchrow(\n            """\n            SELECT id FROM public.users ORDER BY RANDOM() LIMIT 1\n            """\n        )\n\n        # Ensure user_id is retrieved\n        if not user_record:\n            raise asyncpg.PostgresError("No users found to associate with rating.")\n\n        user_id = user_record[\'id\']\n\n        # Retrieve a random product_id from the products table\n        product_record = await conn.fetchrow(\n            """\n            SELECT id FROM public.products ORDER BY RANDOM() LIMIT 1\n            """\n        )\n\n        # Ensure product_id is retrieved\n        if not product_record:\n            raise asyncpg.PostgresError("No products found to associate with rating.")\n\n        product_id = product_record[\'id\']\n\n        await conn.execute(\n            """\n            INSERT INTO public.ratings (user_id, product_id, rating, review) VALUES ($1, $2, $3, $4)\n            """,\n            user_id, product_id, rating, review\n        )\n    except asyncpg.PostgresError as e:\n        logger.debug(str(e))\n        return str(e)\n    \n    return None\n```\n\nThis script generates a rating with a review, selects random valid `user_id` and `product_id` that satisfy foreign key constraints, and inserts them into the `ratings` table. It ensures that ratings are between 1 and 5, as required by the CHECK constraint.',  # noqa: E501
                                },
                            },
                        }
                    },
                }
            )
        )
        yield

    unlink(".filgood.mock.cache")
