import re
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser

def main():
    # Browse to Rap Genius
    browser = RoboBrowser(history=True)
    browser = RoboBrowser(parser="html.parser")  # will get a warning if parser not declared
    browser.open('http://rapgenius.com/')

    # Search for Queen
    form = browser.get_form(action='/search')
    form                # <RoboForm q=>
    form['q'].value = 'queen'
    browser.submit_form(form)

    # Look up the first song
    songs = browser.select('.song_name')
    try:
        browser.follow_link(songs[0])
    except IndexError:
        print ("Songs Index doesn't exist!")
        return
    lyrics = browser.select('.lyrics')
    try:
        lyrics[0].text      # \n[Intro]\nIs this the real life...
    except IndexError:
        print ("Lyrics Index doesn't exist!")

    # Back to results page
    browser.back()

    # Look up my favorite song
    browser.follow_link('death on two legs')

    # Can also search HTML using regex patterns
    lyrics = browser.find(class_=re.compile(r'\blyrics\b'))
    print(lyrics.text)         # \n[Verse 1]\nYou suck my blood like a leech...

main()