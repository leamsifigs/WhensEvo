import functools
import datetime
import pytz

from flask import (
    Blueprint, flash, g, redirect, render_template, url_for
)

bp = Blueprint("timegrab",  __name__, url_prefix='/time')

@bp.route('/grab')
def grab():
    currentDate = datetime.datetime.now(datetime.UTC)
    evoDate = datetime.datetime(2025, 8, 1, 10, tzinfo = pytz.utc)
    timeUntilEVO = evoDate - currentDate
    
    return render_template('timegrab/date.html' , timeUntilEVO=timeUntilEVO)

@bp.route('/rawgrab')
def rawgrab():
    currentDate = datetime.datetime.now(datetime.UTC)
    evoDate = datetime.datetime(2025, 8, 1, 10, tzinfo = pytz.utc)
    timeUntilEVO = evoDate - currentDate
    
    return str(timeUntilEVO)