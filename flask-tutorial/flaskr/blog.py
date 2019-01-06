# The blog should list all posts, allow logged in users to create posts,
# and allow the author of a post to edit or delete it.

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
