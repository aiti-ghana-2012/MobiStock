import requests
from bs4 import BeautifulSoup
import pprint
import json

"""
Requires:
BeautifulSoup (sudo pip install beautifulsoup4)
requests (sudo pip install requests) <-- i think
"""

URL = "http://www.gse.com.gh/gseticker/tickerView.php"

HEADERS = {
	'connection' : 'keep-alive',
	'accept-encoding' : 'gzip,deflate,sdch',
	'accept-language' : 'en-US,en;q=0.8',
	'accept' : '*/*',
	'cache-control' : 'max-age=0',
	'host' : 'www.gse.com.gh',
	'origin' : 'http://www.gse.com.gh',
	'referer' : 'http://www.gse.com.gh/',
	'content-length' : '0',
	'user-agent' : 'Mozilla/5.0',
}

def get_ticker_data():
    
    def error(string):
        return "Something has changed in the reponse HTML!\n%s" % string

    r = requests.post(URL, headers=HEADERS)

    gse_soup = BeautifulSoup(r.content)

    table_rows = gse_soup.find_all('tr')

    if not len(table_rows) == 2:
        raise ValueError(error("Expected two <tr> elements, got %d" % len(table_rows)))


    tickers, volumes = table_rows #unpacking a two element list

    ticker_cells = tickers.find_all('td')
    volume_cells = volumes.find_all('td')

    # lets assert that the first one is different, has no span
    if ticker_cells[0].find_all('span'):
        raise ValueError(error("Expected first cell of the ticker row to have no span elements!"))
    
    # ok, since we made sure that the first cell is special, we are going to iterate through the rest!
    # lets form our datastructure now.
    ticker_data = {}
    ticker_order = []

    for ticker_cell in ticker_cells[1:]:
        ticker_cell_spans = ticker_cell.find_all('span')
    
        if not len(ticker_cell_spans) == 3:
            raise ValueError(error("Expected 3 spans inside of ticker cell: %s" % str(ticker_cell)))
    
        data = [span.text.strip() for span in ticker_cell_spans]
    
        ticker_symbol = data[0]
    
        try:
            price = float(data[1])
        except ValueError:
            raise ValueError(error("Expected to be able to create a float out of content of second span %s"%data[1]))
    
        try:
            change = float(data[2])
        except ValueError:
            raise ValueError(error("Expected to be able to create a float out of content of second span %s"%data[1]))
    
        ticker_order.append(ticker_symbol)
        ticker_data[ticker_symbol] = {
            'price' : price,
            'change' : change,
            'symbol' : ticker_symbol,
        }
    
    if not len(ticker_order) == len(volume_cells) - 1:
        raise ValueError(error("Expected number of volume cells to be one more than number of ticker symbols!"))
    
    for volume_cell, symbol in zip(volume_cells[1:],ticker_order): #throw away the first td, its garbage
    
        try:
            volume = int(volume_cell.text)
        except ValueError:
            raise ValueError(error("Expected content of volume cell to be integer! got: %s" % volume_cell))
        
        ticker_data[symbol]['volume'] = volume
    
    
    
    return [ticker_data[symbol] for symbol in ticker_order]
    
    
    
if __name__ == "__main__":
    print json.dumps(get_ticker_data(), indent=4)