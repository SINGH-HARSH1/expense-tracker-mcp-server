# Expense Tracker MCP Server 💰

This is a Model Context Protocol (MCP) server designed to connect with **Claude Desktop** and other MCP clients. It enables users to manage their personal finances using natural language.

## 🌟 The Vision
The ultimate goal of this project is to serve as the financial brain for an **Integrated AI Agent (Personal Assistant)**. This assistant will utilize a small, high-performance local model designed to run efficiently on any device (mobile, laptop, or IoT), ensuring your financial data remains private, secure, and accessible offline.

---

## 🛠 Initial Tools (Available Now)

The server currently exposes the following capabilities to the AI:

1.  **Add Expense**: Record new spending with details including `amount`, `category`, `date`, and `description`.
2.  **List Expenses**: Retrieve records with the ability to filter by **date range** or **category**.
3.  **Summarize Expenses**: Generate a financial overview for any period, including total spending and a breakdown by category.
4.  **Edit Expense**: Modify details of an existing record (e.g., correcting an amount or updating a description).
5.  **Delete Expense**: Completely remove an entry from the records.
6.  **Credit Expense (Income)**: Track money coming in to maintain a complete picture of cash flow.

---

## 🚀 Future Roadmap

These features are planned to transform the tracker into a proactive financial advisor:

* **View Balance**: Instant calculation of `Total Income - Total Expenses`.
* **Create Budget**: Set spending limits for specific categories and track progress.
* **Alert Notifications**: Proactive warnings when spending nears or exceeds budget limits.
* **Export Data**: Export your database to **CSV** or **Excel** for external bookkeeping.
* **Visual Reports**: Generation of charts and spending trend visualizations.

---

## ⚙️ Configuration

To use this with Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ExpenseTracker": {
      "command": "absolute path to uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "absolute path to main mcp file"
      ],
      "env": {
        "PATH": "Path to nodejs (Optional, if not already in system PATH)"
      },
      "transport": "stdio",
      "type": null,
      "cwd": null,
      "timeout": null,
      "description": null,
      "icon": null,
      "authentication": null
    }
  }
}