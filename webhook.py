import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook',methods=['post'])
def webhook():
    req = request.get_json(silent=True, force=True)
    #print(json.dumps(req, indent=4))
    res=makeResponse(req)
    #res= json.dumps(req, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeResponse(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    date = parameters.get("date")
    fulfillmentText=''
    if city is None:
        return None
    '''r=requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+city+'&appid=2d62943e869f2e25288dbcbd798dccff')
    json_object = r.json()
    weather=json_object['list']
    for i in range(0,31):
        if date in weather[i]['dt_txt']:
            print("in loop")
            condition= weather[i]['weather'][0]['description']
            break'''
    condition="  is cloudy and chances of rainy"
    fulfillmentText = "The forecast for "+city+ "for "+date+condition
    print(fulfillmentText)
    #weburl='https://webhook.site/c96238a6-06ce-4ce8-87d2-64c8ccf57952?'
    return{
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        fulfillmentText
                        ]
                    }
                }
            ]
        }
    
    '''return{
        "fulfillment": fulfillmentText,
        "displayText": fulfillmentText,
        "source": "apiai-weather-webhook"
    }'''
    #r=requests.post(weburl,data=json.dumps(data,indent=4),headers={'content-type':'application/json'})'''


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=True, port=port, host='0.0.0.0')

















