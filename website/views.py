from flask import Blueprint, render_template, request
from .models import *

import sqlite3 # pip install sqlite3

views = Blueprint('views', __name__)

# lists needed for combo boxes on bowling_corner page
month_from_list = []
date_from_list = []
year_from_list = []
month_to_list = []
date_to_list = []
year_to_list = []
venue_list = []
event_from_list = []
event_to_list = []

###############################################################################

@views.route('/about')
def about(): # the about page
	return render_template('about.html')

###############################################################################

@views.route('/bowling', methods=['GET', 'POST'])
def bowling_corner(): # the bowling_corner page
	# populate the lists for the combo boxes if they are empty
	if venue_list == []:
		create_month_lists()
		create_date_lists()
		create_year_lists()
		create_venue_list()
		create_event_lists()

# 3/23/1991 - 12/30/2004 by default for the date range
	selected_month_from = 2
	selected_date_from = 22
	selected_year_from = 0
	selected_month_to = 11
	selected_date_to = 29
	selected_year_to = 13
	selected_venue = 0
# default selected events are the first and last events	
	selected_event_from = 0
	selected_event_to = 1554

	stats_results = None # object that stores all the statistics results of a given search

	if request.method == 'POST': # executes this block of code if either button for getting statistics is clicked.
		data = request.form
		
		if data.get("get-stats") == "": # if get stats based on date range or venue is clicked
			month_from = int(data.get("cmb-month-from")) + 1
			date_from = int(data.get("cmb-date-from")) + 1
			year_from = int(data.get("cmb-year-from")) + 1991
			month_to = int(data.get("cmb-month-to")) + 1
			date_to = int(data.get("cmb-date-to")) + 1
			year_to = int(data.get("cmb-year-to")) + 1991
			venue = int(data.get("cmb-venues"))

			stats_results = get_statistics(month_from, date_from, year_from, month_to, date_to, year_to, venue, 1, 1555, 1)

		if data.get("get-stats2") == "": # if get stats based on range of events is clicked
			event_from = int(data.get("cmb-event-from")) + 1
			event_to = int(data.get("cmb-event-to")) + 1

			stats_results = get_statistics(3, 23, 1991, 12, 30, 2004, 0, event_from, event_to, 2)

	return render_template("bowling.html", dfl=date_from_list, mfl=month_from_list, yfl=year_from_list, dtl=date_to_list, efl=event_from_list, etl=event_to_list, mtl=month_to_list, ytl=year_to_list, vl=venue_list, smf=selected_month_from, sdf=selected_date_from, syf=selected_year_from, smt=selected_month_to, sdt=selected_date_to, sef=selected_event_from, set=selected_event_to, syt=selected_year_to, sv=selected_venue, results=stats_results )

###############################################################################

@views.route('/contact')
def contact(): # contact_page
	return render_template('contact.html')

# *****************************************************************************

def create_date_lists(): # creating the list of dates for the combo boxes on the bowling_corner page
	for x in range(1,32):
		date_from_list.append(date_id(x,x-1))
		date_to_list.append(date_id(x,x-1))

# *****************************************************************************

def create_event_lists(): # creating event list for events combo boxes (bowling_corner)
	conn = sqlite3.connect('website/static/databases/johns_world.db')
	cmd = conn.cursor()

	sql = "SELECT bowling_my_events.event_id, bowling_my_events.event_date, bowling_my_venues.name, bowling_my_event_names.name FROM bowling_my_events, bowling_my_venues, bowling_my_event_names WHERE bowling_my_events.venue_id = bowling_my_venues.venue_id AND bowling_my_events.event_name_id = bowling_my_event_names.event_name_id"
	cmd.execute(sql)
	for rec in cmd:
		id = int(rec[0])
		stardate = int(rec[1])
		venue = str(rec[2])
		event_name = str(rec[3])

		year = int(stardate / 10000)
		month = int((stardate % 10000) / 100)
		date = stardate % 100
		event_date = str(month) + "/" + str(date) + "/" + str(year)

		event_str = str(id) + ". " + event_date + " -- " + venue
		if len(event_name) > 0:
			event_str += " -- " + event_name
		if len(event_str) > 54:			
			temp_str = event_str[0:54]
			event_str = temp_str

		event_from_list.append(event_id(event_str, id-1))
		event_to_list.append(event_id(event_str, id-1))

