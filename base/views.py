from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import server_conf, dim_sale_ordertransaction
#from .forms import RoomForm,  MyUserCreationForm

from datetime import date
from datetime import timedelta
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import json
# Create your views here.

# rooms = [
#     {'id': 1,'name': 'lets leran python'},
#     {'id': 2,'name': 'Design with me'},
#     {'id': 3,'name': 'Frontend developers'},
# ]
# -------------------------------------------------------------------------------------
def loginPage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return  switchUser(request) #redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist.')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return switchUser(request) #redirect('home')
        else:
            messages.error(request,'Username or Password does not exist.')
        
        
    context = {'page': page}
    return render(request, 'base/login_register.html', context)
# -------------------------------------------------------------------------------------
def logoutUser(request):
    logout(request)
    return redirect('login')

# -------------------------------------------------------------------------------------
# def registerUser(request):
#     form = UserCreationForm()
    
    
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'An error occurred during registration')
            
#     context = {'form': form}
#     return render(request, 'base/login_register.html',context)

# # -------------------------------------------------------------------------------------
@login_required(login_url='login')
def switchUser(request):
    if request.user.username == 'sribilone' or request.user.username == 'admin@system':
        return redirect('admin-home')
    else:
        return redirect('home')

# -------------------------------------------------------------------------------------
@login_required(login_url='login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    # rooms = Room.objects.filter(
    #     Q(topic__name__icontains=q) |
    #     Q(name__icontains=q) |
    #     Q(description__icontains=q)
    #     )
    
    # topics = Topic.objects.all()
    # room_count = rooms.count()
    
    # context = {'rooms': rooms, 
    #            'topics': topics,
    #            'room_count': room_count,
    #            }
    
    conn = psycopg2.connect(database="seefah",
                        host="172.26.117.18",
                        user="seefah",
                        password="zxc123**",
                        port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM dim_sale_ordertransaction WHERE saledate = '2022-10-24'")
    seefah_count = cursor.fetchone()

    seefah = int(seefah_count[0])
    counts = [{
        'seefah':seefah
    }]
    
    cursor = conn.cursor()
    cursor.execute("SELECT date_part('MONTHS', saledate),  COUNT(*) AS count FROM dim_sale_ordertransaction GROUP BY date_part('MONTHS', saledate)")
    sale_count = cursor.fetchall()
     
    sale_num = []
    sale_date = []
    for i in sale_count:
        # match int(i[0]):
        #     case 1: sale_date.append("Jan.")
        #     case 2: sale_date.append("Feb.")
        #     case 3: sale_date.append("Mar.")
        #     case 4: sale_date.append("Apl.")
        #     case 5: sale_date.append("May.")
        #     case 6: sale_date.append("Jun.")
        #     case 7: sale_date.append("Jul.")
        #     case 8: sale_date.append("Aug.")
        #     case 9: sale_date.append("Sep.")
        #     case 10: sale_date.append("Oct.")
        #     case 11: sale_date.append("Nov.")
        #     case 12: sale_date.append("Dec.")
        sale_date.append(i[0])
        sale_num.append(i[1])

    sale_data = [{
        'mount':sale_date,
        'num':sale_num
    }]
    

    
    context = {'counts':counts,
               'data':sale_data
               }
    
    return render(request, 'base/home.html',context)
# -------------------------------------------------------------------------------------
@login_required(login_url='login')
def adminHome(request):
    return render(request, 'base/admin-home.html')

# # -------------------------------------------------------------------------------------
# @login_required(login_url='login')
# def room(request, pk):
#     # room = None
#     # for i in rooms:
#     #     if i['id'] == int(pk):
#     #         room = i
#     room = Room.objects.get(id=pk)
#     context = {'room': room}
    
#     return render(request, 'base/room.html',context)
# # -------------------------------------------------------------------------------------

@login_required(login_url='login')
def serverConf(request):
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # server = {}
    
    # if q == 'seefah':
    #     server = server_conf.objects.get(database_name="seefah")
    #     print(server)
    # elif q == 'duobao':
    #     server = [{
    #         'set':'value',
    #         'qduobao': 'active',
    #         'Host': '6230.2225.25563',
    #         'Port': '78955',
    #         'Database': 'Duobao database center',
    #         'Username': 'sribilone',
    #         'Password': '123456',
    #     }]
    # elif q == 'osakaohsho':
    #     server = [{
    #         'set':'value',
    #         'qosakaohsho': 'active',
    #         'Host': '78555.25566.2588',
    #         'Port': '1255',
    #         'Database': 'osakaohsho database center',
    #         'Username': 'sribilone',
    #         'Password': '123456',
    #     }]
    # elif q == 'bakebros':
    #     server = [{
    #         'set':'value',
    #         'qbakebros': 'active',
    #         'Host': '85256.2593.97122',
    #         'Port': '8711236',
    #         'Database': 'bakebros database center',
    #         'Username': 'sribilone',
    #         'Password': '123456',
    #     }]
    # else:
    #     server = [{
    #         'set':'default',
    #     }]
                                
    #room = Room.objects.get(id=pk)
   
    #----------------------------
    # form = RoomForm()
    # if request.method == 'POST':
    #     #print(request.POST)
    #     form = RoomForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    
    #Member.objects.filter(firstname='Emil').values()
    qid = 1
    server = server_conf.objects.all()
    if q == 'default':
        server = [{'set':'default'}]
    else:
        if q == 'seefah':
            qid = 1
        elif q == 'duobao':
            qid = 2
        elif q == 'osakaohsho':
            qid = 3
        elif q == 'bakebros':
            qid = 4
            
        server = server_conf.objects.filter(id=qid).values()
        
    
    
    if request.method == 'POST':
        server = server_conf.objects.get(id=qid)
        server.host = request.POST.get('host')
        server.port = request.POST.get('port')
        server.database_name = request.POST.get('database_name')
        server.username = request.POST.get('username')
        server.password = request.POST.get('password')
        server.save()
        return redirect('home')

    context  = {'server':server}
    
    return render(request, 'base/server_conf.html',context)

# # -------------------------------------------------------------------------------------
@login_required(login_url='login')
def updateRoom(request,pk):
    room = server_conf.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse("You are not allowed")
    
    if request.method == 'POST':
        #print(request.POST)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'server': form}
    return render(request, 'base/room_form.html', context)
# # -------------------------------------------------------------------------------------

#Seefah ----from sqlalchemy import create_engine

def conPostgreSQL(uid,pwd,host,db):
        con_string_PostgreSQL=f'postgresql://{uid}:{pwd}@{host}:5432/{db}'
        connect_PostgreSQL = create_engine(con_string_PostgreSQL,pool_pre_ping=True)
        print(f'╰┈➤ Connecting PostgreSQL Sever: {host}')
        return connect_PostgreSQL
    
connect_PostgreSQL = conPostgreSQL('seefah','zxc123**','172.26.117.18','seefah')


def SQL_query(connection,sql):
    # PostgreSQL connection
    df_query = pd.read_sql(str(sql),connection)
    return df_query

@login_required(login_url='login')
def dataWarehouse(request):
    #table = dim_sale_ordertransaction.objects.all()
    month = 0
    sql = "SELECT * FROM dim_sale_ordertransaction ORDER BY saledate DESC LIMIT 500"
    if request.method == 'POST':
        month = request.POST.get('month')
        if int(month) == 0:
            sql = "SELECT * FROM dim_sale_ordertransaction ORDER BY saledate DESC LIMIT 500"
        else:
            sql = "SELECT * FROM dim_sale_ordertransaction WHERE EXTRACT(MONTH FROM saledate) = "+str(month)+"ORDER BY saledate DESC LIMIT 500" 
        #return redirect('data-warehouse')
    df = SQL_query(connect_PostgreSQL,sql)
    df['saledate']=df['saledate'].astype(str)
    df['opentime']=df['opentime'].astype(str)
    df['paidtime']=df['paidtime'].astype(str)
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    
    context = {'table': data}
    return render(request, 'base/data_warehouse.html',context)
# -------------------------------------------------------------------------------------

@login_required(login_url='login')
def userManagemant(request):
    user = User.objects.all()
    
    context = {'users': user}
    
    return render(request, 'base/user_management.html',context)
# -------------------------------------------------------------------------------------
@login_required(login_url='login')
def userRegistration(request):
    
    # if request.method == 'POST':
        
    #     User.objects.create(
    #         first_name = request.POST.get('fname'),
    #         last_name = request.POST.get('lname'),
    #         email = request.POST.get('email'),
    #         username = request.POST.get('username'),
    #         password = request.POST.get('password'),
    #     )
    #     return redirect('user-management')
    
    # form = MyUserCreationForm()

    # if request.method == 'POST':
    #     form = MyUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.username = user.username.lower()
    #         user.save()
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'An error occurred during registration')
    
    return render(request, 'base/user_registration.html')

@login_required(login_url='login')
def userDelete(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    q = int(q)

    usera = User.objects.get(id=q)
    
    if request.method == 'POST':
            username = request.user 
            password = request.POST.get('password')
            print(username, password)
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request,'User does not exist.')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                usera.delete()
                redirect('user-management')
            else:
                print("Her")
    
    context = {'user': usera.username}
    
    return render(request, 'base/user_delete.html',context)

@login_required(login_url='login')
def userEdit(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    q = int(q)

    userd = User.objects.get(id=q)
    
    context = {'fname': userd.first_name,
               'lname': userd.last_name,
               'email': userd.email,    
               
               
               }
    
    return render(request, 'base/user_edit.html',context)