from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
from flask_login import current_user, login_required, logout_user

# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """Homepage."""
    return render_template(
        'home.jinja2',
        current_user = current_user,
        title="Homepage",
        description="Track your projects!"
    )

@home_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_bp.login'))