from flask import Blueprint, render_template, redirect, url_for, flash, request
from ..forms import SignupForm, LoginForm
from flask_login import current_user, login_user
from ..models import User, db
from .. import login_manager


# Blueprint Configuration
login_bp = Blueprint(
    'login_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@login_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """Sign Up Page"""
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('home_bp.home'))
        flash('A user already exists with that email address.')
    return render_template(
        'signup.jinja2',
        title="Sign Up",
        form = form,
        description="Sign Up Description"
    )

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login Page."""
    if current_user.is_authenticated:
        return redirect(url_for("home_bp.home"))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("home_bp.home"))
        flash("Invalid username/password combination.")
        return redirect(url_for("login_bp.login"))
    return render_template(
        'login.jinja2',
        title="Login",
        form = form,
        description="Login description"
    )

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized user to Login page."""
    flash('You must be logged in to view that page')
    return redirect(url_for('login_bp.login'))