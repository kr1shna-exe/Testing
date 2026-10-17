import sqlite3


def main(db_path: str) -> None:
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("UPDATE orders SET total_cents = 0 WHERE total_cents IS NULL")
    print(f"backfilled {cursor.rowcount} orders")
    conn.commit()


if __name__ == "__main__":
    main("shop.db")
