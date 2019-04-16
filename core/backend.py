from core.models import Usuario 
 
class MyBackend:
    def authenticate ( self , request):
        user = Usuario.objects.get(request.POST.get('email'))
        if user:
            senha = request.POST.get("senha")
            if user.senha == senha:
                return user 
            return "Usuário ou senha incorretos"
        return "usuário não encontrato"

