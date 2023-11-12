# from users_event.tasks import test_task
#
import datetime
from datetime import timedelta

import stripe
from django.conf import settings
from django.db.models import Avg, Q
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from rest_framework import mixins
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from users_event.models import Event, Participant, Tag, Rating, BankOperation
from users_event.serializers import (
    EventInfoSerializer,
    TagSerializer,
    EventDetailSerializer,
    RatingSerializer,
    MeanRatingSerializer,
    ParticipantSerializer,
    ParticipantSerializerForCalendar,
)


@api_view(["GET"])
def get_pk_view(request):
    return Response({"pk_token": settings.STRIPE_PUBLISHABLE_KEY})


@api_view(["GET", "POST"])
def pay_event_view(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    products = stripe.Product.list(limit=100, active=True)
    print(products)
    print(request.data)
    product = None
    for existing_product in products:
        if existing_product.name == request.data["event"]["title"]:
            product = existing_product
            break
    if not product:
        product = stripe.Product.create(
            name=request.data["event"]["title"], images=["https://f.nodacdn.net/309636"]
        )
    price = None
    prices = stripe.Price.list(product=product.id, limit=1)
    if prices.data:
        price = prices.data[0]

    # Если цена не найдена, создать новую цену для продукта
    if not price:
        price = stripe.Price.create(
            unit_amount=request.data["event"][
                "price"
            ],  # Сумма в минимальных единицах валюты (например, центы)
            currency="usd",  # Валюта
            product=product.id,  # Идентификатор продукта
        )
    url = "http://localhost:5173/events/pay_response?payment_id={CHECKOUT_SESSION_ID}"
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price": f"{price.id}",  # Идентификатор цены в Stripe Dashboard
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url=url,
        cancel_url=url,
        metadata={"event_title": request.data["event"]["title"]},
    )
    print(session.id)
    return Response({"sessionId": str(session.id)})


@api_view(["GET", "POST"])
def pay_event_response_view(request):
    payment_id = request.GET.get("payment_id")
    session = stripe.checkout.Session.retrieve(payment_id)
    event_title = session.metadata.get("event_title")
    event = Event.objects.get(title=event_title)
    payment_intent_id = session.payment_intent
    payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

    payment_status = payment_intent.status
    payment_created = payment_intent.created
    payment_created = datetime.datetime.fromtimestamp(payment_created).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    print(payment_created)
    if payment_status == "succeeded":
        operation = BankOperation(
            user=request.user,
            event=event,
            status=payment_status,
            created_at=payment_created,
            payment_id=payment_id,
        )
        operation.save()

        return Response(
            {
                "status_pay": "ok",
                "event": EventDetailSerializer(event).data,
            }
        )
    else:
        return Response({"status_pay": "wrong"})


