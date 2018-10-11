from lxml import html
import requests
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

####################################################################
# API
####################################################################

class CMPHoroscope:

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