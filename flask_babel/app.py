from flask import Flask, render_template, request
from flask_babel import Babel, get_locale, format_date, format_datetime,gettext
from datetime import date, datetime


app = Flask(__name__,template_folder='template')
babel = Babel(app)


@babel.localeselector
def localeselector():
    # return 'tr'
    return request.accept_languages.best_match(["en_US", "es_ES"])


@app.route("/")
def index():
    # return '<h1>Locale: {}</h1>'.format(get_locale())
    d = date(2022, 1, 9)
    dt = datetime(2023, 5, 19, 17, 30)

    local_date = format_date(d)
    local_datetime = format_datetime(dt, "short")
    
    
    firat = gettext('Firat')
    babylon = gettext('Babylon')

    return render_template(
        "index.html", Locale=get_locale(), Local_date=local_date, Local_datetime=local_datetime,firat=firat,babylon=babylon)


if __name__ == "__main__":
    app.run(debug=True)
