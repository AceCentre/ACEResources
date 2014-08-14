"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for
from pybtex.database.input import bibtex

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

app = Flask(__name__)

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    # Show search form
    # Show tag cloud
    # Show stats (n books in Oldham, n books in Oxford, n references with attachments)
    # Show most recent entries
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/bibfile/<bibfile>')
def show_bibfile(bibfile):    
    # Get All elements in a bibtex file
    # Present nicely - like the bibtexbrpwser.php does
    bib_data = parser.parse_file(bibfile+'.bib')
    return render_template('base.html',bib_data=bib_data)
    return 'Index Page'
   
@app.route('/bibentry/<bibentry>')
def show_bibentry(bibentry):
    # show the entry for a bibtex entry
    return 'User %s' % bibentry

@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        request.args.get('key', '')
        bib_data = parser.parse_file(bibfile+'.bib')
        # do some clever auto-detection of the kind of item it is..
        # text: search authors, abstract, tags, 
        # year: year
        # doi or isbn or some kind of url.. 
        # and options:
          #has attachments (or in our library) - true or false
        # search attachments
        # https://github.com/willowtreeapps/flask-solr
        # https://github.com/toastdriven/pysolr
        
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    parser = bibtex.Parser()
    app.run(debug=True)