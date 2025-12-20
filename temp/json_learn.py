json_string='''
{ "list":[
    { "product":"laptop",
      "price":7500,
      "available":true
    }
    ]
    }
'''
data=json.loads(json_string)
print(data["list"])    