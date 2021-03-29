import requests
import json


headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer sk-0v2la3a279fRolIzQR4l5t71OvD3YAmQpwLWiomU',
}



def prompt():
    promptoutput = input(str("Input prompt: "))
    global data
    data = '{ "prompt": "%s", "max_tokens": 100 }' % promptoutput
def call():

    prompt()

    response = requests.post('https://api.openai.com/v1/engines/ada/completions', headers=headers, data=data)

    output = response.json()
    global textoutput
    textoutput1 = output.get("choices")
    textoutput = str(textoutput1)

    resultant = textoutput.split(':')
    global resultant2
    resultant2 = str(resultant[1])
    global resultant3
    resultant3 = resultant2.strip("'index")

    return resultant3








# def listfunction():
#     res = []
#     for el in textoutput:
#         sub = el.split()
#         res.append(sub)

#     return(res)

call()
