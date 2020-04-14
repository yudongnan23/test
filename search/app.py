from flask import Flask, render_template, request
from db_manager import query_movie_by_name
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, validators
from spider import start_spider


app = Flask(__name__)
app.secret_key = 'lbj23'


class IndexForm(FlaskForm):
    search = TextField([validators.Required('请输入搜索关键词')])
    submit = SubmitField('搜索')


@app.route('/index')
def hello_world():
    index_form = IndexForm()
    return render_template("index.html", form=index_form)


@app.route("/result/", methods=["GET"])
def get_result():
    index_form = IndexForm()
    title = request.args.get("q")
    ok = True
    if title:
        result_data = query_movie_by_name(title, all=True)
    else:
        result_data = ""
        ok = False
    if not result_data:
        ok = False
    return render_template("index.html", form = index_form, movies=result_data, ok=ok)


@app.route("/Fsearch/", methods=['POST'])
def query_text():
    text = request.form.get('q')
    response = ''
    if text:
        response = query_movie_by_name(text)
    return response


if __name__ == '__main__':
    # 执行爬虫
    start_spider()
    # flask服务启动
    app.run(debug=True)
