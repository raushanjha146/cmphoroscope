from lxml import html
import requests
#from urllib2 import urlopen
#from bs4 import BeautifulSoup
import re

####################################################################
# API
####################################################################

class CMPHoroscope:
		
    @staticmethod
    def get_todays_horoscope_hindi1(sunsign_en, sunsign_hn, language):
        print("hi")
		url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-dainik-rashiphal"
        #print "----->" + url_hindi
        #url_hindi = "https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/"
        url_english = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign_en
        ######## for Date ################
        response = requests.get(url_english)
        #print("-2-->" + response.content)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        #print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        #print("-4-->" + date)

        ######### fro Horoscope ################
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib2.Request(url_hindi, headers=hdr)
        try:
            web_page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print "--------------" +e.fp.read()
        #web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        #print "---TODAY---"
        for extract_div in soup.findAll("div", {"id": "today1"}):
            horoscope = extract_div.text
        #print horoscope
        horoscope = horoscope.replace("\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign-english': sunsign_en,
            'sunsign-hindi': sunsign_hn
        }

        return dict

		
    @staticmethod
    def get_todays_horoscope(sunsign):
        print("hi")
        url = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        date = date.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_weekly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        week = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        week = week.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
        dict = {
            'week': week,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_monthly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        month = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        month = month.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()[1]"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
        dict = {
            'month': month,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_yearly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        year = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        year = year.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
        dict = {
            'year': year,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_tomorrow_horoscope(sunsign):
        print("hi")
        url = "http://www.ganeshaspeaks.com/horoscopes/tomorrow-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        date = date.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_yesterday_horoscope(sunsign):
        print("hi")
        url = "http://www.ganeshaspeaks.com/horoscopes/yesterday-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        date = date.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict