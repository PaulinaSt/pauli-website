def register():   
    if current_user.is_authenticated:
        return redirect(url_for('home')) 
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

def login():    
    if current_user.is_authenticated:
        return redirect(url_for('home')) 
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next') #optional
                return redirect(next_page) if next_page else redirect(url_for('home')) #redirect to next page if it exists,if not return to home
            else:
                 flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

def home():
    form = NewsletterForm()
    if form.validate_on_submit():
        subscriber = Newsletter(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()
        flash('You have been added to our newsletter list. Thank you', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', title="Newsletter", form=form)