from urlparse import urlparse

from flask import Flask, url_for, render_template
from flask import request, redirect, flash, jsonify
from flask import send_from_directory, Response, make_response

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Project, User

from flask import session as login_session
import random
import string

from os import environ as env, path
import json
import httplib2

from auth0.v3.authentication import GetToken
from auth0.v3.authentication import Users
from dotenv import load_dotenv
from functools import wraps

import constants

from dashboard import projects_from_db

engine = create_engine('sqlite:///capexprojectswithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

load_dotenv(path.join(path.dirname(__file__), ".env"))
# What is this stuff? Where does it come into play?

AUTH0_CALLBACK_URL = constants.AUTH0_CALLBACK_URL
AUTH0_CLIENT_ID = constants.AUTH0_CLIENT_ID
AUTH0_CLIENT_SECRET = constants.AUTH0_CLIENT_SECRET
AUTH0_DOMAIN = constants.AUTH0_DOMAIN


app = Flask(__name__)

noPageAccess = 'Hold up! It looks like you don\'t have access to this page!'


# Here we're using the /callback route.
@app.route('/callback')
def callback_handling():
    code = request.args.get(constants.CODE_KEY)

    if code is None:
        return redirect('/')

    get_token = GetToken(AUTH0_DOMAIN)
    auth0_users = Users(AUTH0_DOMAIN)
    token = get_token.authorization_code(AUTH0_CLIENT_ID,
                                         AUTH0_CLIENT_SECRET, code,
                                         AUTH0_CALLBACK_URL)
    access_token = token['access_token']
    user_info = json.loads(auth0_users.userinfo(access_token))

    # Check that the access token is valid.
    url = ('https://capextool.auth0.com/userinfo/?access_token=%s'
           % access_token)
    # Submit request, parse response
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    auth0Id = user_info['sub']
    if result['sub'] != auth0Id:
        response = make_response(
            json.dumps("Token's sub doesn't match sub from cURL."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # # Verify that the access token is valid for this app.
    # if result['issued_to'] != CLIENT_ID:
    #     response = make_response(
    #         json.dumps("Token's client ID does not match app's."), 401)
    #     response.headers['Content-Type'] = 'application/json'
    #     return response

    stored_access_token = login_session.get('access_token')
    stored_sub = login_session.get('profile', {}).get('sub')
    if stored_access_token is not None and auth0Id == stored_sub:
        response = make_response(json.dumps(
            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Add user info
    login_session[constants.PROFILE_KEY] = user_info

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['profile']['name'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    flash("you are now logged in under %s" % login_session['profile']['name'])

    return redirect('/user/%s/dashboard' % user_id)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in login_session:
            # Redirect to Login page here
            return redirect('/')
        return f(*args, **kwargs)

    return decorated


# Controllers API
@app.route('/')
@app.route('/home')
def showHomepage():
    return render_template('homepage.html', env=env)


@app.route('/user/<int:user_id>/dashboard')
@requires_auth
def dashboard(user_id):
    if user_id != login_session['user_id']:
        response = make_response(json.dumps(
            noPageAccess), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    projects_list = projects_from_db()
    return render_template('dashboard.html',
                           user=login_session[constants.PROFILE_KEY],
                           env=env, user_id=user_id,
                           projects_list=projects_list)


@app.route('/logout')
def logout():
    login_session.clear()
    parsed_base_url = urlparse(AUTH0_CALLBACK_URL)
    base_url = parsed_base_url.scheme + '://' + parsed_base_url.netloc
    return redirect('https://%s/v2/logout?returnTo=%s&client_id=%s' % (
        AUTH0_DOMAIN, base_url, AUTH0_CLIENT_ID))


@app.route('/user/<int:user_id>/project/<int:project_id>/inputs')
@requires_auth
def showInputs(user_id, project_id):
    if user_id != login_session['user_id']:
        response = make_response(json.dumps(
            noPageAccess), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    return render_template('inputs.html',
                           user=login_session[constants.PROFILE_KEY],
                           env=env, user_id=user_id, project_id=project_id)


@app.route('/user/<int:user_id>/project/<int:project_id>/results')
@requires_auth
def showResults(user_id, project_id):
    if user_id != login_session['user_id']:
        response = make_response(json.dumps(
            noPageAccess), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    return render_template('results.html',
                           user=login_session[constants.PROFILE_KEY],
                           env=env, user_id=user_id, project_id=project_id)


@app.route('/user/<int:user_id>/compare')
@requires_auth
def compareSelect(user_id):
    return "This will be the compare page for user %s." % user_id


@app.route('/user/<int:user_id>/compare/<int:project_id_1>/<int:project_id_2>/<int:project_id_3>')
@requires_auth
def compareResults(user_id, project_id_1, project_id_2, project_id_3):
    return "This page will show the results for projects being compare for user {0}, 1st project: \
        {1}, 2nd project: {2}, third project: {3}.".format(unicode(str(user_id), 'utf-8'), \
        unicode(str(project_id_1), 'utf-8'), unicode(str(project_id_2), 'utf-8'), \
        unicode(str(project_id_3), 'utf-8'))


# User Helper Functions
def createUser(login_session):
    email = login_session['profile']['name']
    newUser = User(email=email)
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=email).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

# @app.route('/gconnect', methods=['POST'])
# def gconnect():
#     if request.args.get('state') != login_session['state']:
#         response = make_response(json.dumps('Invalid state parameter'), 401)
#         response.headers['Content-type'] = 'application/json'
#         return response
#     code = request.data
#     try:
#         # Upgrading the authorization code into a credentials object
#         # This creates oauth flow object and adds client's secret key to it.
#         oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
#         # Specify with code message 'postmessage' that this is the one-time code flow
#         # that my server will be sending off.
#         oauth_flow.redirect_uris = 'postmessage'
#         # This exchanges the authorization code (one-time code) for a credentials object.
#         credentials = oauth_flow.step2_exchange(code)
#     except FlowExchangeError:
#         response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
#         response.headers['Content-type'] = 'application/json'
#         return response

#     # Check that the access token is valid
#     access_token = credentials.access_token
#     url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
#     h = httplib2.Http()
#     result = json.loads(h.request(url, 'GET')[1])

#     # If there was an error in the access token info, abort.
#     if result.get('error') is not None:
#         response = make_response(json.dumps(result.get('error')), 500)
#         response.headers['Content-type'] = 'application/json'
#         return response

#     # Verify that the access token is used for the intended user.
#     gplus_id = credentials.id_token['sub']
#     if result['user_id'] != gplus_id:
#         response = make_response(
#             json.dumps("Token's user ID doesn't match given user ID."), 401)
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     # Verify that the access token is valid for this app.
#     if result['issued_to'] != CLIENT_ID:
#         response = make_response(
#             json.dumps("Token's client ID does not match app's."), 401)
#         print "Token's client ID does not match app's."
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     stored_access_token = login_session.get('access_token')
#     stored_gplus_id = login_session.get('gplus_id')
#     if stored_access_token is not None and gplus_id == stored_gplus_id:
#         response = make_response(json.dumps('Current user is already connected.'),
#                                  200)
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     # Store the access token in the session for later use.
#     login_session['access_token'] = credentials.access_token
#     login_session['gplus_id'] = gplus_id

#     # Get user info
#     userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
#     params = {'access_token': credentials.access_token, 'alt': 'json'}
#     answer = requests.get(userinfo_url, params=params)

#     data = answer.json()

#     login_session['username'] = data['name']
#     login_session['picture'] = data['picture']
#     login_session['email'] = data['email']

#     output = ''
#     output += '<h1>Welcome, '
#     output += login_session['username']
#     output += '!</h1>'
#     output += '<img src="'
#     output += login_session['picture']
#     output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
#     flash("you are now logged in as %s" % login_session['username'])
#     print "done!"
#     return output


# # Making an API endpoint (GET request)
# @app.route('/restaurants/<int:restaurant_id>/menu/JSON')
# def restaurantMenuJSON(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
#     items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
#     return jsonify(MenuItems=[i.serialize for i in items])

# # Making an API endpoint (GET request)
# @app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
# def restaurantMenuItemJSON(restaurant_id, menu_id):
#     restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
#     item = session.query(MenuItem).filter_by(id = menu_id).one()
#     return jsonify(MenuItems=item.serialize)

# @app.route('/')
# @app.route('/restaurants/<int:restaurant_id>/')
# def restaurantMenu(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
#     items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)

#     return render_template('menu.html', restaurant=restaurant, items=items)

# # Task 1: Create route for newMenuItem function here

# @app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])
# def newMenuItem(restaurant_id):
#     if request.method == 'POST':
#         newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
#         session.add(newItem)
#         session.commit()
#         flash('New menu item created!')
#         return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
#     else:
#         return render_template('newmenuitem.html', restaurant_id=restaurant_id)
#     return "page to create a new menu item. Task 1 complete!"

# # Task 2: Create route for editMenuItem function here

# @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit',
#            methods=['GET', 'POST'])
# def editMenuItem(restaurant_id, menu_id):
#     editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
#     if request.method == 'POST':
#         if request.form['name']:
#             editedItem.name = request.form['name']
#         session.add(editedItem)
#         session.commit()
#         flash('Menu item edited successfully!')
#         return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
#     else:
#         # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
#         # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
#         return render_template(
#             'editMenuItem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)

# # Task 3: Create a route for deleteMenuItem function here

# @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET', 'POST'])
# def deleteMenuItem(restaurant_id, menu_id):
#     deletedItem = session.query(MenuItem).filter_by(id=menu_id).one()
#     if request.method == 'POST':
#         session.delete(deletedItem)
#         session.commit()
#         flash('Menu item deleted!')
#         return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
#     else:
#         # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
#         # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
#         return render_template(
#             'deleteMenuItem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=deletedItem)


if __name__ == '__main__':
    app.secret_key = constants.SECRET_KEY
    app.config['SERVER_NAME'] = '0.0.0.0'
    app.debug = True
    app.run(host=app.config['SERVER_NAME'], port=int(env.get('PORT', 5000)))
