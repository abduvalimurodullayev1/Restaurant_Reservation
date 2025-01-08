from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.reservation.permission import IsAuthor
from apps.reservation.filter import RestaurantFilter
from apps.reservation.models import Reservation
from apps.reservation.pagination import RestaurantPagination
from apps.reservation.serializers import ReservationSerializer, RestaurantSerializer
from apps.reservation.pdf import generate_reservation
from apps.reservation.models import Restaurant

class ReservationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reservations = Reservation.objects.filter(user=request.user)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)


class ReservationApiView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ReservationSerializer,
        responses={
            status.HTTP_201_CREATED: ReservationSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad Request"
        }
    )
    def post(self, request):
        restaurant_id = request.data.get('restaurant')
        existing_reservation = Reservation.objects.filter(user=request.user, restaurant_id=restaurant_id).first()

        if existing_reservation:
            return Response({"detail": "Siz bu restorandan avval bron qilgansiz."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationDelete(DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthor]
    lookup_field = "pk"


class ReservationUpdate(UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthor]
    lookup_field = "pk"


class RestaurantView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = RestaurantFilter
    pagination_class = RestaurantPagination
    filterset_fields = ['title']
    search_fields = ['title']


class GenerateReservationPdf(APIView):
    def get(self, request, reservation_id):
        user = request.user
        try:
            reservation = Reservation.objects.get(id=reservation_id)

            if reservation.user == user:
                pdf_reservation = generate_reservation(user, reservation)

                response = HttpResponse(pdf_reservation, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="reservation_{reservation_id}.pdf"'
                return response
            else:
                return Response({"detail": "Sizning broningiz emas"}, status=status.HTTP_403_FORBIDDEN)

        except Reservation.DoesNotExist:
            return Response({"detail": "Bron topilmadi"}, status=status.HTTP_404_NOT_FOUND)