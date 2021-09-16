import psycopg2

prod = {
    'host': '95.216.225.187',
    'db': 'postgres',
    'username': 'postgres',
    'password': 'pg2020inteGra!#'
}

dev = {
    'host': '10.10.11.30',
    'db': 'postgres',
    'username': 'postgres',
    'password': 'pg2020inteGra!#'
}

local = {
    'host': '127.0.0.1',
    'db': 'integra',
    'username': 'postgres',
    'password': '12345'
}

database = prod

connection = psycopg2.connect(host=database['host'], database=database['db'], user=database['username'],
                              password=database['password'])
