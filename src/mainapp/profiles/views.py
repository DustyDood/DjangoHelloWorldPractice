from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from .forms import UserForm


# Create your views here.
def home_page(request):
    users = UserProfile.objects.all()
    return render(request, 'home.html', {'users': users})


# I need to review this block more later. I copied it from the Tech Academy video,
# but I'm not comfortable fully understanding it yet.
def user_details(request, pk):
    # Here, we take the string pk and store it as an int. Why?
    pk = int(pk)
    # So here we can pass the int as a primary key to get_object_or_404,
    # which finds a record in our model UserProfile with the primary key
    # of pk. This is how user_details knows which record to grab!
    item = get_object_or_404(UserProfile, pk=pk)
    # Now, the form variable is an instance of the UserForm class. The issue
    # is that UserForm inherits from ModelForm, which I don't know the properties
    # of yet. More research is needed!
    form = UserForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            print("Saved data")
            return redirect('home_page')
        else:
            print(form.errors)
    else:
        print("Not posting yet! Going to user_info")
        """
        This part is calling on the main page when we click on someone and click the JS button
        to load the new page. Why is this loop getting called again when the delete button is pressed?
        """
        return render(request, 'profiles/user_info.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        print("Boop")
        # Essentially, using item, the instance in the dB based off of the primary key
        # passed through the URL patter is brought up!
        item.delete()
        return redirect('home_page')
    context = {"item": item,}
    return render(request, "profiles/confirm_delete.html", context)


def confirmed(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('home_page')
        else:
            return redirect('home_page')
