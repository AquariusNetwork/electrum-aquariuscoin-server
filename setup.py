from setuptools import setup

setup(
    name="electrum-aquariuscoin-server",
    version="1.0",
    scripts=['run_electrum_aquariuscoin_server.py','electrum-aquariuscoin-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumaquariuscoinserver':'src'
        },
    py_modules=[
        'electrumaquariuscoinserver.__init__',
        'electrumaquariuscoinserver.utils',
        'electrumaquariuscoinserver.storage',
        'electrumaquariuscoinserver.deserialize',
        'electrumaquariuscoinserver.networks',
        'electrumaquariuscoinserver.blockchain_processor',
        'electrumaquariuscoinserver.server_processor',
        'electrumaquariuscoinserver.processor',
        'electrumaquariuscoinserver.version',
        'electrumaquariuscoinserver.ircthread',
        'electrumaquariuscoinserver.stratum_tcp',
        'electrumaquariuscoinserver.stratum_http'
    ],
    description="aquariuscoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.deg",
    maintainer="aquariuscoin",
    maintainer_email="support@aquariuscoin.org",
    license="GNU Affero GPLv3",
    url="https://github.com/aquariuscoin/electrum-aquariuscoin-server/",
    long_description="""Server for the Electrum Lightweight aquariuscoin Wallet"""
)


