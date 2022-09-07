from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from .serializers import CreateUserSerializer
from collections import defaultdict
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bet, Variant, Event, BetVariant
from .serializers import BetSerializer, VariantSerializer, EventSerializer, BetVariantSerializer
from datetime import datetime


class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # We create a token than will be used for future auth
        token = Token.objects.create(user=serializer.instance)

        token_data = {"token": token.key}
        return Response(
            {**serializer.data, **token_data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class LogoutUserAPIView(APIView):
    queryset = get_user_model().objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    content = Bet.objects.filter(bet_maker=request.user)
    serializer = BetSerializer(content, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_events(request):
    today = datetime.today().strftime('%Y-%m-%d')

    events = list()

    for result in Event.objects.filter(active_due_date__gte=today).values():
        events.append({
            'event': result,
            'variants': VariantSerializer(
                Variant.objects.filter(event__id=result['id']),
                many=True
            ).data
        })

    return Response(events)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication, SessionAuthentication])
def get_bets(request):
    bets = list()

    for result in BetSerializer(Bet.objects.filter(bet_maker=request.user), many=True).data:
        bets.append({
            'bet': result,
            'variants': BetVariantSerializer(
                BetVariant.objects.filter(bet__id=result['id']),
                many=True
            ).data
        })

    return Response(bets)
