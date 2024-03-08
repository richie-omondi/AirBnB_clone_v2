#!/usr/bin/python3
"""Importing Flask to run the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state():
    """Displays a html page with states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Displays a html page with citys of that state"""
    states_list = storage.all('State')
    cities_list = storage.all('City')

    val = "State.{}".format(id)

    cities = []

    if val in states_list:
        state_name = states_list[val].name
        for city in cities_list.values():
            if city.state_id == id:
                cities.append(city)
    else:
        cities = None
        state_name = None

    return render_template(
        "9-states.html", cities=cities, state_name=state_name)


@app.teardown_appcontext
def close(arg=None):
    """ Method to close the session """
    try:
        storage.close()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
