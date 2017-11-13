from flask import Flask, render_template
import urllib2
import json

my_app = Flask(__name__)


@my_app.route("/")
def root():
    u = urllib2.urlopen("")
    data = u.read()
    dic = json.loads(data)
    return render_template('site.html', name = dic['Title'], pic = dic['ImageURL'], info = dic['Description'])

    
if __name__ == '__main__':
    my_app.debug = True
    my_app.run()

