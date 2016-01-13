from django.shortcuts import redirect

class RequireCurrentUser(object):
    def process_request(self, request):
        if request.path == '/':
            return None
