from app import app
from flask import request, redirect, render_template, url_for
import tweepy

#  Chris
access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''

@app.route('/index.html',methods = ['POST', 'GET'])
def home():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

	if request.method == 'POST':
		result = request.form
		user = result['Handle']
		target_user = ('@'+ user)
		api.update_status('@cfrichardson1 Analyze:'+target_user)
	return render_template('index.html')

@app.route('/pro_gun_control.html')
def pro_gc():
	return render_template('Pro_GC.html')

@app.route('/against_gun_control.html')
def against_gc():
	return render_template('Against_GC.html')

@app.route('/resources.html')
def resources():
	return render_template('resources.html')

@app.route('/Bot_Code.html')
def Bot_Code():
	return render_template('Bot_Code.html')

@app.route('/Compare.html')
def compare():
	return render_template('Compare.html')

@app.route('/Tweepy_Problems.html')
def problems():
	return render_template('Problems.html')
