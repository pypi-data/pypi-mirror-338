# foundry-wrap

A Python wrapper for Foundry's forge scripts with dynamic interface generation and Safe transaction support.

## Features

- Dynamic interface generation for Foundry scripts
- Create and sign Safe transactions from Foundry scripts
- Cache and manage interfaces for reuse

## Installation & Usage

### Using with UV (Recommended)

Using foundry-wrap with [Astral's uv](https://github.com/astral-sh/uv) is the most convenient way to run it:

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Run foundry-wrap commands directly
uvx foundry-wrap --help
uvx foundry-wrap safe path/to/Script.s.sol
```

This creates a temporary isolated environment with all dependencies installed.

## Commands

- `uvx foundry-wrap run SCRIPT`: Process a script and handle interface generation
- `uvx foundry-wrap safe SCRIPT`: Process a script and create/submit a Safe transaction
- `uvx foundry-wrap list`: List all cached interfaces
- `uvx foundry-wrap clear-cache`: Clear the interface cache
- `uvx foundry-wrap config`: Configure foundry-wrap settings

## Requirements

- Python 3.8+
- For Safe features: web3, safe-eth-py, and other Ethereum-related packages

## License

[MIT License](LICENSE)
