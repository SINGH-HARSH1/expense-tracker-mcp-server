from docutils.parsers.rst.directives.tables import ListTable
from fastmcp import FastMCP
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "expenses.db")
CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), "categories.json")

mcp = FastMCP("ExpenseTracker")


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                         date Text NOT NULL, 
                                                         amount REAL NOT NULL, 
                                                         category TEXT NOT NULL, 
                                                         subcategory TEXT DEFAULT '', 
                                                         note TEXT DEFAULT '')
                    """)
        conn.commit()


init_db()


@mcp.tool()
def add_expense(date: str, amount: float, category: str, subcategory: str, note: str) -> dict:
    """Add an expense to the database."""
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO expenses(date, amount, category, subcategory, note) VALUES (?, ?, ?, ?, ?)",
                    (date, amount, category, subcategory, note))
        conn.commit()
        return {"status": "200", "message": "Expense addition Successful", "id": cur.lastrowid}


@mcp.tool()
def list_expenses(start_date: str, end_date: str) -> list:
    """List expenses entries within an inclusive date range."""
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, date, amount, category, subcategory, note FROM expenses WHERE date BETWEEN ? AND ?",
                    (start_date, end_date))
        conn.commit()
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]


@mcp.tool()
def summarize_expenses(start_date: str, end_date: str, category=None) -> list:
    """Summarize expenses by category within an inclusive date range."""
    with sqlite3.connect(DB_PATH) as conn:
        query = "SELECT category, SUM(amount) AS total_amount FROM expenses WHERE date BETWEEN ? AND ?"
        params = [start_date, end_date]
        if category:
            query += " AND category = ?"
            params.append(category)

        query += " GROUP BY category ORDER BY category ASC"

        cur = conn.cursor()
        cur.execute(query, params)
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]


@mcp.resource("expense://categories", mime_type="application/json")
def categories():
    # Read fresh each time so that we can edit file without restarting
    with open(CATEGORIES_PATH, "r", encoding='utf-8') as f:
        return f.read()


if __name__ == "__main__":
    mcp.run()
