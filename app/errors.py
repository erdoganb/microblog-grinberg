from app import app, db
from flask import render_template, url_for


@app.errorhandler(404)
def page_not_found(error):
    print("anan")
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500