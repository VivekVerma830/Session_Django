from django.shortcuts import render


# Create your views here.

def set(request):
    # cookie----------------------
    # data = render(request, 'set.html')
    # data.set_cookie('name','Vivek',max_age=5*60*60,httponly=True,secure=True)
    # data.set_cookie('age','23',max_age=3*60*60,httponly=True,secure=True)
    # data.set_cookie('city','Bhopal',max_age=5*60*60,httponly=True,secure=True)
    # return data

    #session=================default time is 14 day data rhta h 
    l1={'id':1,'nm':'neha'}
    l2={'id':2,'nm':'om'}
    l=[l1,l2]
    request.session['data']=l
    return render(request,'set.html') 

def get(request):
    # cookie------------------------------------
    # print(request.COOKIES)
    # nm= request.COOKIES['name']
    # age= request.COOKIES['age']
    # ct= request.COOKIES['city']
    # data={'name':nm,
    #       'age':age,
    #       'city':ct}
    # return render(request,'get.html',data)
    d=request.session.get('data','guest')
    return render(request ,'get.html',{'nm':d})

# def delete(request):
#     data = render(request,'delete.html')
#     data.delete_cookie('name')
#     data.delete_cookie('age')
#     data.delete_cookie('city')
#     return data

def delete(request):
    # if 'data' in request.session:
    request.session.flush()
    return render(request ,'delete.html' )