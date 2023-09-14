# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class date_id: # for the date combo boxes on the bowling_corner page
    def __init__(self, d, i):
        self.name = d
        self.id = i        

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class event_id: # for the event combo box on the bowling_corner page
    def __init__(self, e, i):
        self.name = e
        self.id = i        

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class event_type: # for the details about an event, relevant to the bowling_corner page
    def __init__(self, i, d, v, e, g, tp, a, gl):
        self.id = i
        year = int(d / 10000)
        month = int((d % 10000) / 100)
        date = d % 100
        self.date = str(month) + "/" + str(date) + "/" + str(year)        
        self.venue = v
        self.event_name = e
        self.games = g
        self.total_pins = tp
        self.average = format(a,'.2f')
        self.game_list = gl

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class game_type: # for the game detail of a bowling score (bowling_corner page)
    def __init__(self, n, s, ss):
        self.game_number = n # game number in a set
        self.score = s
        self.series_str = ss # if the game is part of a 3-game series of at least 600, a 4-game series of at least 800, or a 5-game series of at least 1000, this string will contain the info.

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class hi_lo_info: # info for a high game or a low game in a given query set (bowling_corner)
    def __init__(self, sc, d, v, e):
        self.score = sc
        year = int(d / 10000)
        month = int((d % 10000) / 100)
        date = d % 100
        self.date = str(month) + "/" + str(date) + "/" + str(year)
        self.venue = v
        if len(e) > 5:
            self.event = e
        
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class month_id: # for the month combo boxes (bowling_corner)
    def __init__(self, m, i):
        self.name = m
        self.id = i

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class result: # details of a query result for a range of dates or events (bowling corner)
    def __init__(self,c,g,tp,a,hg,hgi,lg,lgi,hs3,hsi3,hs4,hsi4,hs5,hsi5,g200,g300,s600,s700,s800,el):
        self.caption = c
        self.games = g
        self.total_pins = tp
        self.average = format(a,'.2f')
        self.high_game = hg
        self.high_game_info = hgi
        self.low_game = lg
        self.low_game_info = lgi
        self.high_series3 = hs3
        self.high_series3_info = hsi3
        self.high_series4 = hs4
        self.high_series4_info = hsi4
        self.high_series5 = hs5
        self.high_series5_info = hsi5
        self.games_200 = g200
        self.perfect_games = g300
        self.series_600 = s600
        self.series_700 = s700
        self.series_800 = s800
        self.event_list = el

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class sel_series: # name of series and the list of stories in the given series (writings_corner page)
    def __init__(self, s, sl):
        self.series = s
        self.story_list = sl

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class sel_story: # details of a selected story, and the list of songs featured in the story (writings_corner page)
    def __init__(self, s, stid, st, p, sum, ds, df, sl):
        self.series = s
        self.story_id = stid
        self.story = st # title
        self.pages = p
        if len(sum) < 5:
            sum = None
        self.summary = sum
        self.song_list = sl

        ys = int(ds / 10000)
        ms = int((ds % 10000) / 100)
        dds = ds % 100
        self.date_started = str(ms) + "/" + str(dds) + "/" + str(ys)
        
        yf = int(df / 10000)
        mf = int((df % 10000) / 100)
        ddf = df % 100
        self.date_finished = str(mf) + "/" + str(ddf) + "/" + str(yf)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class series_id: # contains info to be printed in the series list of the menu on the writings_corner page
    def __init__(self, i, s, st):
        self.name = s
        self.id = i
        self.stories = st

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class song_detail: # contains the details of a selected song, which is displayed on the writings_corner page
    def __init__(self, title, artist, album, year, time, peak, songwriter, genre, comments):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.time = time
        self.peak = peak
        self.songwriter = songwriter
        self.genre = genre
        self.comments = comments
        
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class song_index: # contains the information of a song that is in a list of songs featured in a given story (writings_corner)
    def __init__(self, i, id, t, a, y):
        self.index = i # order in story
        self.id = id
        self.title = t
        self.artist = a
        self.year = y

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class stories_id: # contains the info of a story that is displayed in a list of stories in a given series (writings_corner)
    def __init__(self, stid, t, p):
        self.story_id = stid
        self.title = t
        self.pages = p

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class venue_id: # for the venues combo box (bowling_corner)
    def __init__(self, v, i):
        self.name = v
        self.id = i

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class year_id: # for the year combo boxes (bowling_corner)
    def __init__(self, y, i):
        self.name = y
        self.id = i        