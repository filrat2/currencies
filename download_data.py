# -*- coding: utf-8 -*-

# import needed modules
import argparse
from sqlalchemy import exc
from requests import get
from datetime import datetime

from database import app, db_nbp, Currency, CurrencyDayMidRate


URL = "http://api.nbp.pl/api/exchangerates/tables/A/{start_date}/{end_date}/"


class DateValidationAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):

        try:
            values = datetime.strptime(values, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Niepoprawny format daty! Prawidłowy format daty "
                             "to: RRRR-MM-DD (standard ISO 8601)")

        setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser()
parser.add_argument('start_date', help=('Podaj początek zakresu dat do '
                                        'pobrania danych z Narodowego Banku '
                                        'Polskiego. Datę podaj w formacie '
                                        'RRRR-MM-DD (standard ISO 8601). Dane '
                                        'archiwalne o kursach walut dostępne '
                                        'są od 2 stycznia 2002 r.'),
                    action=DateValidationAction)
parser.add_argument('end_date', help=('Podaj koniec zakresu dat do '
                                      'pobrania danych z Narodowego Banku '
                                      'Polskiego. Datę podaj w formacie '
                                      'RRRR-MM-DD (standard ISO 8601). Dane '
                                      'archiwalne o kursach walut dostępne '
                                      'są od 2 stycznia 2002 r.'),
                    action=DateValidationAction)
args = parser.parse_args()

time_delta = args.end_date - args.start_date

if time_delta.days > 93:
    raise ValueError("Zakres czasowy nie może obejmować przedziału dłuższego, "
                     "niż 93 dni. Podaj inny, krótszy zakres czasowy.")


start_date = datetime.strftime(args.start_date, '%Y-%m-%d')
end_date = datetime.strftime(args.end_date, '%Y-%m-%d')

r = get(URL.format(start_date=start_date, end_date=end_date))
response = r.json()

with app.app_context():
    for day in response:
        history_date = day['effectiveDate']
        currencies_day_midrates = []

        for rate in day['rates']:
            currency = Currency.query.filter_by(code=rate['code']).first()

            if not currency:
                currency = Currency(name=rate['currency'], code=rate['code'])
                db_nbp.session.add(currency)
                db_nbp.session.commit()

            currency_day_midrate = CurrencyDayMidRate(
                currency_id=currency.id,
                mid_rate=rate['mid'],
                date=datetime.strptime(history_date, '%Y-%m-%d')
            )
            currencies_day_midrates.append(currency_day_midrate)
        try:
            db_nbp.session.add_all(currencies_day_midrates)
            db_nbp.session.commit()

        except exc.IntegrityError:
            db_nbp.session.rollback()
