import psycopg2

local = {
    'host': 'localhost',
    'db': 'integra',
    'username': 'postgres',
    'password': '12345'
}

dev = {
    'host': '10.10.11.30',
    'db': 'postgres',
    'username': 'postgres',
    'password': 'pg2020inteGra!#'
}

prod = {
    'host': '95.216.225.187',
    'db': 'postgres',
    'username': 'postgres',
    'password': 'pg2020inteGra!#'
}

database = local

connection = psycopg2.connect(host=database['host'], database=database['db'], user=database['username'],
                              password=database['password'])
