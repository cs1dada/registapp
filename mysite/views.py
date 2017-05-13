# _*_ encoding:utf-8 _*_
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
# messages framework
from django.contrib import messages
#database
from mysite import models, forms
#auth
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    polls = models.Poll.objects.all()

    messages.get_messages(request)

    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)

@login_required
def poll(request, pollid):
    try:
        poll = models.Poll.objects.get(id = pollid)
    except:
        poll = None

    if poll is not None:
        pollitems = models.PollItem.objects.filter(poll = poll).order_by('-vote')

    messages.get_messages(request)

    template = get_template('poll.html')
    html = template.render(locals())
    return HttpResponse(html)

@login_required
def vote(request, pollid, pollitemid):
    try:
        pollitem = models.PollItem.objects.get(id = PollItem)
    except:
        pollitem = None

    if pollitem is not None:
        pollitem.vote = pollitem.vote + 1
        pollitem.save()

    target_url = '/poll/' + pollid
    return redirect(target_url)

def login(request):
    if request.method == 'POST':
        #post method (write)
        #check login_form is valid 
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            #grab account info from client
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            # password verify from User (not models.User)
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    #save userinfo into session
                    auth.login(request, user)
                    print ("success")
                    messages.add_message(request, messages.SUCCESS, 'success login')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, 'account not active')
            else:
                messages.add_message(request, messages.WARNING, 'login fail')
        else:
            messages.add_message(request, messages.INFO, 'plz check input content')
    else:
        #empty instance for login.htm read login_form
        login_form = forms.LoginForm()

    template = get_template('login.html')

    html = template.render(locals(), request)
    response = HttpResponse(html)

    return response

''' raw auth method
        login_form = forms.LoginForm()
            try:
                # grab user data from database
                user = models.User.objects.get(name=login_name)
                # password verify
                if user.password == login_password:
                    # write session [username, useremail]
                    request.session['username'] = user.name
                    request.session['useremail'] = user.email
                    messages.add_message(request, messages.SUCCESS, 'success login')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, 'incorrect password')
            except:
                messages.add_message(request, messages.WARNING, 'no such member, cannot login')
        else:
            messages.add_message(request, messages.INFO, 'plz check input content')
    else:
'''
def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, ' log out !!!')
    return redirect('/')

@login_required(login_url='/login/')
def userinfo(request):
    #login?
    if request.user.is_authenticated():
        #get curent login user info  from auth.models User //request.user is User model object.
        username = request.user.username
        #get user info  from User (not models.User)
        user = User.objects.get(username=username)

    try:
        #read user info from Profile database by user //User<1:1>Profile
        userinfo = models.Profile.objects.get(user=user)
    except:
        #if read empty userinfo
        #create instance Profile for specific user
        userinfo = models.Profile(user=user)

    #send ProfileForm POST?
    if request.method == 'POST':
        #WRITE
        #container [form ProfileForm]  save [Profile(userinfo) instance(user-client post)]
        profile_form = forms.ProfileForm(request.POST, instance=userinfo)
        if profile_form.is_valid():
            messages.add_message(request, messages.INFO, "個人資料已儲存")
            profile_form.save()  
            return HttpResponseRedirect('/userinfo')
        else:
            messages.add_message(request, messages.INFO, '要修改個人資料，每一個欄位都要填...')
        """
        #WRITE
        #get login user info
        user = User.objects.get(username = username)
        #create instance Diary for specific user
        diary = models.Diary(user=user)
        #container [form DiaryForm]  save [diary instance(user post)]
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO, "DIARY is stored ")
            post_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, "EVERY column need to fill !!!")
        """
    else:
        #READ
        profile_form = forms.ProfileForm()

    template = get_template('userinfo.html')
    html = template.render(locals(), request)
    return HttpResponse(html)

def listing(request):
    template = get_template('listing.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()

    html = template.render(locals())

    return HttpResponse(html)

def post2db(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = "您的訊息已儲存，要等管理者啟用後才看得到喔。"
            post_form.save()
            return HttpResponseRedirect('/list/')
        else:
            message = '如要張貼訊息，則每一個欄位都要填...'
    else:
        post_form = forms.PostForm()
        message = '如要張貼訊息，則每一個欄位都要填...'          

    template = get_template('post2db.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)

    return HttpResponse(html)

@login_required(login_url='/login/')
def posting(request):
    #login?
    if request.user.is_authenticated():
        #get curent login user info  from auth.models User
        username = request.user.username
        useremail = request.user.email

    messages.get_messages(request)

    if request.method == 'POST':
        #WRITE
        #get login user info
        user = User.objects.get(username = username)
        #create instance Diary for specific user
        diary = models.Diary(user=user)
        #container [form DiaryForm]  save [diary instance(user post)]
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO, "DIARY is stored ")
            post_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, "EVERY column need to fill !!!")
    else:
        #READ
        post_form = forms.DiaryForm()
        messages.add_message(request, messages.INFO, "EVERY column need to fill !!!")

    template = get_template('posting.html')
    html = template.render(locals(), request)

    return HttpResponse(html)

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "感謝您的來信，我們會儘速處理您的寶貴意見。"
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email  = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']

            mail_body = u'''
網友姓名：{}
居住城市：{}
是否在學：{}
反應意見：如下
{}'''.format(user_name, user_city, user_school, user_message)

            email = EmailMessage(   '來自【不吐不快】網站的網友意見', 
                                    mail_body, 
                                    user_email,
                                    ['skynet.tw@gmail.com'])
            email.send()
        else:
            message = "請檢查您輸入的資訊是否正確！"
    else:
        form = forms.ContactForm()

    template = get_template('contact.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)

    return HttpResponse(html)