# *****************************************************************************

def create_month_lists(): # creating the list of months for the months combo boxes (bowling_corner)
	for x in range(1,13):
		if x == 1:
			month_from_list.append(month_id("JANUARY", 0))
			month_to_list.append(month_id("JANUARY", 0))

		elif x == 2:
			month_from_list.append(month_id("FEBRUARY", 1))
			month_to_list.append(month_id("FEBRUARY", 1))

		elif x == 3:
			month_from_list.append(month_id("MARCH",2))
			month_to_list.append(month_id("MARCH",2))

		elif x == 4:
			month_from_list.append(month_id("APRIL",3))
			month_to_list.append(month_id("APRIL",3))

		elif x == 5:
			month_from_list.append(month_id("MAY" ,4))
			month_to_list.append(month_id("MAY" ,4))

		elif x == 6:
			month_from_list.append(month_id("JUNE" ,5))
			month_to_list.append(month_id("JUNE" ,5))

		elif x == 7:
			month_from_list.append(month_id("JULY" ,6))
			month_to_list.append(month_id("JULY" ,6))

		elif x == 8:
			month_from_list.append(month_id("AUGUST" ,7))
			month_to_list.append(month_id("AUGUST" ,7))

		elif x == 9:
			month_from_list.append(month_id("SEPTEMBER" ,8))
			month_to_list.append(month_id("SEPTEMBER" ,8))

		elif x == 10:
			month_from_list.append(month_id("OCTOBER" ,9))
			month_to_list.append(month_id("OCTOBER" ,9))

		elif x == 11:
			month_from_list.append(month_id("NOVEMBER" ,10))
			month_to_list.append(month_id("NOVEMBER" ,10))

		else:
			month_from_list.append(month_id("DECEMBER" ,11))
			month_to_list.append(month_id("DECEMBER" ,11))

###############################################################################

def create_series_list(): # creating list of series for the menu on the writings_corner page
	conn = sqlite3.connect('website/static/databases/johns_world.db')
	cmd = conn.cursor()

	conn2 = sqlite3.connect('website/static/databases/johns_world.db')
	cmd2 = conn2.cursor()

	series_list = []
	sql = "SELECT * FROM writings_series"
	cmd.execute(sql)
	for rec in cmd:
		id = int(rec[0])
		name = str(rec[1])

		sql2 = "SELECT * FROM writings_stories WHERE series_id = " + str(id)		
		cmd2.execute(sql2)
		stories = 0
		for rec2 in cmd2:
			stories += 1

		series_list.append(series_id(id, name, stories))

	return series_list

###############################################################################

def create_song_list(series_id, story_id): # creating song list for a given series and story (writings_corner page)
	conn = sqlite3.connect('website/static/databases/johns_world.db')
	cmd = conn.cursor()

	song_list = []
	series = ""
	story_title = ""
	date_started = 0
	date_finished = 0
	pages = 0
	summary = ""
	# split into 3 sql statements
	sql = "SELECT * FROM writings_series WHERE series_id = " + str(series_id)
	cmd.execute(sql)
	for rec in cmd:
		series = str(rec[1])

	sql = "SELECT * FROM writings_stories WHERE series_id = " + str(series_id) + " AND story_id = " + str(story_id)
	cmd.execute(sql)
	for rec in cmd:
		story_title = str(rec[2])
		ds = int(rec[3])
		df = int(rec[4])

		pages = int(rec[5])
		summary = str(rec[6])

	songs_in_story = 0
	sql = "SELECT music_songs.song_id, music_songs.title, music_songs.artist, music_songs.year FROM writings_songs_in_stories, music_songs WHERE writings_songs_in_stories.song_id = music_songs.song_id AND writings_songs_in_stories.series_id = "	+ str(series_id) + " AND writings_songs_in_stories.story_id = " + str(story_id)
	cmd.execute(sql)
	for rec in cmd:
		songs_in_story += 1
		song_id = int(rec[0])
		song_title = str(rec[1])
		artist = str(rec[2])
		year = int(rec[3])

		song_list.append(song_index(songs_in_story, song_id, song_title, artist, year))

	selected_story = sel_story(series, story_id, story_title, pages, summary, ds, df, song_list)
	return selected_story

