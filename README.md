# Flask-Bitcoind

Flask-Bitcoind initializes an bitcoind JSON-RPC interface using Peter Todd's [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib) package.

## Installation

```
$ pip install flask-bitcoind
```

## Usage

```
import flask
from flask_bitcoind import BitcoindNode

app = flask.Flask(__name__)

bitcoind = BitcoindNode()
bitcoind.init_app(app)


@app.route('/')
def index():
    return str(bitcoind.rpc.getbestblockhash())
```
    