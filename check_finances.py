import re
import config #import the config file data
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser

# def main():
# Browse to Rap Genius
browser = RoboBrowser(history=True)
browser = RoboBrowser(parser="html.parser")  # will get a warning if parser not declared

# open chase login website
browser.open('https://secure07b.chase.com/web/auth/dashboard#/dashboard/overviewAccounts/overview/index')

# Search for Queen
form = browser.get_form()
form['userId'].value = config.CHASE_UN
form['password-text-input-field'].value = config.CHASE_PW
browser.submit_form(form)

src = str(browser.parsed())

start = '<span class="mc-value H1L current-balance-value" id="accountAvailableBalanceLinkPrimaryValue-183580333">'
end = '</span>'
result = re.search('%s(.*)%s' % (start, end), src).group(1)

print(result)


# main()