###############################################################################

def create_story_list(series_id): # creating a list of stories for the given series, plus the series name
	conn = sqlite3.connect('website/static/databases/johns_world.db')
	cmd = conn.cursor()

	story_list = []
	series_name = ""
	sql = "SELECT writings_stories.story_id, writings_stories.title, writings_stories.pages, writings_series.name FROM writings_stories, writings_series WHERE writings_stories.series_id = writings_series.series_id AND writings_stories.series_id = " + str(series_id)
	cmd.execute(sql)
	for rec in cmd:
		id = int(rec[0])
		title = str(rec[1])
		pages = int(rec[2])
		series_name = str(rec[3])

		story_list.append(stories_id(id, title, pages))

	selected_series = sel_series(series_name, story_list)
	return selected_series

 # *****************************************************************************

def create_venue_list(): # creating a list of venues for the combo box (bowling_corner)
	conn = sqlite3.connect('website/static/databases/johns_world.db')
	cmd = conn.cursor()

	venue_list.append(venue_id("ALL VENUES", 0))

	sql = "SELECT * FROM bowling_my_venues"
	cmd.execute(sql)
	for rec in cmd:
		id = int(rec[0])
		venue = str(rec[1])

		venue_list.append(venue_id(venue, id))

# *****************************************************************************

def create_year_lists(): # creating year lists for combo boxes in bowling corner
	for x in range(1991,2005):
		year_from_list.append(year_id(x,x-1991))
		year_to_list.append(year_id(x,x-1991))

###############################################################################

def get_song_details(song_id): # getting the details of a given song for display on the writings corber page
	selected_song = None
	conn = sqlite3.connect('website/static/databases/johns_world.db')
	cmd = conn.cursor()
	sql = "SELECT * FROM music_songs WHERE song_id = " + str(song_id)
	cmd.execute(sql)
	for rec in cmd:
		title = str(rec[1])
		artist = str(rec[2])
		album = str(rec[3])
		if len(album) < 1:
			album = None
		year = int(rec[4])
		tm = int(rec[5])
		m = int(tm/60)
		s = tm % 60
		time = str(m) + ":"
		if s < 10:
			time += "0"
		time += str(s)
		p = int(rec[6])
		peak = "Did Not Chart"
		if p < 101:
			peak = "Peak: #" + str(p)
		if p == 200 or p == 201:
			peak = "Album Track"
		if p == 300 or p == 301:
			peak = "Flip Side"

		songwriter = str(rec[7])
		if len(songwriter) < 2:
			songwriter = None
		genre = str(rec[8])
		if len(genre) < 2:
			genre = None
		comments = str(rec[9])
		if len(comments) < 5:
			comments = None

		selected_song = song_detail(title, artist, album, year, time, peak, songwriter, genre, comments)
		
	return selected_song

###############################################################################