class ParticipantViewSetForCalendar(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ParticipantSerializerForCalendar

    def get_queryset(self, *args, **kwargs):
        return Participant.objects.filter(
            Q(user=self.request.user) & Q(is_organizer=False)
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ParticipantViewSet(APIView):
    """API для просмотра подписчиков мероприятия"""

    def get(self, request):
        event_id = request.GET["event_id"]
        subscribed_users = Participant.objects.filter(
            Q(event_id=event_id) & Q(is_organizer=False)
        )
        serializer = ParticipantSerializer(subscribed_users, many=True)
        return Response(serializer.data)


class SubscribeViewSet(APIView):
    """API для подписки/отписки пользователя на бесплатное мероприятие"""

    def post(self, request):
        print(request.data)
        event_id = request.data["event"]["id"]
        if "unsubscribe" not in request.data.keys():
            ans = Participant(user=request.user, event_id=event_id, is_organizer=False)
            ans.save()
            start_time = datetime.datetime.strptime(
                request.data["event"]["start_time"], "%Y-%m-%d %H:%M:%S"
            )
            notify_time = (start_time - timedelta(hours=1)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            date, time = notify_time.split(" ")
            print(date, time)
            year, month, day = date.split("-")
            hours, minutes, seconds = time.split(":")
            crontab_schedule = CrontabSchedule(
                minute=minutes,
                hour=hours,
                day_of_week="*",
                day_of_month=day,
                month_of_year=month,
                timezone="Europe/Moscow",
            )

            crontab_schedule.save()

            task = PeriodicTask(
                name=f"send_event_notification_{request.user.id}_{event_id}",
                task="users_event.tasks.send_event_notification",
                crontab=crontab_schedule,
                enabled=True,
                one_off=True,
                args=[event_id],
            )
            task.save()
        else:
            subscribe_to_delete = Participant.objects.get(
                event_id=event_id, user_id=request.user.id
            )
            task_to_delete = PeriodicTask.objects.get(
                name=f"send_event_notification_{request.user.id}_{event_id}"
            )
            crontab_to_delete = CrontabSchedule.objects.get(
                id=task_to_delete.crontab_id
            )
            subscribe_to_delete.delete()
            task_to_delete.delete()
            crontab_to_delete.delete()
        return Response({"message": "Subscribe successful"})


class TagViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    pagination_class = None
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class RatingViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Rating.objects.all()

    def get_serializer_class(self):
        if self.action == "mean_rate":
            return MeanRatingSerializer
        else:
            return RatingSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def mean_rate(self, request, *args, **kwargs):
        event_id = self.request.GET["event_id"]
        ratings = Rating.objects.filter(event=event_id)
        avg_rating = ratings.aggregate(Avg("rating"))["rating__avg"]
        print(avg_rating)
        serializer = self.get_serializer({"rate": avg_rating, "count": len(ratings)})
        return Response(serializer.data)


class EventViewSet(
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    permission_classes = []

    def get_serializer_class(self):
        if self.action in ("retrieve", "list"):
            return EventDetailSerializer
        else:
            return EventInfoSerializer

    def get_queryset(self, *args, **kwargs):
        if "slug" in self.request.GET.keys():
            category = self.request.GET["slug"]
            return Event.objects.filter(category=category)
        else:
            return Event.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, user_id=request.user.id)
        return Response(serializer.data)


class UserEventViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = EventInfoSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(user_id=self.request.user.id))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        if "user_id" in kwargs.keys():
            user_id = kwargs["user_id"]
            events = Event.objects.all()
            my_events_id = []
            for event in events:
                for obj in event.participant_set.all():
                    if user_id == obj.user_id and obj.is_organizer is True:
                        my_events_id.append(obj.event_id)
            return Event.objects.filter(id__in=my_events_id)
        else:
            return Event.objects.all()

    def perform_create(self, serializer):
        obj = serializer.save()
        return obj

    def create_new_tag(self, request, title):
        print(request.user, title)
        new_tag = Tag(title=title, user=request.user)
        new_tag.save()
        return new_tag

    def converting_data(self, request):
        """
        Создает новый тег, если его не существует и
        заменяет значения price и url на null
        :param request:
        :type request:
        :return:
        :rtype:
        """
        price = request.POST.get("price")
        if price == "null":
            price = None
        else:
            price = int(price)
        url = request.POST.get("url")
        if url == "null":
            url = None
        tag_names = request.data.getlist("tags")
        print(request.data)
        tags = []
        for tag_request in tag_names:
            tag = Tag.objects.filter(title=tag_request).first()
            if tag is None:
                tag = self.create_new_tag(request, tag_request)
            tags.append(tag.title)
        event_data = request.data.dict()
        event_data["tags"] = tags
        event_data["price"] = price
        event_data["url"] = url
        return event_data

    def create(self, request, *args, **kwargs):
        event_data = self.converting_data(request)
        serializer = self.get_serializer(data=event_data)
        serializer.is_valid(raise_exception=True)
        event = self.perform_create(serializer)
        ans = Participant(user=request.user, event=event, is_organizer=True)
        ans.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=self.converting_data(request), partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
