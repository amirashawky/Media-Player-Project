import sqlite3
import pygame
from time import sleep
from tkinter import *
from tkinter import ttk

all_playlists = []
all_artists = []
all_bands = []
all_songs = []
all_albums=[]

########################################################################

class album:

    def _init_(self):
        self.title = ''
        self.band_name = ''
        self.number_songs = 0
        self.list_songs = []
        self.list_artist=[]

    def load_album_songs(self):
        conn = sqlite3.connect('musicly.sqlite')
        cursor = conn.cursor()
        cursor=conn.execute("SELECT * from songs where album_name="+"'"+self.title + "'")
        self.list_songs=[]
        for row in cursor:
            s=song()
            s.album_name = row[0]
            s.band_name = row[1]
            s.feature_artist = row[2]
            s.genres = row[3]
            s.length = row[4]
            s.lyrics = row[5]
            s.path = row[6]
            s.playlist_name = row[7]
            s.relase_date=row[8]
            s.name=row[9]
            s.artist_name = row[10]
            self.list_songs.append(s)
        cursor.close()
        conn.close()
        self.number_songs=len(self.list_songs)


    def show_album_songs(self):
        self.load_album_songs()
        for s in self.list_songs:
            print(s.name )

    def play_album_songs(self):
        self.load_album_songs()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)
        for song in self.list_songs:
            pygame.mixer.music.load(song.path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                sleep(1)
            pygame.mixer.music.stop()

###########################################################################
class playLists:
    def __init__(self):
        self.name=''
        self.list_songs=[]
        self.discription=''
        self.tracks=0

    def load_playList_discription(self):
        conn = sqlite3.connect('musicly.sqlite')
        cursor = conn.cursor()
        cursor = conn.execute("SELECT playList_discription from playlists where playList_name="+"'"+self.name+"'")
        for row in cursor:
            self.discription = row[0]
        conn.close()

    def load_playlist_songs(self):
        conn=sqlite3.connect('musicly.sqlite')
        cursor=conn.cursor()
        cursor=conn.execute("SELECT * from songs where playList_name ="+"'"+self.name + "'")
        self.list_songs=[]
        for row in cursor:
            s=song()
            s.album_name = row[0]
            s.band_name = row[1]
            s.feature_artist = row[2]
            s.genres = row[3]
            s.length = row[4]
            s.lyrics = row[5]
            s.path = row[6]
            s.playlist_name = self.name
            s.relase_date=row[8]
            s.name=row[9]
            s.artist_name=row[10]
            self.list_songs.append(s)
        conn.close()
        self.tracks=len(self.list_songs)

    def show_sonngs(self):
        self.load_songs()
        for s in self.list_songs:
            print("Song name is ", s.name)

    def play_playlist_songs(self):
        self.load_playlist_songs()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)
        for song in self.list_songs:
            pygame.mixer.music.load(song.path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                sleep(1)

###########################################################################
class band:
    def __init__(self):
        self.band_name=''
        self.number_artists=0
        self.artists=[]
        self.band_songs=[]

    def load_band_songs(self):
        conn = sqlite3.connect('musicly.sqlite')
        cursor = conn.cursor()
        cursor = conn.execute("SELECT * from songs where bandname =" + "'" + self.band_name + "'")
        self.band_songs=[]
        for row in cursor:
            s = song()
            s.album_name = row[0]
            s.band_name = row[1]
            s.feature_artist = row[2]
            s.genres = row[3]
            s.length = row[4]
            s.lyrics = row[5]
            s.path = row[6]
            s.playlist_name = row[7]
            s.relase_date = row[8]
            s.name = row[9]
            s.artist_name = row[10]
            self.band_songs.append(s)
        conn.close()

    def show_band_songs(self):
        self.load_band_songs()
        for s in self.band_songs:
            print(s.name, " ", s.length)

    def play_band_songs(self):
        self.load_band_songs()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)
        for song in self.band_songs:
            pygame.mixer.music.load(song.path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                sleep(1)

###############################################################################

class artist:

    def __init__(self):
        self.name = ''
        self.band_name=''
        self.date_of_birth = ''
        self.list_songs=[]

    def load_artist_songs(self):
        conn = sqlite3.connect('musicly.sqlite')
        cursor = conn.cursor()
        cursor = conn.execute("SELECT * from songs where artist_name =" + "'" + self.name + "'or bandname='"+self.band_name+"'")
        #"'"+"or bandname="+"'"+self.band_name+
        self.list_songs=[]
        for row in cursor:
            s = song()
            s.album_name = row[0]
            s.band_name = row[1]
            s.feature_artist = row[2]
            s.genres = row[3]
            s.length = row[4]
            s.lyrics = row[5]
            s.path = row[6]
            s.playlist_name = row[7]
            s.relase_date = row[8]
            s.name = row[9]
            s.artist_name = row[10]
            self.list_songs.append(s)
        conn.close()
        print("name ",self.name)
        print(len(self.list_songs))

    def show_artist_songs(self):
        self.load_artist_songs()
        for s in self.list_songs:
            print(s.name)

    def play_artist_songs(self):
        self.load_artist_songs()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)
        for song in self.list_songs:
            pygame.mixer.music.load(song.path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                sleep(1)


##########################################################################

class song:

    def __init__(self):
        self.name = ''
        self.band_name = ''
        self.artist_name=''
        self.album_name = ''
        self.relase_date = ''
        self.genres = ''
        self.lyrics = ''
        self.length = ''
        self.path = ''
        self.playlist_name = ''
        self.feature_artist = ''

    def add_song_to_db(self):
        conn = sqlite3.connect('musicly.sqlite')
        conn.execute("INSERT INTO songs(album_name,bandname,featured_artist,genres,length,lyric,path,playList_name,release_date,song_name,artist_name) VALUES("+"'"+self.album_name+"','"+self.band_name +"','"+self.feature_artist+"','"+self.genres+"','"+self.length+"','"+self.lyrics+"','"+self.path+"','"+self.playlist_name+"','"+self.relase_date+"','"+self.name+"','"+self.artist_name+"');");
        cursor = conn.execute("SELECT * from artists where artist_name="+"'"+self.artist_name+"'")
        count = 0
        for row in cursor:
            count += 1
        if count==0:
            conn.execute("INSERT INTO artists(artist_name) VALUES('"+self.artist_name+"')")
        if self.band_name !='':
            cursor = conn.execute("SELECT * from bands where band_name=" + "'" + self.band_name + "'")
            count=0
            for row in cursor:
                count += 1
            if count ==0:
                conn.execute("INSERT INTO bands(band_name,number_artists) VALUES('" + self.band_name + "',0)")
        cursor = conn.execute("SELECT * from albums where title=" + "'" + self.album_name + "'")
        count = 0
        for row in cursor:
            count += 1
        if count ==0:
            conn.execute("INSERT INTO albums(band_name,number_songs,title) VALUES('"+self.band_name+"',1,'"+self.album_name+"')")
        conn.commit()
        conn.close()

    def delete_song_db(self):
        conn = sqlite3.connect('musicly.sqlite')
        conn.execute("DELETE from songs where song_name = "+"'"+self.name+"'")
        conn.commit()
        conn.close()

########################################################################## Musicly

def load_all_playLists():
    all_l=[]
    conn = sqlite3.connect('musicly.sqlite')
    cursor = conn.cursor()
    cursor = conn.execute("SELECT playList_name , tracks  from playlists ")
    for row in cursor:
        if row[0]!="":
            l= playLists()
            l.name = row[0]
            l.tracks=row[1]
            l.load_playlist_songs()
            all_l.append(l)
    conn.close()
    return all_l ;

def load_all_bands():
    bs=[]
    conn = sqlite3.connect('musicly.sqlite')
    cursor = conn.cursor()
    cursor = conn.execute("SELECT band_name from bands ")
    for row in cursor:
        if row[0]!="":
            b = band()
            b.band_name = row[0]
            bs.append(b)
    conn.close()
    return bs;

def load_library():
    all_s=[]
    conn = sqlite3.connect('musicly.sqlite')
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * from songs ")
    for row in cursor:
        s = song()
        s.album_name = row[0]
        s.band_name = row[1]
        s.feature_artist = row[2]
        s.genres = row[3]
        s.length = row[4]
        s.lyrics = row[5]
        s.path = row[6]
        s.playlist_name = row[7]
        s.relase_date = row[8]
        s.name = row[9]
        all_s.append(s)
    conn.close()
    return all_s ;

def load_all_artists():
    all_a = []
    conn = sqlite3.connect('musicly.sqlite')
    cursor = conn.cursor()
    cursor = conn.execute("SELECT artist_name from artists ")
    for row in cursor:
        if row[0]!="":
            a = artist()
            a.name=row[0]
            all_a.append(a)
    conn.close()
    return all_a;

def load_all_albums():
    all_a=[]
    conn = sqlite3.connect('musicly.sqlite')
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * from albums ")
    for row in cursor:
        a = album()
        a.band_name=row[0]
        a.number_songs=row[1]
        a.title=row[2]
        a.load_album_songs()
        all_a.append(a)
    conn.close()
    return all_a
###########################################################################   MAke all your test here
def New_playList_gui():
    form =Tk()
    form.title("Play List Information ")
    form.geometry('350x350')
    fram = Frame(form)
    name_label = Label(fram, text="Enter playList Name ")
    name_entry = Entry(fram)
    description_label = Label(fram , text="Enter PlayList Discription ")
    des_entery = Entry(fram)
    add_button = Button(fram, text=" Add ", command=lambda: add_playlist(name_entry.get(), des_entery.get(), form))
    fram.pack()
    name_label.grid(row=0)
    name_entry.grid(row=0, column=1)
    description_label.grid(row=2, column=0)
    des_entery.grid(row=2, column=1)
    add_button.grid(row=3, column=7)
    form.mainloop()


def add_playlist(n_e, des_e, page):
    p = playLists()
    p.name = n_e
    p.discription = des_e
    all_playlists.append(p)
    conn = sqlite3.connect('musicly.sqlite')
    #conn.execute("INSERT INTO playlists (playList_name,playList_discription , tracks )  VALUES ('funnyplayList','this discription' , 0 )")
    conn.execute("INSERT INTO playlists (playList_name,playList_discription , tracks )  VALUES ('" +p.name+"','"+p.discription+"',0)" )
    conn.commit()
    conn.close()
    page.destroy()

def view_playlists_gui():
    display_page = Tk()
    display_page.title(" Display PlayLists ")
    display_page.geometry('500x500+500+500')
    count = 0
    for p in all_playlists:
        count += 1
        p_number = Label(display_page, text=str(count) + ".")
        playlistlable = Label(display_page, text=p.name+"       "+str(p.tracks)  )
        #playlistlable.bind("<Button-1>", lambda event : view_choosing_playlist(event,display_page,count ))
        p_number.grid(row=count , column=0)
        playlistlable.grid(row=count, column=1)

    p_choosen = Entry(display_page)
    count += 1
    p_choosen.grid(row=count , column=0)

    b_play = Button(display_page, text=" Play "  , command=lambda:play_playlist(p_choosen.get() , display_page) , height = 1, width = 13 )
    b_play.grid(row=count , column=1  )

    b_delete = Button(display_page, text=" Delete " ,command=lambda:delete_playlist(p_choosen.get() ,display_page), height = 1, width = 8)
    b_delete.grid(row=count, column=2)

    b_view = Button(display_page, text="discription and songs" , command=lambda:view_playlist_dis(p_choosen.get(),display_page))
    b_view.grid(row=count, column=3)

    b_add_song = Button(display_page, text=" Add Song " , command=lambda :add_song_playlist(p_choosen.get()))
    b_add_song.grid(row=count, column=4)
    display_page.mainloop()


def play_playlist(p_number , page ):
    number = int(p_number)
    number = number-1
    if number in range(len(all_playlists)):
        all_playlists[number].play_playlist_songs()
    #len(all_playlists[number].)
    #print("play")


def view_playlist_dis(p_num,page):
    page.destroy()
    number=int(p_num)
    number=number-1
    newpage=Tk()
    newpage.title(" PlayList Information ")
    newpage.geometry('500x500+500+500')
    all_playlists[number].load_playList_discription()
    dis_lable=Label(newpage,text=all_playlists[number].discription)
    dis_lable.grid(row=0, column=0)
    all_playlists[number].load_playlist_songs()
    count=1
    for s in all_playlists[number].list_songs :
        s_lable=Label(newpage , text=s.name + "  Duration : "+str(s.length))
        s_lable.grid(row=count , column=0)
        count += 1

    back_button = Button(newpage , text=" Back ", command= lambda :  go_to_view_p(newpage))
    back_button.grid(row=count , column=0 )

    newpage.mainloop()

def go_to_view_p(page):
    page.destroy()
    view_playlists_gui()

def delete_playlist(p_num , page):
    num=int(p_num)
    num -= 1
    if num in range(len(all_playlists)):
        page.destroy()
        conn = sqlite3.connect('musicly.sqlite')
        conn.execute("DELETE from playlists where playList_name = " + "'" + all_playlists[num].name + "'")
        conn.commit()
        conn.close()
        del all_playlists[num]
        view_playlists_gui()

def add_song_playlist(p_number):
    number = int(p_number)
    number = number - 1
    page = Tk()
    page.geometry('350x350')

    n_lable=Label(page,text='Song Name')
    n_lable.grid(row=0,column=0)
    n_entry=Entry(page)
    n_entry.grid(row=0,column=1)

    band_lable=Label(page,text='Band Name')
    band_lable.grid(row=1,column=0)
    band_entry=Entry(page)
    band_entry.grid(row=1,column=1)

    artist_lable = Label(page, text='Artist Name')
    artist_lable.grid(row=2, column=0)
    artist_entry = Entry(page)
    artist_entry.grid(row=2, column=1)

    album_lable=Label(page,text='Album Name')
    album_lable.grid(row=3,column=0)
    album_entry = Entry(page)
    album_entry.grid(row=3, column=1)

    rele_date_lable = Label(page, text='Release Date')
    rele_date_lable.grid(row=4, column=0)
    date_entry = Entry(page)
    date_entry.grid(row=4, column=1)

    genres_lable=Label(page, text=' Genres ')
    genres_lable.grid(row=5, column=0)
    genres_entry=Entry(page)
    genres_entry.grid(row=5, column=1)

    lyrics_lable=Label(page, text=' Lyrice ')
    lyrics_lable.grid(row=6, column=0)
    lyrics_entry=Entry(page)
    lyrics_entry.grid(row=6, column=1)

    length_lable=Label(page, text=' Length ')
    length_lable.grid(row=7, column=0)
    length_entry=Entry(page)
    length_entry.grid(row=7, column=1)
    add_button=Button(page,text="Add Song ", command=lambda :add_song(number , n_entry.get(),band_entry.get(),length_entry.get(),date_entry.get(),lyrics_entry.get(),genres_entry.get(),album_entry.get(),page))
    add_button.grid(row=8,column=2)
    page.mainloop()

def add_song(playlist_number,song_name ,band_name,length,re_date,lyrice,genres,album_name ,page):
    s = song()
    s.playlist_name = all_playlists[playlist_number].name
    s.name = song_name
    s.band_name = band_name
    s.length = length
    s.relase_date = re_date
    s.lyrics = lyrice
    s.genres = genres
    s.feature_artist = ''
    s.album_name = album_name
    s.path =s.name + ".mp3"
    all_playlists[playlist_number].list_songs.append(s)
    page.destroy()
    s.add_song_to_db()

####################################################################
def New_album_gui():
    album_form=Tk()
    album_form.geometry('250x250+500+300')
    title_label=Label(album_form,text='Title')
    title_e=Entry(album_form)
    char_label=Label(album_form,text='Artist/Band')
    c_entry=Entry(album_form)
    title_label.grid(row=0,column=0)
    title_e.grid(row=0,column=1)
    char_label.grid(row=1,column=0)
    c_entry.grid(row=1,column=1)
    add_but=Button(album_form , text="Add",command=lambda :add_album(title_e.get(),c_entry.get(),album_form))
    add_but.grid(row=2,column=2)
    album_form.mainloop()

def add_album(title,character,page):
    page.destroy()
    a=album()
    a.number_songs=0
    a.title=title
    a.band_name=character
    all_albums.append(a)
    conn = sqlite3.connect('musicly.sqlite')
    conn.execute("INSERT INTO albums (band_name,number_songs,title)VALUES ("+"'"+character+"',"+"0"+",'"+title+"')");
    conn.commit()
    conn.close()

def view_albums_gui():
    all_albums=load_all_albums()
    display_page = Tk()
    display_page.title(" Display Albums ")
    display_page.geometry('500x500+500+500')
    count = 0
    for a in all_albums:
        count += 1
        p_number = Label(display_page, text=str(count) + ".")
        playlistlable = Label(display_page, text=a.title + "       " + str(a.number_songs))
        # playlistlable.bind("<Button-1>", lambda event : view_choosing_playlist(event,display_page,count ))
        p_number.grid(row=count, column=0)
        playlistlable.grid(row=count, column=1)

    a_choosen = Entry(display_page)
    count += 1
    a_choosen.grid(row=count, column=0)

    b_play = Button(display_page, text=" Play ", command=lambda :play_chosen_album(a_choosen.get()),  height=1,width=13)
    b_play.grid(row=count, column=1)

    b_delete = Button(display_page, text=" Delete ",command=lambda :delete_album(a_choosen.get(),display_page), height=1, width=8)
    b_delete.grid(row=count, column=2)

    display_page.mainloop()

def play_chosen_album(a_number):
    number=int(a_number)
    number=number-1
    if number in range(len(all_playlists)) :
        all_albums[number].play_album_songs()

def delete_album(a_number , page):
    num=int(a_number)
    num -= 1
    if num in range(len(all_albums)):
        page.destroy()
        conn = sqlite3.connect('musicly.sqlite')
        conn.execute("DELETE from albums where title = " + "'" + all_albums[num].title + "'")
        conn.execute("DELETE from songs where album_name = "+"'"+all_albums[num].title+"'")
        conn.commit()
        conn.close()
        del all_albums[num]
        view_albums_gui()

#################################################################################################
def new_artist_gui():
    artist_form = Tk()
    artist_form.geometry('250x250+500+300')
    name_label = Label(artist_form, text='Artist Name')
    name_e = Entry(artist_form)
    band_name = Label(artist_form, text='Band Name')
    b_entry = Entry(artist_form)
    bd_lable=Label(artist_form,text="Date Of Birth")
    bd_entry=Entry(artist_form)

    name_label.grid(row=0, column=0)
    name_e.grid(row=0, column=1)
    band_name.grid(row=1, column=0)
    b_entry.grid(row=1, column=1)
    bd_lable.grid(row=2, column=0)
    bd_entry.grid(row=2, column=1)

    add_but = Button(artist_form, text="Add", command=lambda: add_artist(name_e.get(),b_entry.get(),bd_entry.get(),artist_form))
    add_but.grid(row=2, column=2)
    artist_form.mainloop()

def add_artist(name,band_name,date_birth,page):
    page.destroy()
    art=artist()
    art.name=name
    art.band_name=band_name
    art.date_of_birth=date_birth
    conn = sqlite3.connect('musicly.sqlite')
    conn.execute("INSERT INTO artists (artist_name,band_name,date_of_birth)VALUES (" + "'" + name + "','" +band_name + "','" + date_birth + "')");
    conn.commit()
    conn.close()
    all_artists.append(art)

def view_artists_gui():
    display_page = Tk()
    all_artists=load_all_artists()
    display_page.title(" Display Artists ")
    display_page.geometry('500x500+500+500')
    count = 0
    for a in all_artists:
        count += 1
        a_number = Label(display_page, text=str(count) + ".")
        artist_lable = Label(display_page, text=a.name )
        # playlistlable.bind("<Button-1>", lambda event : view_choosing_playlist(event,display_page,count ))
        a_number.grid(row=count, column=0)
        artist_lable.grid(row=count, column=1)

    a_choosen = Entry(display_page)
    count += 1
    a_choosen.grid(row=count, column=0)

    b_play = Button(display_page, text=" Play ",  height=1, width=13 , command=lambda :play_artist_songs(a_choosen.get()))
    b_play.grid(row=count, column=1)

    b_delete = Button(display_page, text=" Delete ",height=1, width=8 , command=lambda :delete_artist(a_choosen.get(),display_page))
    b_delete.grid(row=count, column=2)

    display_page.mainloop()

def play_artist_songs(a_choosen):
    num=int(a_choosen)
    num -=1
    if num in range(len(all_artists)):
        all_artists[num].play_artist_songs()

def delete_artist(a_choosen,page):
    num = int(a_choosen)
    num -= 1
    if num in range(len(all_artists)):
        page.destroy()
        conn = sqlite3.connect('musicly.sqlite')
        conn.execute("DELETE from artists where artist_name = " + "'" + all_artists[num].name + "'")
        #conn.execute("DELETE from songs where artist_name = " + "'" + all_artists[num].name + "'")
        conn.commit()
        conn.close()
        del all_artists[num]
        view_artists_gui()

#################################################################################################


def view_bands():
    display_page = Tk()
    all_bands=load_all_bands()
    display_page.title(" Display Bands ")
    display_page.geometry('500x500+500+500')
    count = 0
    for b in all_bands:
        count += 1
        b_number = Label(display_page, text=str(count) + ".")
        band_lable = Label(display_page, text=b.band_name )
        # playlistlable.bind("<Button-1>", lambda event : view_choosing_playlist(event,display_page,count ))
        b_number.grid(row=count, column=0)
        band_lable.grid(row=count, column=1)

    b_choosen = Entry(display_page)
    count += 1
    b_choosen.grid(row=count, column=0)

    b_play = Button(display_page, text=" Play ", command=lambda: play_chosen_band(b_choosen.get()), height=1, width=13)
    b_play.grid(row=count, column=1)

def play_chosen_band(band_number):
    number=int(band_number)
    number -= 1
    if number in range(len(all_bands)):
        all_bands[number].play_band_songs()
#################################################################################################
def new_song_gui():
    page = Tk()
    page.geometry('350x350')

    n_lable = Label(page, text='Song Name')
    n_lable.grid(row=0, column=0)
    n_entry = Entry(page)
    n_entry.grid(row=0, column=1)

    band_lable = Label(page, text='Band Name')
    band_lable.grid(row=1, column=0)
    band_entry = Entry(page)
    band_entry.grid(row=1, column=1)

    artist_lable = Label(page, text='Artist Name')
    artist_lable.grid(row=2, column=0)
    artist_entry = Entry(page)
    artist_entry.grid(row=2, column=1)

    album_lable = Label(page, text='Album Name')
    album_lable.grid(row=3, column=0)
    album_entry = Entry(page)
    album_entry.grid(row=3, column=1)

    rele_date_lable = Label(page, text='Release Date')
    rele_date_lable.grid(row=4, column=0)
    date_entry = Entry(page)
    date_entry.grid(row=4, column=1)

    genres_lable = Label(page, text=' Genres ')
    genres_lable.grid(row=5, column=0)
    genres_entry = Entry(page)
    genres_entry.grid(row=5, column=1)

    lyrics_lable = Label(page, text=' Lyrice ')
    lyrics_lable.grid(row=6, column=0)
    lyrics_entry = Entry(page)
    lyrics_entry.grid(row=6, column=1)

    length_lable = Label(page, text=' Length ')
    length_lable.grid(row=7, column=0)
    length_entry = Entry(page)
    length_entry.grid(row=7, column=1)
    add_button = Button(page, text="Add Song " , command=lambda :add(n_entry.get(),band_entry.get(),artist_entry.get(),length_entry.get(),date_entry.get(),lyrics_entry.get(),genres_entry.get(),album_entry.get(),page))
    add_button.grid(row=8, column=2)
    page.mainloop()
    print('song will be added ')
def add(song_name, band_name,artist_name ,length ,re_date ,lyrice ,genres ,album_name,page):
    #print('hi from ading song')
    s=song()
    s.name=song_name
    s.band_name=band_name
    s.artist_name=artist_name
    s.length=length
    s.relase_date=re_date
    s.lyrics=lyrice
    s.genres=genres
    s.feature_artist = ""
    s.album_name=album_name
    s.path=s.name+".mp3"
    s.playlist_name = ""
    s.add_song_to_db()
    all_songs.append(s)
    page.destroy()

def view_song_gui():
    display_page=Tk()
    display_page.geometry('350x350')
    count = 0
    for s in all_songs:
        count += 1
        count_label = Label(display_page , text=str(count)+" .")
        song_label=Label(display_page,text=s.name)
        count_label.grid(row=count , column =0)
        song_label.grid(row=count , column=1)
    choosen=Entry(display_page)
    count += 1
    choosen.grid(row=count,column=0)
    view_button=Button(display_page,text='View',command=lambda :view_s(choosen.get())).grid(row=count , column=1)
    del_button = Button(display_page, text='Delete', command=lambda: delete_song_from_lib(choosen.get())).grid(row=count, column=2)
    display_page.mainloop()


def view_s(choosen_s):
    num = int(choosen_s)
    num = num-1
    if num in range(len(all_songs)):
        dis_page = Tk()
        dis_page.geometry('350x350')
        l_name=Label(dis_page,text='Name: ').grid(row=0,column=0)
        ll_name=Label(dis_page,text=all_songs[num].name).grid(row=0,column=1)

        l_redate=Label(dis_page,text='Release Date: ').grid(row=1,column=0)
        ll_redate=Label(dis_page,text=all_songs[num].relase_date).grid(row=1,column=1)

        l_lyric = Label(dis_page, text='Lyrics: ').grid(row=2, column=0)
        ll_lyric = Label(dis_page, text=all_songs[num].lyrics).grid(row=2, column=1)

        l_albun_name = Label(dis_page, text='Album Name: ').grid(row=3, column=0)
        ll_lyric = Label(dis_page, text=all_songs[num].album_name).grid(row=3, column=1)

        l_length = Label(dis_page, text='Length: ').grid(row=4, column=0)
        ll_length = Label(dis_page, text=all_songs[num].length).grid(row=4, column=1)

        quit_b=Button(dis_page,text='Ok',command=lambda :dist(dis_page)).grid(row=6,column=0)
        dis_page.mainloop()


def dist(page):
    page.destroy()


def delete_song_from_lib(s_choosen):
    num = int(s_choosen)
    num -= 1
    if num in range(len(all_songs)):
        all_songs[num].delete_song_db()
        del all_songs[num]

################################################################################################

def start_page():

    myGui = Tk()
    myGui.title(" Musicly ")
    myGui.geometry('450x450+500+300')

    menu = Menu(myGui)

    playList_menu = Menu(menu, tearoff=0)
    playList_menu.add_command(label="New", command=New_playList_gui)
    playList_menu.add_command(label="View PlayLists", command= view_playlists_gui)
    menu.add_cascade(label="PlayLists", menu=playList_menu)

    artist_menu = Menu(menu, tearoff=0)
    artist_menu.add_command(label="New",command=new_artist_gui)
    artist_menu.add_command(label="View Artists" , command=view_artists_gui)
    menu.add_cascade(label="Artists", menu=artist_menu)

    band_menu = Menu(menu, tearoff=0)
    band_menu.add_command(label="View Bands" , command=view_bands)
    menu.add_cascade(label="Bands", menu=band_menu)

    albums_menu = Menu(menu, tearoff=0)
    albums_menu.add_command(label="New" , command=New_album_gui)
    albums_menu.add_command(label="View Albums" , command=view_albums_gui)
    menu.add_cascade(label="Albums", menu=albums_menu)

    library_menu = Menu(menu, tearoff=0)
    library_menu.add_command(label="New Song",command=new_song_gui)
    library_menu.add_command(label="View Song",command=view_song_gui)

    menu.add_cascade(label="Library", menu=library_menu )

    myGui.config(menu=menu)

    myGui.mainloop()
################################################################################################
all_playlists=load_all_playLists()
all_albums=load_all_albums()
all_artists=load_all_artists()
all_songs=load_library()
all_bands=load_all_bands()

#conn = sqlite3.connect('musicly.sqlite')
#conn.execute("delete from songs where song_name='Come Back To Me'")
start_page()