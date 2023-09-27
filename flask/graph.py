from flask import Flask, render_template
import duckdb

app = Flask(__name__)

@app.route("/")
def homepage():
    # Define Plot Data
    labels = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    data = []

    #duckdb connect
    con = duckdb.connect(database='../duckdb/sales_bdd.duckdb', read_only=False)
    con.execute('SELECT * FROM total_revenue_per_month')

    for row in con.fetchall():
        data.append(row[2])

    con.close()

    # Return the components to the HTML template
    return render_template(
        template_name_or_list='graph.html',
        data=data,
        labels=labels,
    )


