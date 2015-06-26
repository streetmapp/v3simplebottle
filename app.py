__author__ = 'spousty'


from bottle import route, run

@route('/')
def index():
    return "<h1> you're doing this</h1>
            <h2> just another test </h2>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
