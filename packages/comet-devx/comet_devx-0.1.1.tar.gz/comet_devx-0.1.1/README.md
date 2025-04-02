# Comet DevX Python SDK

A Python SDK for interacting with Compound V3 (Comet).  
This SDK provides a simple, high-level interface for:

- **Supplying** collateral to Comet.
- **Borrowing** the base asset.
- **Repaying** borrowed assets.
- Querying positions and market data.

---

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Initializing the Comet Instance](#initializing-the-comet-instance)
  - [Core Methods](#core-methods)
    - [Supply](#supply)
    - [Borrow](#borrow)
    - [Repay](#repay)
- [Configuration](#configuration)
- [Examples](#examples)
- [Development](#development)
- [License](#license)

---

## Overview

The Comet SDK is designed to streamline interactions with Compound V3 (Comet). It leverages Web3.py for blockchain communication and provides clear exceptions and transaction handling.  
The main class, `Comet`, initializes using a network identifier, a Web3 provider, and an optional account address, and it exposes methods to supply collateral, borrow assets, and repay loans.

---

## Installation

To install the Comet Python SDK, run:

```bash
pip install comet-devx
```


---

## Usage

### Initializing the Comet Instance

Import the `Comet` class from the SDK, create a Web3 instance, and then instantiate the class.

```python
from web3 import Web3
from comet import Comet  # Adjust the import as needed

# Connect to your RPC provider (e.g., Infura)
provider = Web3.HTTPProvider("https://sepolia.infura.io/v3/YOUR_INFURA_KEY")
web3 = Web3(provider)

# Optionally, set your account (checksum address)
account = web3.toChecksumAddress("0xYourAccountAddress")

# Create a Comet instance for the 'sepolia' network
comet = Comet(network="sepolia", web3=web3, account=account)
print(comet.get_network())  # Should output: "Connected to sepolia network"
```

### Core Methods

#### Supply

Supply an ERC20 asset as collateral to Comet.

```python
from web3 import Web3

# Example: Supply 1,000 USDC (USDC has 6 decimals)
usdc_address = web3.toChecksumAddress("0xA0b86991C6218B36C1d19D4a2E9Eb0CE3606EB48")
amount = Web3.toWei(1_000, 'mwei')  # or use your preferred conversion

try:
    receipt = await comet.supply(asset=usdc_address, amount=amount)
    print("Supply successful, receipt:", receipt)
except Exception as e:
    print("Supply failed:", e)
```

#### Borrow

Borrow the base asset from Comet.

```python
# Example: Borrow 100 USDC (assume base asset uses 6 decimals)
borrow_amount = Web3.toWei(100, 'mwei')
try:
    receipt = await comet.borrow(amount=borrow_amount)
    print("Borrow successful, receipt:", receipt)
except Exception as e:
    print("Borrow failed:", e)
```

#### Repay

Repay the borrowed base asset.

```python
# Example: Repay 50 USDC (using 6 decimals)
repay_amount = Web3.toWei(50, 'mwei')
try:
    receipt = await comet.repay(amount=repay_amount)
    print("Repay successful, receipt:", receipt)
except Exception as e:
    print("Repay failed:", e)
```

---

## Configuration

The SDK reads network-specific settings from a configuration module. You can customize the configuration by editing the configuration files under the `config/` directory.

- **NetworkConfig:**  
  Provides settings such as the Comet contract address and oracle configurations.  
- **ABI Files:**  
  The SDK loads the Comet ABI from the `abis/` directory. Ensure this file is present and updated.

---

## Examples

For more detailed examples, refer to the `examples/` directory which includes sample scripts demonstrating:

- Setting up the environment.
- Supplying collateral.
- Borrowing and repaying assets.
- Querying market data and positions.

---

## Development

### Setting Up the Environment

1. Clone the repository.
2. Install dependencies in editable mode:

   ```bash
   pip install -e ".[dev]"
   ```

3. Update configuration files under `config/` as needed.

### Running the SDK

Run your example scripts from the command line:

```bash
python examples/supply_example.py
```

### Contributing

Contributions are welcome!  
1. Fork the repository.  
2. Create a feature branch.  
3. Write tests and update documentation.  
4. Submit a pull request with your changes.

For major changes, please open an issue first to discuss the design.

