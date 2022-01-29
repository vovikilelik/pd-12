from flask import Flask, request, render_template

from app_settings import AppSettings
from candidates import Candidates

app = Flask('__name__')

settings = AppSettings()
settings.load_from_file('res/settings.json')

candidates = Candidates()
candidates.load_from_file('res/candidates.json')


@app.route('/')
def index():
    return 'Приложение работает' if settings.online else 'Приложение не работает'


@app.route('/candidate/<int:ident>')
@app.route('/<int:ident>')
def candidate_view(ident):
    record = candidates.get_by_id(int(ident))
    return render_template('candidate.html', **record.map()) if record is not None else render_template('404.html')


@app.route('/search')
def search_view():
    args = request.args

    if len(args) == 0:
        return render_template('404.html', message='Введите хотя бы один поисковый запрос!')

    records = candidates.search_by_text(case_sensitive=settings.case_sensitive, limit=settings.limit, **args)

    represent_text = f'Найдено по {", ".join(args)}: {len(records)}'
    return render_template('list.html', records=records, represent_text=represent_text)


@app.route('/skill/<skill>')
def skill_view(skill: str):
    records = candidates.search_by_skill(skill, limit=settings.limit)

    represent_text = f'Найдено со скиллом {skill}: {len(records)}'
    return render_template('list.html', records=records, represent_text=represent_text)


@app.route('/list')
def list_view():
    return render_template('list.html', records=candidates.get_list(), represent_text="Все кандидаты")


app.run()

