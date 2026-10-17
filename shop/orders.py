import sqlite3


def get_orders(conn: sqlite3.Connection, customer_id: int) -> list[tuple]:
    return conn.execute(
        "SELECT id, total_cents FROM orders WHERE customer_id = ?", (customer_id,)
    ).fetchall()
