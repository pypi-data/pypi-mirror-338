# Interactive Connectivity Establishment (ICE) in Python

This project implements ICE (RFC 5245) in Python to establish connections between two servers behind NAT.

## Features
- STUN-based public IP discovery
- ICE candidate gathering
- Signaling mechanism for exchanging candidates
- NAT traversal using UDP
- Sends a "Hello" message upon successful connection

## Installation
```sh
pip install ice-python
```

## Usage
```sh
python main.py
```

## License
This project is licensed under the MIT License.
