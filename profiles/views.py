from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Api view de prueba"""
    
    def get(self, request, format=None):
        """Return a list of APIView features"""
        
        an_apiview = [
            'usamos metodos HTTP como funciones (get,post,patch,put,delete)',
            'es similar a una vista tradicional de django',
            'nos da mayor control sobre la loginca de nuestra aplicacion',
            'esta mapeado manualmente a los urls'
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})