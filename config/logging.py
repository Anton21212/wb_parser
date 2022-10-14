from pathlib import Path

BASE_DIR = Path(__file__).parents[1]

LOG_DIR = BASE_DIR / 'log'
LOG_DIR.mkdir(parents=True, exist_ok=True)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # выключать или нет встроенное лолгирование django
    'formatters': { # как должен выглядить log
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': { # понимает что нужно записывать, от какого уровня и куда
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler', # создает файлы в зависимость от того, достигают ли они макс.размер.
            'filename': LOG_DIR / 'wb_parser.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7, # удаляет старые логи когда их 7
            'formatter': 'verbose',
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'wb_parser_debug.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': { # то, что будет логировать
        'django': {
            'handlers': ['file', 'debug_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'debug': {
            'handlers': ['file', 'debug_file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
