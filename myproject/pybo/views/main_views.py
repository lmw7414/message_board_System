from flask import Blueprint, url_for, request
from flask import render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return redirect(url_for('question._list'))
#redirect 입력받은 URL로 리다이렉트 해준다
#url_for 라우트가 설정된 함수명으로 URL을 역으로 찾아준다.


