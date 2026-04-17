from flask import Blueprint, render_template, request, redirect, url_for
from .db import get_db

bp = Blueprint("timegrab", __name__)


@bp.route('/')
def home():
    db = get_db()
    events = db.execute('SELECT id, name, target_date FROM events ORDER BY target_date').fetchall()
    return render_template('timegrab/home.html', events=events)


@bp.route('/add', methods=['POST'])
def add():
    name = request.form['name'].strip()
    target_date = request.form['target_date']
    if name and target_date:
        db = get_db()
        db.execute('INSERT INTO events (name, target_date) VALUES (?, ?)', (name, target_date))
        db.commit()
    return redirect(url_for('timegrab.home'))


@bp.route('/delete/<int:event_id>', methods=['POST'])
def delete(event_id):
    db = get_db()
    db.execute('DELETE FROM events WHERE id = ?', (event_id,))
    db.commit()
    return redirect(url_for('timegrab.home'))
