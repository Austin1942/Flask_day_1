from flask import config, render_template, request, redirect, url_for, flash
import requests
from flask_login import login_user, current_user, logout_user, login_required
from .forms import CheckForm
from . import bp as main

@main.route('/', methods=['GET'])
def index():
    return render_template("index.html.j2")



@main.route('/poki_find', methods=['GET', 'POST'])
def poki_find():
    form = CheckForm()
    new_list = []
    
    if request.method == 'POST' and form.validate_on_submit():
        poke_look = request.form.get('poke_look')
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_look}'
        response = requests.get(url)
        if response.ok:
            poke = response.json()
            if not response.json()['stats']:
                error_string=f'There is no info for {poke_look}'
                return render_template("poki_find.html.j2",error=error_string, form=form)
    
            poke_dict={
                'Pokemon_name':poke['forms'][0]['name'],
                'Base_HP':poke['stats'][0]['base_stat'],
                'Base_Attack':poke['stats'][1]['base_stat'],
                'Base_Defence':poke['stats'][2]['base_stat'],
                'Image_of_Pokemon':poke['sprites']['front_shiny']
            }
            new_list.append(poke_dict)
            return render_template("poki_find.html.j2",pmon=new_list, form=form)
        else:
            error_string="Well This Is Embarrassing..."
            render_template("poki_find.html.j2",error=error_string, form=form)
    return render_template('poki_find.html.j2', form=form)