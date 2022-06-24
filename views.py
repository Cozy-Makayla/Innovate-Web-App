from flask import(
    render_template,
    Blueprint,
    request
)

message_list = []

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/product')
def product():
    return render_template('product.html')

@views.route('/item')
def item():
    return render_template('item.html')

@views.route('/contacts')
def contacts():
    return render_template('contacts.html')

@views.route('/message', methods=["GET", "POST"])
def message():
    if request.method == "POST":
        task = request.form.get("Message")
        message_list.append(task)
        print(message_list)
        return render_template("message.html", message_list=message_list)
    return render_template('message.html')

@views.route('/about')
def about():
    return render_template('about.html')

