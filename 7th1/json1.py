import json
jsonstring = '''{
  "IWS": [
    {
      "item": null,
      "salescy": "9267071.96",
      "salespy": null,
      "growth": null,
      "gmcy": null,
      "gmpy": null,
      "growth_gm": null
    },
    {
      "item": "CLOUD",
      "salescy": "30584865.34",
      "salespy": "30584865.34",
      "growth": "0.00",
      "gmcy": null,
      "gmpy": null,
      "growth_gm": null
    }
  ]
}'''
#print(jsonstring)
jsondata = json.loads(jsonstring)
print(jsondata['IWS'])
print('a')
