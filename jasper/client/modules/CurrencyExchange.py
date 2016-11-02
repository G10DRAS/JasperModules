# -*- coding: utf-8-*-

# Copyright 2016 g10dras.
__author__ = 'g10dras'

import re
import json
import urllib2
from urllib import urlopen
from semantic.numbers import NumberService
from client.mic import Mic

WORDS = ["CURRENCY", "EXCHANGE"]
		
def handle(text, mic, profile):
    # Vocab used in Currency Exchange Rate Module
    phrases = ["YES", "NO", "JAPANESE", "YEN", "AMERICAN", "DOLLAR", "INDIAN", "RUPEES", "EURO",
                            "SWISS", "FRANC", "BRITISH", "POUND", "CHINESE", "YUAN"]

    # Comment out below two lines if you are using Jasper in TEXT Mode			
    currexch_stt_engine = mic.active_stt_engine.get_instance('rateexch', phrases)
    mic = Mic(mic.speaker, mic.passive_stt_engine, currexch_stt_enginess)

    serviceNum = NumberService()
	
    def convertToCode(currency):
			
        code_list = {"INDIAN" : "INR", "RUPEES" : "INR", "YEN" : "JPY", "JAPANESE" : "JPY", 
                            "AMERICAN" : "USD", "DOLLAR" : "USD", "YUAN" : "CNH", "CHINESE" : "CNH", 
                            "EURO" : "EUR", "POUND" : "GBP", "BRITISH" : "GBP", " SWISS" : "CHF", 
                            "FRANC" : "CHF"}
		
        for key, value in code_list.iteritems():
                if key in currency.split():
                        return value
        return ''
		
    def currencyConverterYahoo(currency_from,currency_to,currency_input):
        yql_base_url = "https://query.yahooapis.com/v1/public/yql"
        yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+currency_from+currency_to+'")'
        yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

        yql_response = urllib2.urlopen(yql_query_url)
        yql_json = json.loads(yql_response.read())
        currency_output = currency_input * float(yql_json['query']['results']['rate']['Rate'])
        return currency_output

    while True:
            mic.say(" First Currency?")
            currency_from = convertToCode(mic.activeListen())

            mic.say(" Second Currency?")
            currency_to = convertToCode( mic.activeListen())
            
            if currency_from != "" and currency_to != "":
                mic.say(" Getting exchange rate of " + currency_from + " against " + currency_to + ".")
                currency_input = 1
                currency_input_str = serviceNum.parseMagnitude(currency_input)	

                try:
                    # YAHOO Services 
                    rate = currencyConverterYahoo(currency_from,currency_to,currency_input)
                    rateStr = serviceNum.parseMagnitude(rate)	
                     
                except (IOError, ValueError, KeyError, TypeError):
                    pass # invalid json
                    mic.say(" An error occurred. Maybe the A P I is off line?")
                    break 

                else:
                    pass # valid json
                    mic.say(" Okay, here is the exchange rate.")
                    mic.say(" It is approximately " + rateStr + " " + currency_to + " for " + currency_input_str + " " + currency_from + " .")
                    mic.say(" Do you want to continue?")
                    ans = mic.activeListen()
                    if "NO" in ans.split():
                        break 
                    continue 
            else:
                mic.say(" One or both currencies are not understood. Please try again.")   
                continue 
        
def isValid(text):
    return any(word in text.upper() for word in WORDS)		

