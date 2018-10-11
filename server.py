from flask import Flask, jsonify
from cmphoroscope import CMPHoroscope

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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

# Today's Horoscope Hindi
@app.route('/horoscope/today-hindi/<sunsign_en>/<sunsign_hn>/<language>', methods=['GET'])
def today_horoscope_route_hindi(sunsign_en, sunsign_hn, language):
    result = dict(CMPHoroscope.get_todays_horoscope_hindi(sunsign_en, sunsign_hn, language))
    #result = dict(CMPHoroscope.get_test())
    return jsonify(date=result['date'],
            sunsign_en=result['sunsign english'],
            sunsign_hn=result['sunsign hindi'],
            horoscope=result['horoscope'])

# Tomorrow's Horoscope Hindi
@app.route('/horoscope/tomorrow-hindi/<sunsign_en>/<sunsign_hn>/<language>', methods=['GET'])
def tomorrow_horoscope_route_hindi(sunsign_en, sunsign_hn, language):
    result = dict(CMPHoroscope.get_tomorrow_horoscope_hindi(sunsign_en, sunsign_hn, language))
    #result = dict(CMPHoroscope.get_test())
    return jsonify(date=result['date'],
            sunsign_en=result['sunsign english'],
            sunsign_hn=result['sunsign hindi'],
            horoscope=result['horoscope'])

# Yesterday's Horoscope Hindi
@app.route('/horoscope/yesterday-hindi/<sunsign_en>/<sunsign_hn>/<language>', methods=['GET'])
def yesterday_horoscope_route_hindi(sunsign_en, sunsign_hn, language):
    result = dict(CMPHoroscope.get_yesterday_horoscope_hindi(sunsign_en, sunsign_hn, language))
    #result = dict(CMPHoroscope.get_test())
    return jsonify(date=result['date'],
            sunsign_en=result['sunsign english'],
            sunsign_hn=result['sunsign hindi'],
            horoscope=result['horoscope'])

# Weekly Horoscope Hindi
@app.route('/horoscope/weekly-hindi/<sunsign_en>/<sunsign_hn>/<language>', methods=['GET'])
def weekly_horoscope_route_hindi(sunsign_en, sunsign_hn, language):
    result = dict(CMPHoroscope.get_weekly_horoscope_hindi(sunsign_en, sunsign_hn, language))
    #result = dict(CMPHoroscope.get_test())
    return jsonify(date=result['date'],
            sunsign_en=result['sunsign english'],
            sunsign_hn=result['sunsign hindi'],
            horoscope=result['horoscope'])

# Monthly Horoscope Hindi
@app.route('/horoscope/monthly-hindi/<sunsign_en>/<sunsign_hn>/<language>', methods=['GET'])
def monthly_horoscope_route_hindi(sunsign_en, sunsign_hn, language):
    result = dict(CMPHoroscope.get_monthly_horoscope_hindi(sunsign_en, sunsign_hn, language))
    #result = dict(CMPHoroscope.get_test())
    return jsonify(date=result['date'],
            sunsign_en=result['sunsign english'],
            sunsign_hn=result['sunsign hindi'],
            horoscope=result['horoscope'])

# Yearly Horoscope Hindi
@app.route('/horoscope/yearly-hindi/<sunsign_en>/<sunsign_hn>/<language>', methods=['GET'])
def yearly_horoscope_route_hindi(sunsign_en, sunsign_hn, language):
    result = dict(CMPHoroscope.get_yearly_horoscope_hindi(sunsign_en, sunsign_hn, language))
    #result = dict(CMPHoroscope.get_test())
    return jsonify(date=result['date'],
            sunsign_en=result['sunsign english'],
            sunsign_hn=result['sunsign hindi'],
            horoscope=result['horoscope'])

##########################################################

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