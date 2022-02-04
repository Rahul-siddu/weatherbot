from flask import Flask
import json
app=Flask(__name__)
@app.route('/api')
def webhook():
    a={"company":"sunlight","place":"delhi","employee details":[{"name":"rahul","state":"telangana"},
                                                                {"name":"utkarsh","state":"maharastra"},
                                                                {"name":"rajdeep","state":"gujarat"},
                                                                {"name":"umesh","state":"delhi"},
                                                                {"name":"kris","state":"us"}]}
    b=json.dumps(a,indent=5)
    return b
if __name__=='__main__':
    print("starting the app")
    app.run(debug=True)
    
