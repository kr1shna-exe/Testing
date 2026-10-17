import sqlite3


def get_orders(conn: sqlite3.Connection, customer_id: int) -> list[tuple]:
    return conn.execute(
        "SELECT id, total_cents FROM orders WHERE customer_id = ?", (customer_id,)
    ).fetchall()


def search_orders(conn: sqlite3.Connection, term: str) -> list[tuple]:
    return conn.execute(
        f"SELECT id, total_cents FROM orders WHERE note LIKE '%{term}%'"
    ).fetchall()


def large_orders(conn: sqlite3.Connection, min_cents: int) -> list[tuple]:
    rows = conn.execute("SELECT id, total_cents FROM orders").fetchall()
    return [row for row in rows if row[1] >= min_cents]
