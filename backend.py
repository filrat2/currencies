# -*- coding: utf-8 -*-

# import needed modules
from flask import render_template, request
from datetime import date
import json
import plotly
import plotly.express as px

from database import app, db_nbp, Currency, CurrencyDayMidRate


# define endpoints
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


pln = Currency(id=0, name="polski złoty", code="PLN")


@app.route("/comparison", methods=['GET', 'POST'])
def comparison():
    resp = None
    currencies = Currency.query.all()
    currencies.append(pln)

    if request.method == "POST":
        resp = dict(request.form)
        first_currency_id = int(request.form.get('first_currency'))
        second_currency_id = int(request.form.get('second_currency'))

        if first_currency_id != 0:
            first_currency = CurrencyDayMidRate.query.filter_by(
                    currency_id=first_currency_id,
                    date=date.today()
                ).first()
        else:
            first_currency = CurrencyDayMidRate(mid_rate=1.00)

        if second_currency_id != 0:
            second_currency = CurrencyDayMidRate.query.filter_by(
                    currency_id=second_currency_id,
                    date=date.today()
                ).first()
        else:
            second_currency = CurrencyDayMidRate(mid_rate=1.00)

        first_currency_midrate = first_currency.mid_rate
        second_currency_midrate = second_currency.mid_rate

        if first_currency_midrate and second_currency_midrate:
            compare_result = first_currency_midrate - second_currency_midrate

        resp["first_currency"] = [c for c in currencies if c.id == first_currency_id][0].code
        resp["second_currency"] = [c for c in currencies if c.id == second_currency_id][0].code
        resp["compare_result"] = compare_result

    return render_template('comparison.html', resp=resp, currencies=currencies)


@app.route("/trade", methods=['GET', 'POST'])
def trade():
    resp = None

    currencies = Currency.query.all()
    currencies.append(pln)

    if request.method == "POST":
        resp = dict(request.form)
        id_sell = int(request.form.get('sell'))
        id_buy = int(request.form.get('buy'))
        count = float(request.form.get('count', 0))
        resp["count"] = float(count)
        if id_sell != 0:
            sell_c = CurrencyDayMidRate.query.filter_by(
                    currency_id=id_sell,
                    date=date.today()
                ).first()
        else:
            sell_c = CurrencyDayMidRate(mid_rate=1.00)

        if id_buy != 0:
            buy_c = CurrencyDayMidRate.query.filter_by(
                    currency_id=id_buy,
                    date=date.today()
                ).first()
        else:
            buy_c = CurrencyDayMidRate(mid_rate=1.00)

        if sell_c and buy_c and count:
            sell_value = sell_c.mid_rate
            buy_value = buy_c.mid_rate

            amount = (sell_value * count) / buy_value
            resp["amount"] = amount

            resp["sell"] = [c for c in currencies if c.id == id_sell][0].code
            resp["buy"] = [c for c in currencies if c.id == id_buy][0].code

    return render_template('trade.html', resp=resp, currencies=currencies)


@app.route("/table",  methods=['GET', 'POST'])
def table():
    query = db_nbp.session.query(Currency, CurrencyDayMidRate).\
            join(CurrencyDayMidRate,
                 Currency.id == CurrencyDayMidRate.currency_id).filter_by(
                     date=date.today()
                 ).all()

    return render_template('table.html', currencies=query)


@app.route("/plot", methods=['GET', 'POST'])
def plot():

    currency_id = 8
    currencies = Currency.query.all()
    if request.method == "POST":
        currency_id = int(request.form.get('currency'))

    currency = {}
    currency['name'] = [c for c in currencies if c.id == currency_id][0].name
    currency['code'] = [c for c in currencies if c.id == currency_id][0].code

    query = CurrencyDayMidRate.query.filter_by(
            currency_id=currency_id,
        ).order_by(CurrencyDayMidRate.date.asc()).all()

    df = {'date': [], 'mid_rate': []}

    for currency_day_midrate in query:
        df['date'].append(currency_day_midrate.date)
        df['mid_rate'].append(currency_day_midrate.mid_rate)

    fig = px.line(df, x='date', y='mid_rate',
                  labels={
                      "date": "Data",
                      "mid_rate": "Kurs (PLN)"
                      },
                  )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('plot.html', graphJSON=graphJSON,
                           currencies=currencies, currency=currency)
