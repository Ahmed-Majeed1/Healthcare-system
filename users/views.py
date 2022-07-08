from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .face_register import face_reg
from .face_compare import face_test
from django.contrib.auth import authenticate, login as log
from . forms import ppUpdateForm
from django.core.mail import send_mail





@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ppUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your Picture has been updated!')
            return redirect('profile')
    else:
        p_form = ppUpdateForm(instance=request.user.profile)
            
    context = {
    'p_form': p_form
    }    
    return render(request, 'users/profile.html', context)
    
    
    
    
@login_required
def face_register(request):
    current_user = request.user
    name = current_user.username
    face_reg(name)
    return redirect('profile')

# def face_compare(request):
    # if request.method == 'POST':
    #     form = faceon(request.POST, instance=request.user.profile.face)
    #     if form.is_valid():
    #         form.save()
    #         context = {'form' : form}
    #         messages.success(request, f'Face ID Turned on')
    #         return render(request, 'users/profile.html', context)
    # if face_test() == True:
    #     messages.success(request, f'Your face was recognized, Logged in Successfully!')
    #     return redirect('profile')
    
    # if face_test() == False:
    #     messages.success(request, f"Face wasn't recognized, Try Again!")
    #     return redirect('doctors')

def login(request):
    
    
    uname = face_test()
    password = ('healthcare')
    if uname == 'unknown':
        messages.MessageFailure(request, f'There was a problim logging you in, Try Again')
        return redirect('prelogin')
    user = authenticate(request, username = uname, password = password)
    if user is not None:
        log(request, user)
        messages.success(request, f"You're Logged in Successfully!")
        return redirect('profile')
    
    else:
        messages.MessageFailure(request, f'There was a problim logging you in, Try Again')
        return redirect('login')
    
def prelogin(request):
    return render(request, 'users/prelogin.html')



def send(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data = {
            'name' : name,
            'email' :email,
            'subject' : subject,
            'message' : message,
        }
        message = '''
        Name: {}
        Email: {}
        Message: {}
      
        '''.format(data['name'], data['email'], data['message'])
        send_mail(data['subject'], message, '', ['a7m2d.majeed@gmail.com'])
        messages.success(request, 'Email Sent Successfully')
        
    return render(request, 'blog/contact.html', {})