# The blog should list all posts, allow logged in users to create posts,
# and allow the author of a post to edit or delete it.

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p join user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/idex.html', posts=posts)

# The create view works the same as the auth register view.
# Either the form is displayed, the posted data is validated and added to
# the database, or an error is thrown.
@bp.route('/create', methods=('GET', 'POST'))
# The login_required decorator written earlier will redirect the user to the
# login page if they aren't already logged in.
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Blog title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
        db.execute(
            'INSERT INTO post (title, body, author_id)'
            ' VALUES (?, ?, ?)',
            (title, body, g.user['id'])
        )
        db.commit()
        return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
