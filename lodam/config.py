import pathlib


CONFIG = {
    'config_path': pathlib.Path('tests/config'),
    'default_auth_client': '3388ea36-4a4f-4821-900a-b574c8829d52',
    'env': 'production',

    'backends': {
        'default': {
            'backend': 'spinta.backends.postgresql:PostgreSQL',
            'dsn': 'postgresql://admin:admin123@localhost:54321/lodam',
        },
    },

    'manifests': {
        'default': {
            'backend': 'default',
            'path': pathlib.Path() / 'manifest',
        },
    },

    'environments': {
        'dev': {
            'default_auth_client': '3388ea36-4a4f-4821-900a-b574c8829d52',
        },
    },
}
