from flask import Blueprint, render_template, request
import random

bp = Blueprint(__name__, __name__, template_folder='templates')


def random_string(length=16):
    chars = 'abcdefghijklmnopqrstuvwxyz123456789'
    final_string = ''

    for i in range(0, length):
        final_string += chars[random.randint(0, len(chars)-1)]

    return final_string


@bp.route('/createnote', methods=['post','get'])
def show():
    if request.method == 'POST': #Important: 'POST' must be capitalized.
        if request.form.get('createnote'):
            text = request.form.get('notetext')

            with open('noteapp/notes/{}.note'.format(random_string()), 'w+') as _file:
                _file.write(text)

            _file.close()

    return render_template("createnote.html")
