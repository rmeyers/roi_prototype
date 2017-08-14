from flask import Flask #, url_for, render_template, request, redirect, flash, jsonify

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from database_setup import Base, Restaurant, MenuItem

# from flask import session as login_session
# import random, string

# # IMPORTS FOR THIS STEP
# from oauth2client.client import flow_from_clientsecrets
# from oauth2client.client import FlowExchangeError
# import httplib2
# import json
# from flask import make_response
# import requests

# # Declare client ID by referencing the JSON file downloaded from Google.
# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']

# engine = create_engine('sqlite:///restaurantmenu.db')
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind = engine)
# session = DBSession()

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def showHomepage():
    return "This page will show my homepage."

@app.route('/login')
def login():
    return "This page will be for logging into the app."

@app.route('/register')
def register():
    return "This page will be for signing up for the app."

@app.route('/user/<int:user_id>/dashboard')
def showDashboard(user_id):
    return "This page will show the projects for user %s." % user_id

@app.route('/user/<int:user_id>/project/<int:project_id>/inputs')
def showInputs(user_id, project_id):
    return "This page will show the inputs for project {0} from user {1}".format\
        (unicode(str(project_id),'utf-8'),unicode(str(user_id),'utf-8'))

@app.route('/user/<int:user_id>/project/<int:project_id>/results')
def showResults(user_id, project_id):
    return "This page will show the results for project {0} from user {1}".format\
        (unicode(str(project_id),'utf-8'),unicode(str(user_id),'utf-8'))

@app.route('/user/<int:user_id>/compare')
def compareSelect(user_id):
    return "This will be the compare page for user %s." % user_id

@app.route('/user/<int:user_id>/compare/<int:project_id_1>/<int:project_id_2>/<int:project_id_3>')
def compareResults(user_id, project_id_1, project_id_2, project_id_3):
    return "This page will show the results for projects being compare for user {0}, 1st project: \
        {1}, 2nd project: {2}, third project: {3}.".format(unicode(str(user_id), 'utf-8'), \
        unicode(str(project_id_1), 'utf-8'), unicode(str(project_id_2), 'utf-8'), \
        unicode(str(project_id_3), 'utf-8'))

# Create a state token to prevent request forgery.
# Store it in the session for later validation.
# @app.route('/login')
# def showLogin():
#     state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
#     login_session['state'] = state
#     return render_template('login.html', STATE=state)


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
    # app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)