def get_statistics(mf, df, yf, mt, dt, yt, v, ef, et, t): # get the bowling statistics to be displayed on the bowling corner page
	conn = sqlite3.connect('website/static/databases/johns_world.db')
	cmd = conn.cursor()

	stardate1 = (yf*10000) + (mf*100) + df
	stardate2 = (yt*10000) + (mt*100) + dt

	games = 0
	total_pins = 0
	average = 0
	high_game = -1
	low_game = 301
	g300 = 0
	g200 = 0
	high_series3 = -1
	high_series4 = -1
	high_series5 = -1
	s600 = 0
	s700 = 0
	s800 = 0
	
	last_event = -1
	last_date = 0
	last_venue = ""
	last_event_name = ""
	game_list = []
	event_list = []
	high_game_info_list = []
	low_game_info_list = []
	hi_series3_info_list = []
	hi_series4_info_list = []
	hi_series5_info_list = []
	first_date = 0

	if t == 1: # date range:
		sql = "SELECT bowling_my_games.event_id, bowling_my_games.score, bowling_my_events.event_date, bowling_my_venues.name, bowling_my_event_names.name FROM bowling_my_games, bowling_my_events, bowling_my_venues, bowling_my_event_names WHERE bowling_my_games.event_id = bowling_my_events.event_id AND bowling_my_events.venue_id = bowling_my_venues.venue_id AND bowling_my_events.event_name_id = bowling_my_event_names.event_name_id AND bowling_my_events.event_date >= " + str(stardate1) + " AND bowling_my_events.event_date <= " + str(stardate2)
		if v > 0:
			sql += " AND bowling_my_events.venue_id = " + str(v)

	if t == 2: # event range:
		sql = "SELECT bowling_my_games.event_id, bowling_my_games.score, bowling_my_events.event_date, bowling_my_venues.name, bowling_my_event_names.name FROM bowling_my_games, bowling_my_events, bowling_my_venues, bowling_my_event_names WHERE bowling_my_games.event_id = bowling_my_events.event_id AND bowling_my_events.venue_id = bowling_my_venues.venue_id AND bowling_my_events.event_name_id = bowling_my_event_names.event_name_id AND bowling_my_games.event_id >= " + str(ef) + " AND bowling_my_games.event_id <= " + str(et)

	cmd.execute(sql)
	for rec in cmd:
		id = int(rec[0])
		score = int(rec[1])
		date = int(rec[2])
		venue = str(rec[3])
		event = str(rec[4])

		if first_date == 0:
			first_date = date

		if score > high_game:
			high_game = score
			high_game_list_info = []
			high_game_list_info.append(hi_lo_info(high_game, date, venue, event))
		elif score == high_game:
			high_game_list_info.append(hi_lo_info(high_game, date, venue, event))

		if score < low_game:
			low_game = score
			low_game_list_info = []
			low_game_list_info.append(hi_lo_info(low_game, date, venue, event))
		elif score == low_game:
			low_game_list_info.append(hi_lo_info(low_game, date, venue, event))

		if score == 300:
			g300 += 1
		if score >= 200 and score <= 299:
			g200 += 1

		games += 1
		total_pins += score

		if id != last_event:
			if last_event > -1:
				gms = 0
				tp = 0
				for g in game_list:
					gms += 1
					tp += g.score
				avg = tp / gms
				event_list.append(event_type(last_event, last_date, last_venue, last_event_name, gms, tp, avg, game_list))

			last_event = id
			last_date = date
			last_venue = venue
			last_event_name = event
			game_list = []
			game_list.append(game_type(1, score, ""))
			
		else:
			g = len(game_list) + 1
			series_str = ""
			if g > 2:
				series3 = score + game_list[g-2].score + game_list[g-3].score
				if series3 > high_series3:
					high_series3 = series3
					high_series3_list_info = []
					high_series3_list_info.append(hi_lo_info(high_series3, date, venue, event))
				elif series3 == high_series3:
					high_series3_list_info.append(hi_lo_info(high_series3, date, venue, event))
				if series3 > 599:
					series_str += "(" + str(series3) + ")"
				if series3 >= 600 and series3 <= 699:
					s600 += 1
				if series3 >= 700 and series3 <= 799:
					s700 += 1
				if series3 >= 800 and series3 <= 899:
					s800 += 1

			if g > 3:
				series4 = score + game_list[g-2].score + game_list[g-3].score + game_list[g-4].score
				if series4 > high_series4:
					high_series4 = series4
					high_series4_list_info = []
					high_series4_list_info.append(hi_lo_info(high_series4, date, venue, event))
				elif series4 == high_series4:
					high_series4_list_info.append(hi_lo_info(high_series4, date, venue, event))
				if series4 > 799:
					series_str += " [" + str(series4) + "]"
					# more to come

			if g > 4:
				series5 = score + game_list[g-2].score + game_list[g-3].score + game_list[g-4].score + game_list[g-5].score
				if series5 > high_series5:
					high_series5 = series5
					high_series5_list_info = []
					high_series5_list_info.append(hi_lo_info(high_series5, date, venue, event))
				elif series5 == high_series5:
					high_series5_list_info.append(hi_lo_info(high_series5, date, venue, event))
				if series5 > 999:
					series_str += " {" + str(series5) + "}"
					# more to come

			game_list.append(game_type(g, score, series_str))

	if games > 0:
		gms = 0
		tp = 0
		for g in game_list:
			gms += 1
			tp += g.score
		avg = tp / gms
		event_list.append(event_type(last_event, last_date, last_venue, last_event_name, gms, tp, avg, game_list))

		average = total_pins / games
		print(average)

		caption = ""
		if t == 1:
			caption = "Statistics For Events From " + str(mf) + "/" + str(df) + "/" + str(yf) + " To " + str(mt) + "/" + str(dt) + "/" + str(yt)
			if v > 0:
				caption += " At " + venue
		if t == 2:
			yf = int(first_date / 10000)
			mf = int((first_date % 10000) / 100)
			df = first_date % 100

			yt = int(last_date / 10000)
			mt = int((last_date % 10000) / 100)
			dt = last_date % 100
			caption = "Statistics For Events " + str(ef) + " to " + str(et) + " ("  + str(mf) + "/" + str(df) + "/" + str(yf) + " - " + str(mt) + "/" + str(dt) + "/" + str(yt) + ")"

		stats_results = result(caption, games, total_pins, average, high_game, high_game_list_info, low_game, low_game_list_info, high_series3, high_series3_list_info, high_series4, high_series4_list_info, high_series5, high_series5_list_info, g200, g300, s600, s700, s800, event_list)
		return stats_results

