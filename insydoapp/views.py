from django.shortcuts import render
from utils import longest_substring
# Create your views here.



from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LongestStringForm

def longest_string_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LongestStringForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            list_of_strings = form.cleaned_data['list_of_strings']

            return render(request, 'longeststring.html', {'form': form, 'longest_substring': longest_substring(list_of_strings.split("\n"))})

    # if a GET (or any other method) we'll create a blank form
    else:
        #Initialize the form with a dummy data for testing purposes
        form = LongestStringForm(initial=
                                 {'list_of_strings':
"""aaa bbbb cccc rrrrr
aa fhgk deed
bbbn rrrrssddedebt bbboo
hello word, bbb"""
                                 })

    return render(request, 'longeststring.html', {'form': form})