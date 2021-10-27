from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')


@app.route('/poki_find', methods=['GET', 'POST'])
def poki_find():
    if request.method == 'POST':
        poke_look = request.form.get('poke_look')
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_look}'
        response = requests.get(url)
        if response.ok:
            poke = response.json()
            if not poke.get('forms'):
                error_string=f'There is no info for {poke_look}'
                return render_template("poki_find.html.j2",error=error_string)
    
            poke_dict={
                'Pokemon_name':poke['forms'][0]['name'],
                'Base_HP':poke['stats'][0]['base_stat'],
                'Base_Attack':poke['stats'][1]['base_stat'],
                'Base_Defence':poke['stats'][2]['base_stat'],
                'Image_of_Pokemon':poke['sprites']['front_shiny']
            }
        
            return render_template("poki_find.html.j2",pmon=poke_dict)
        else:
            error_string="Well This Is Embarrassing..."
            render_template("poki_find.html.j2",error=error_string)
    return render_template('poki_find.html.j2')