###############################################################################

@views.route('/happy-places') # the happy_places page
def happy_places():
	return render_template('happy_places.html')

###############################################################################

@views.route('/') # the home page
def home():
	return render_template('home.html')

###############################################################################

@views.route('/hundred-degree-days') # the hundred degree days page
def hundred_degree_days():
	return render_template('hundred_degree_days.html')

##############################################################################

@views.route('/writings') # the writings page
def writings():
	series_list = []
	selected_series = None
	selected_story = None
	selected_song = None

	series_id = 0
	story_id = 0
	song_id = 0

	sid = request.args.get("series_id")
	stid = request.args.get("story_id")
	soid = request.args.get("song_id")

	print(series_id, story_id, song_id)

	if sid == None:
		series_id = 0
	else:
		series_id = int(sid)

	if stid == None:
		story_id = 0
	else:
		story_id = int(stid)

	if soid == None:
		song_id = 0
	else:
		song_id = int(soid)

	print(series_id, story_id, song_id)

	if series_id == 0 and story_id == 0 and song_id == 0: # list the series
		series_list = create_series_list()

	if series_id > 0 and story_id == 0: # list the stories in the given series
		selected_series = create_story_list(series_id)

	if series_id > 0 and story_id > 0 and song_id == 0: # list all the songs in the given series and story
		selected_story = create_song_list(series_id, story_id)

	if song_id > 0: # list details about the song
		selected_song = get_song_details(song_id)

	return render_template('writings.html', list_series=series_list, series=series_id, series_selected=selected_series, story=story_id, story_selected=selected_story, song=selected_song)