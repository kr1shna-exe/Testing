# Shop

Small order and pricing helpers.

## Orders

- `get_orders(conn, customer_id)` lists a customer's orders.
- `search_orders(conn, term)` finds orders whose note contains `term`.
- `large_orders(conn, min_cents)` lists orders at or above a total.
