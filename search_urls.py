import webbrowser
import sys
import urllib.parse

# Set search queries here (updated based on your comments for variety)
search_paths = [
    "https://calendar.notion.so/",  # e.g., for                                                                         caldendar search
    "https://docs.google.com/spreadsheets/d/1wVF3QQQiLs9FIcz0-syEifKBBwgzdSFMBspuHwURZoo/edit?gid=0#gid=0", # e.g., for spreadsheet search
    "https://github.com/hvdyinv4688hbv/run-application/tree/main",  # e.g., for                                         run application repository search
]

def search_on_duckduckgo(query):
    #search bar search
    # Properly URL-encode the query
    #encoded_query = urllib.parse.quote(query)
    #url = f"https://duckduckgo.com/?q={encoded_query}"
    
    #address bar search
    url = query  # Assuming the query is a full URL or file path

    # Try to use Firefox, falling back to default browser
    try:
        firefox = webbrowser.get('firefox')
    except webbrowser.Error:
        print("Firefox not found. Falling back to default browser.")
        webbrowser.open(url, new=1)
    else:
        firefox.open(url, new=1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Use command-line arguments as a single query
        query = ' '.join(sys.argv[1:])
        search_on_duckduckgo(query)
    else:
        # No args: Loop through each search path/query
        for query in search_paths:
            search_on_duckduckgo(query)