# ORIGINAL VERSION - fully synchronous

import time
import random
import logging

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def get_market_data(market):
    """ 
    Calls the API and return data for a particular market 

    Likely steps:
    1. Initialise the market data API and authenticate
    2. Make a call to the API
    3. Retry X times if response failed
    4. Parse the response and return the market data

    Returns: dict of market data
    """

    logging.info(f"{market} - Started fetching market data.")
    time.sleep(1)
    logging.info(f"{market} - Finished fetching market data.")

    return {"latest_price": 44.1, "volume": 1030}


def get_database_data(market):
    """ 
    Fetches data about this market and our trading status from our database 

    Likely steps:
    1. Initialise our database connection
    2. Query database for our market data
    3. Await response
    4. Parse and return the database data

    Returns: dict of database data
    """

    logging.info(f"{market} - Started calling database.")
    time.sleep(0.5)
    logging.info(f"{market} - Finished fetching database data.")

    return {"prices": [42, 41, 44, 45.5], "position": "long"}


def trade_logic(market, market_data, database_data):
    """ 
    Makes decision on whether to trade given the latest market data and 
    information on current state and past prices (from our database)
    
    Returns: 'go long', 'go short', 'exit position', None
    """

    action = random.choice(["go long", "go short", "exit position", None])
    logging.info(f"{market} - Trading logic decision => {action}.")

    return action


def execute_trade(market, action):
    """
    Makes a trade via the API and responds once completed.
    May have multiple retrys before raising exception if it failed.

    Likely steps:
    1. Initialise the trading API
    2. Post trade to the API
    3. Confirm success in response or retry if it failed
    4. Return the response once successful

    Returns: dict of trade_information or raises Exception
    """

    logging.info(f"{market} - Posting {action} trade.")
    time.sleep(5)
    logging.info(f"{market} - {action} trade successful.")

    return {"success": True, "trade_details": {}}


def update_database(market, market_data, trade):
    """
    Updates the database data with the results of the recent trade and updated market data

    Likely steps:
    1. Post the new market data to the database
    2. Post the trade if it exists to the database and update the market position
    """

    logging.info(f"{market} - Started updating database.")
    time.sleep(0.7)
    logging.info(f"{market} - Finished updating database data.")


def run(market):
    """
    Run the bot cycle once now for a market. 

    1. Reads market data from an API
    2. Reads data from a database
    3. (once both are available) Calculates some logic to decide on a trade
    4. (if logic says we should trade) Executes a trade via an API
    5. (when trade is completed) updates the database

    Returns - action result of this cycle
    """

    logging.critical(f"{market} - Starting the bot cycle.")

    market_data = get_market_data(market)
    database_data = get_database_data(market)

    action = trade_logic(market, market_data, database_data)
    if action is not None:
        trade = execute_trade(market, action)
    else:
        trade = None
        logging.info(f"{market} - No trade to post.")

    update_database(market, market_data, trade)

    logging.critical(f"{market} - Finished the bot cycle.")
    return action


def run_all():
    """
    Run the bot cycle for all markets.
    Perhaps this method would be called by a cron job or similar to do every 5 minutes.
    """

    logging.critical(f"Starting up the trading bot.")
    start = time.time()

    MARKETS = ["AAPL", "AMZN", "MSFT"]

    trades = []
    for market in MARKETS:
        action = run(market)
        trades.append((market, action))

    logging.info(f"Summary of trades: {trades}")

    logging.critical(f"Finished everything. Took {time.time() - start} seconds.")


if __name__ == "__main__":
    run_all()
