import webbrowser
import sys
import urllib.parse

#making into program
#python -m  PyInstaller path/to/your/python/script.py
#python -m  PyInstaller C:\Users\sje8wy\Documents\search_urls.py

# Set search queries here (updated based on your comments for variety)
search_paths = [
    "https://calendar.notion.so/",  # e.g., for                                                                         caldendar search
    "https://docs.google.com/spreadsheets/d/1wVF3QQQiLs9FIcz0-syEifKBBwgzdSFMBspuHwURZoo/edit?gid=0#gid=0", # e.g., for spreadsheet search
    "https://github.com/hvdyinv4688hbv/run-application/tree/main",  # e.g., for                                         run application repository search
    "https://docs.google.com/document/d/1VUjSy-EMgEM2PfahK8ozA_utukx_hmK9OZ5lYE9sccw/edit?tab=t.0",  # e.g., for        progress document search
    "https://www.w3schools.com/html/html_table_sizes.asp",  # e.g., for                                                 w3 project search
    "https://docs.google.com/document/d/1FiOK_w35ZfjHamzDpfyn-yzkGpcyO-5gT62CRcAOivk/edit?tab=t.0",  # e.g., for        precedence document search
    "https://docs.google.com/document/d/1_llM4FxZ-EBzI1ByBB_5wcapXCl02diXZ6d31p64Id4/edit?tab=t.0",  # e.g., for        weekly ideas document search
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