import requests
import json
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fact(_):
    """Fetch and display a random fact."""
    clear()
    try:
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = json.loads(response.text)
            fun_fact = data['text']
            
            # Use scope to manage output
            with use_scope('fun_fact_scope', clear=True):
                put_html(
                    '<p align="left">'
                    '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
                    '</p>'
                )
                put_text(fun_fact).style('color:blue; font-size:20px')
                put_buttons([dict(label='Click Me!', value='fetch', color='success')], onclick=get_fact)
        else:
            put_text("Failed to fetch a fact! Please try again later.").style('color:red; font-size:18px')
    except Exception as e:
        put_text(f"An error occurred: {e}").style('color:red; font-size:18px')

if __name__ == '__main__':
    # Initial UI setup
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    put_buttons([dict(label='Click Me!', value='fetch', color='success')], onclick=get_fact)

    # Keep the session alive
    hold()
