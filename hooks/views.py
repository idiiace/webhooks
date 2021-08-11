from django.shortcuts import render ,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
import requests  

def main(data):
    url = "https://hook.integromat.com/8iio1cu6c43wcd8yqf6dj8jcitaqa7nh"
    data = data
    try:
        open('notifications').read()
    except:
        open('notifications','w').write('1')

    #check if data is duplicate by comparing with existing data .txt file for the id
    ids=open('notifications').read()
    for i in ids.splitlines():
        if int(i) == data['id']:
            print('duplicate')
            return True
    
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    print(r.status_code)
    open("notifications",'a').write(str(data['id'])+'\n')
    

@csrf_exempt
def api(request):
    data=json.loads(request.body)
    print(data)
    main(data)
    return HttpResponse("success")

