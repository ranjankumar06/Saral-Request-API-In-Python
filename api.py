import json
from pprint import pprint
import requests
url=("http://saral.navgurukul.org/api/courses")
res= requests.get(url)
a=res.text
r=json.loads(a)
e=[]
for i in r:
    d=1
    for j in r[i]:
        print(d,'.',j['name'])
        d=d+1
        e.append(j['id'])
imp=int(input("Enter a id:"))
r=e[imp-1]
pr='http://saral.navgurukul.org/api/courses/'+r+'/exercises'
var=requests.get(pr)
var1=var.text
var2=json.loads(var1)
f=open('saral_ex.json','w')
json.dump(var2,f,indent=4)
f.close()
c=1
slug_list=[]
for i in var2['data']:
    print(c,i['name'])
    slug_list.append(i['slug'])
    c+=1
    for j in i:
        if i['childExercises'] == []:
            pass
        else:
            for k in i['childExercises']:
                print(k['name'])
            break
sl=int(input("Enter a id:"))
s=slug_list[sl]
print(s)
slug='http://saral.navgurukul.org/api/courses/'+r+'/exercise/getBySlug?slug='+s
slug1=requests.get(slug)
slug2=slug1.json()
print(slug2['content'])

    


            




    
        