# noinspection PyPackageRequirements
from bitcoin.rpc import Proxy


class BitcoindNode(object):
    def __init__(self, app=None):
        self.rpc = None
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('BITCOIND_CONF_FILE_PATH', None)
        self.rpc = Proxy(
            btc_conf_file=app.config['BITCOIND_CONF_FILE_PATH']
        )

    def estimate_smart_fee(self, conf_target, mode):
        # noinspection PyProtectedMember
        r = self.rpc._call('estimatesmartfee', conf_target, mode)
        return r
