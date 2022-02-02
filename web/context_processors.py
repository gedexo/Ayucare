
from .forms import SubscribeForm


def main_context(request):
    email_form = SubscribeForm()
    return {
        'email_form':email_form,
        'domain' : request.META['HTTP_HOST'],
    }