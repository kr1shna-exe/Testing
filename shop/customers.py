import sqlite3


def big_spenders(conn: sqlite3.Connection, min_cents: int) -> list[tuple]:
    rows = conn.execute("SELECT id, name, lifetime_cents FROM customers").fetchall()
    return [row for row in rows if row[2] >= min_cents]


def customer_name(conn: sqlite3.Connection, customer_id: int) -> str | None:
    row = conn.execute(
        "SELECT name FROM customers WHERE id = ?", (customer_id,)
    ).fetchone()
    return row[0] if row else None


def lifetime_dollars(conn: sqlite3.Connection, customer_id: int) -> float:
    row = conn.execute(
        "SELECT lifetime_cents FROM customers WHERE id = ?", (customer_id,)
    ).fetchone()
    return row[0] / 100
