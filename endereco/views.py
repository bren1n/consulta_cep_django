import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from endereco.models import Endereco
from endereco.serializers import EnderecoSerializer
from endereco.utils import CustomException


class ListEndereco(APIView):
    def get(self, request):
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(instance=enderecos, many=True)
        return Response(data=serializer.data, status=200)
    
    def post(self, request):
        cep = request.data.get('cep', None)
        cep_exists = Endereco.objects.filter(cep=cep).exists()
        
        if cep_exists:
            raise CustomException(
                status_code=400,
                attr='cep',
                message='CEP já registrado.'
            )

        api_request = requests.get(f'http://viacep.com.br/ws/{cep}/json/')        

        if api_request.status_code == 400:
            raise CustomException(
                status_code=400,
                attr='cep',
                message='Formato de CEP inválido.'
            )
        elif 'erro' in api_request.json().keys():
            raise CustomException(
                status_code=404,
                attr='cep',
                message='CEP não registrado.'
            )
        
        endereco_data = api_request.json()
        endereco_data['cep'] = cep
        
        serializer = EnderecoSerializer(data=endereco_data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)
        
        return Response(data=serializer.errors, status=400)

class DetailEndereco(APIView):
    def get(self, request, cep):
        if not cep.isnumeric() or len(cep) != 8:
            raise CustomException(
                status_code=404,
                attr='cep',
                message='Formato de CEP inválido.'
            )
        
        try:
            endereco = Endereco.objects.get(cep=cep)
        except:
            raise CustomException(
                status_code=404,
                attr='cep',
                message='CEP não registrado.'
            )
        
        serializer = EnderecoSerializer(instance=endereco)
        
        return Response(data=serializer.data, status=200)