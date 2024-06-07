import os
from flask_admin import Admin
from models import db, User, Favorites, People, Planets, Vehicles
from flask_admin.contrib.sqla import ModelView

class FavoritesView(ModelView):
    column_list = ('user', 'person', 'planet', 'vehicle')
    column_labels = {
        'user': 'User',
        'person': 'Person',
        'planet': 'Planet',
        'vehicle': 'Vehicle'
    }
    column_formatters = {
        'user': lambda v, c, m, p: m.user.username,
        'person': lambda v, c, m, p: m.person.persons_name if m.person else '',
        'planet': lambda v, c, m, p: m.planet.description if m.planet else '',
        'vehicle': lambda v, c, m, p: m.vehicle.model if m.vehicle else ''
    }

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(FavoritesView(Favorites, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Vehicles, db.session))

    # You can duplicate that line to add new models
    # admin.add_view(ModelView(YourModelName, db.session))