# -*- coding: utf-8 -*-
#db = DAL("sqlite://storage.sqlite")
from gluon.tools import Auth
auth = Auth(db)

db.define_table('owners',
    #Field('associated_auth', 'reference auth_user'),
    Field('name', 'string'),
    Field('rating', 'integer', default=0),
    Field('email', 'string',requires = IS_EMAIL(error_message='invalid email!')),
    Field('phone', 'integer', requires = IS_MATCH('^[01]?[- .]?(\([2-9]\d{2}\)|[2-9]\d{2})[- .]?\d{3}[- .]?\d{4}$',
         error_message='not a phone number')),
    format='%(name)s')



db.define_table('poster',
   Field('title', 'string'),
   Field('owners_id', 'reference owners', readable=False, writable=False),
   Field('created_on', 'datetime'),
   Field('description', 'text'),
   Field('category', requires=IS_IN_SET(['Car','Bike','Book','Music','Outdoors','Household','Misc'])),
   Field('price', 'double'),
   Field('status', 'boolean'),
   format='%(title)s'
)

db.define_table('picture',
    Field('poster_id', 'reference poster', readable=False, writable=False),
    Field('title','string'),
    Field('pic', 'upload')
    )
