import psycopg2
from flask import Flask, request, jsonify

app = Flask("bank_app")

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bank",
    user="postgres",
    password="postgres")


if __name__ == '__main__':
    app.run(debug=True)


# Accounts - 2
@app.route('/api/accounts')
def accounts():
    allowed_args = ('from_balance', 'to_balance', 'from_max_limit', 'to_max_limit')
    if request.args and not set(request.args).issubset(allowed_args):
        return app.response_class(status=400)

    # for