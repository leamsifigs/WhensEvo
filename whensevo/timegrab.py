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

@bp.route('/jsonGrab')
def rawgrab():
    currentDate = datetime.datetime.now(datetime.UTC)
    evoDate = datetime.datetime(2025, 8, 1, 10, tzinfo = pytz.utc)
    timeUntilEVO = evoDate - currentDate
    
    return timeUntilEVO
#   todo update this so there's a jason response? Idk. seems like a dumb way to go about this 
#   but if it works, it works i guess. There doesnt seem to be a way to deal with this outside 
#   of using promises but i'm not sure I want to learn how to do that riught now. should the 
#   javascript be inside the jinja or should it be inside of its own folder. does it belong in 
#   templates? much to thinkabout