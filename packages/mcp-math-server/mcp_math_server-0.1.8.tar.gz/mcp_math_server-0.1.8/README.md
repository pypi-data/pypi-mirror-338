[![PyPI version](https://img.shields.io/pypi/v/mcp-math-server)](https://pypi.org/project/mcp-math-server/)
[![Python](https://img.shields.io/pypi/pyversions/mcp-math-server)](https://pypi.org/project/mcp-math-server/)
[![License](https://img.shields.io/pypi/l/mcp-math-server)](./LICENSE)

---

## ✅ `README.md` for `mcp-math-server`

```markdown
# 📐 MCP Math Server

An [MCP (Model Context Protocol)](https://modelcontextprotocol.io) server that provides basic arithmetic operations — addition, subtraction, multiplication, and division — to integrate easily with LLMs like Claude.

> Built using the official `mcp` Python SDK and `FastMCP`.

---

## 🚀 Features

- ✨ Claude/LLM-ready math tools
- 🔢 Four core operations: add, subtract, multiply, divide
- 🧠 Designed for seamless MCP integration
- 🐍 Easy CLI usage via `mcp-math` command

---

## 📦 Installation

You need Python 3.10 or later.

### Option 1: From PyPI (once published)

```bash
pip install mcp-math-server
```

Then run:

```bash
mcp-math
```

### Option 2: From source (for development)

```bash
git clone https://github.com/yourusername/mcp-math-server.git
cd mcp-math-server

# Recommended: use virtualenv or uv
python3 -m venv venv
source venv/bin/activate

pip install -e .
mcp-math
```

---

## 🧪 Usage

After running `mcp-math`, your server will expose these tools:

### 🔧 Tools

| Tool         | Description                        |
|--------------|------------------------------------|
| `add`        | Adds two numbers                   |
| `subtract`   | Subtracts one number from another  |
| `multiply`   | Multiplies two numbers             |
| `divide`     | Divides one number by another      |

---

## 🤖 Using with Claude Desktop

1. [Download Claude Desktop](https://claude.ai/download) if you haven’t.
2. Make sure your MCP server is running via:

```bash
mcp-math
```

3. In another terminal, register it with Claude:

```bash
mcp install $(which mcp-math) --name "Math Assistant"
```

4. Claude will now show “Math Assistant” as an available context/tool.

🧠 Example prompt in Claude:

> “Use the multiply tool from Math Assistant to calculate 12 × 6.”

---

## 🧰 Example MCP Inspector Test

You can also test it manually:

```bash
mcp dev mcp_math/server.py
```

Try calling:

```json
{
  "tool": "divide",
  "arguments": { "x": 100, "y": 5 }
}
```

---

## 📁 Project Structure

```
mcp-math-server/
├── mcp_math/
│   ├── __init__.py
│   └── server.py  # All MCP logic
├── pyproject.toml  # Package config
├── README.md       # You're reading this
```

---

## 🛠️ Development

Feel free to fork or clone this repo and add more math tools, logging, or context history!

### To build & publish to PyPI:

```bash
pip install build twine
python -m build
twine upload dist/*
```

---

## 📃 License

MIT © 2025 Ajinkya  
See [LICENSE](LICENSE) for details.

---

## 🙌 Contributions Welcome

If you have an idea or improvement, feel free to open an issue or pull request. Let's make LLMs better at math — together!
```

---

## ✅ Next Steps for You

- ✅ Save this `README.md` to your root folder
- ✅ Replace placeholder fields:
  - `https://github.com/yourusername/...`
  - Your name + email
- ✅ Add a `LICENSE` file (MIT recommended — I can generate one)

---

Would you like me to:
- Create a matching `LICENSE` file?
- Help write a `setup.cfg` or GitHub Actions CI?
- Add more advanced math (e.g. percentages, square roots)?

Let’s keep leveling it up 🚀