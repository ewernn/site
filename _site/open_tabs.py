import webbrowser, time
# Example usage
comma_separated_list = "Neel Nanda, Ryan Greenblatt, Lisa Dunlap, Nate Thomas, Stephen\
Casper, Kayo Yin, Dan Hendrycks, Nora Belrose, Jacob Hilton, Charlie Snell and Lawrence Chan".split(", ")
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
for name in comma_separated_list:
    url = f"https://www.google.com/search?q={name}"
    webbrowser.get(chrome_path).open(url)
    # wait 1 second
    time.sleep(1)
