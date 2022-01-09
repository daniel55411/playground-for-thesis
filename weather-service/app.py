import datetime as dt
import random
from enum import Enum
from typing import Any
from typing import Mapping

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
cache = dict()


class Status(str, Enum):
    SUCCESS = 'success'
    ERROR = 'error'

    def __str__(self) -> str:
        return self.value


def _is_valid_date(date_str: str) -> bool:
    try:
        dt.date.fromisoformat(date_str)
    except ValueError:
        return False
    else:
        return True


def _get_temperature_from_cache(date: Any) -> float:
    if date not in cache:
        temperature = random.randint(-30, 30)
        temperature += round(random.random(), 1)
        cache[date] = temperature

    return cache[date]


def _change_temperature_in_cache(date: Any, value: float) -> None:
    cache[date] = value


def _get_temperature() -> Mapping[str, str]:
    date = request.args.get('date')

    if date is None:
        return {
            'status': Status.ERROR,
            'reason': 'Not specified date',
        }

    if not _is_valid_date(date):
        return {
            'status': Status.ERROR,
            'reason': 'Not valid input date',
        }

    return {
        'status': Status.SUCCESS,
        'result': _get_temperature_from_cache(date),
    }


def _change_temperature() -> Mapping[str, str]:
    date = request.form.get('date')
    temperature = float(request.form.get('temperature'))

    if date is None or temperature is None:
        return {
            'status': Status.ERROR,
            'reason': 'Not specified date or temperature',
        }

    if not _is_valid_date(date):
        return {
            'status': Status.ERROR,
            'reason': 'Not valid input date',
        }

    _change_temperature_in_cache(date, temperature)
    return {
        'status': Status.SUCCESS,
    }


@app.route('/api/v1/temperature', methods=['GET', 'POST'])
def temperature_api() -> Any:
    if request.method == 'GET':
        return _get_temperature()
    else:
        return _change_temperature()


@app.route('/admin/temperature')
def admin() -> str:
    return render_template(
        'admin.html',
        email=request.headers.get('X-Forwarded-Email'),
    )
