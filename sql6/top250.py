#!/Users/valeria/src/morning-ninjas/venv/bin/python3

import argparse
from configparser import ConfigParser

import psycopg2


class MoviesModel:

    def __init__(self):
        self._conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='top250movies',
        user='postgres',
        password='postgres')




def perform_query(movie_name):
    # read connection parameters

    with psycopg2.connect(
        host='localhost',
        port=5432,
        database='top250movies',
        user='postgres',
        password='postgres') as conn:


        with conn.cursor() as cur:

            query = f"select * from imdb_top where movie_name ilike '{movie_name}'"
            print(f"going to execute: {query}")

            cur.execute(query)
            results = cur.fetchall()
            return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n')
    parser.add_argument('--rating', '-r', type=float)

    args = parser.parse_args()
    if not args.__getattr__('name') and not args.__getattr__('rating'):
        print('Error: You have to provide one of --name of --rating')
    elif args.__getattr__('name') and args.__getattr__('rating'):
        print('Error: You have to provide only one of --name or --rating')
    else:
        results = perform_query(args.movie_name)
        print(results)


