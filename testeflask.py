from flask.views import View

class MyRequest(View):
    def dispatch_request(self):
        name = request.args.get('name', 'Damyan')
        return 'Hello, %s!' % name

app.add_url_rule(
    '/say-hi', view_func=MyRequest.as_view('my_request')
)