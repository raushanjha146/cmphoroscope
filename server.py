from flask import Flask, jsonify
from cmphoroscope import CMPHoroscope

app = Flask(__name__)


############################################
# Index
############################################

@app.route('/', methods=['GET'])
def index_route():
    return jsonify({
        'author': 'Raushan Kumar',
        'author_url': 'http://raushan-kumar.github.io/',
        'base_url': 'cmp-horoscope-api.herokuapp.com',
        'project_name': 'CMPHoroscope API',
        'project_url': 'http://raushan-kumar.github.io/CMPHoroscope-API'
    })


############################################
# Horoscopes
###########################################

			
# Todays' Horoscope
@app.route('/horoscope/today-hindi1/<sunsign_en>/<sunsign_hn>/<language>', methods=['GET'])
def today1_horoscope_route(sunsign_en, sunsign_hn, language):
    result = dict(CMPHoroscope.get_todays_horoscope_hindi1(sunsign_en, sunsign_hn, language))
    return jsonify(date=result['date'],
                   sunsign=result['sunsign'],
                   horoscope=result['horoscope'])   
   
# Todays' Horoscope
@app.route('/horoscope/today/<sunsign>', methods=['GET'])
def today_horoscope_route(sunsign):
    result = dict(CMPHoroscope.get_todays_horoscope(sunsign))
    return jsonify(date=result['date'],
                   sunsign=result['sunsign'],
                   horoscope=result['horoscope'])

# Tomorrow' Horoscope
@app.route('/horoscope/tomorrow/<sunsign>', methods=['GET'])
def tomorrow_horoscope_route(sunsign):
    result = dict(CMPHoroscope.get_tomorrow_horoscope(sunsign))
    return jsonify(date=result['date'],
                   sunsign=result['sunsign'],
                   horoscope=result['horoscope'])

# Yesterday' Horoscope
@app.route('/horoscope/yesterday/<sunsign>', methods=['GET'])
def yesterday_horoscope_route(sunsign):
    result = dict(CMPHoroscope.get_yesterday_horoscope(sunsign))
    return jsonify(date=result['date'],
                   sunsign=result['sunsign'],
                   horoscope=result['horoscope'])

# Current Week Horoscope
@app.route('/horoscope/week/<sunsign>', methods=['GET'])
def weekly_horoscope_route(sunsign):
    result = dict(CMPHoroscope.get_weekly_horoscope(sunsign))
    return jsonify(week=result['week'],
                   sunsign=result['sunsign'],
                   horoscope=result['horoscope'])


# Current Month Horoscope
@app.route('/horoscope/month/<sunsign>', methods=['GET'])
def monthly_horoscope_route(sunsign):
    result = dict(CMPHoroscope.get_monthly_horoscope(sunsign))
    return jsonify(month=result['month'],
                   sunsign=result['sunsign'],
                   horoscope=result['horoscope'])


# Current Year Horoscope
@app.route('/horoscope/year/<sunsign>', methods=['GET'])
def yearly_horoscope_route(sunsign):
    result = dict(CMPHoroscope.get_yearly_horoscope(sunsign))
    return jsonify(year=result['year'],
                   sunsign=result['sunsign'],
                   horoscope=result['horoscope'])


###########################################
# Start Flask
###########################################

if __name__ == "__main__":
    app.run()