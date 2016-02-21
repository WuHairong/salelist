# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    items=db().select(db.poster.ALL, orderby=db.poster.title)
    return locals()
#show each poster information:
#seller name, rating, email,phone
#poster title, category, date, image, description, price, status
def show():
    poster=db.poster(request.args(0, cast=int)) or redirect(URL('index'))
    seller=db.owners(db.owners.id==poster.owners_id)
    images=db(db.picture.poster_id==poster.id).select(db.picture.ALL, orderby=db.picture.title)
    return locals()


def ratingup():
    owner = db.picture[request.vars.id]
    new_rating = owner.rating+1
    owner.updata_record(rating=new_rating)
    return str(new_votes)

def ratingdown():
    owner = db.picture[request.vars.id]
    if(owner.rating > 0 ):
        new_rating = owner.rating-1
    else:
        new_rating = 0
    owner.updata_record(rating=new_rating)
    return str(new_votes)

def hello():
    return dict("hello world!")

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
