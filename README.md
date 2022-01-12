# Simple traceroute
## About
A simple traceroute implementation in Python.
## Requirements

Python 3.x

## Installation
1. Clone this repository:
```bash
git clone https://github.com/kirill-ivanov-a/simple-traceroute.git
```
2. Go to project directory:
```bash
cd simple-traceroute/
```
## Usage
```bash
usage: sudo python3 -m traceroute [-h] [--max-hops NUM] [--first-hop NUM] [--port PORT] dest

positional arguments:
  dest                  destination host

optional arguments:
  -h, --help            show this help message and exit
  --max-hops NUM, -m NUM
                        set maximal hop number (default: 64)
  --first-hop NUM, -f NUM
                        set initial hop number (TTL) (default: 1)
  --port PORT, -p PORT  set destination port (default: 33434)
```
