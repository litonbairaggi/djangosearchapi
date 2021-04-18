from django.urls import path
from . views import AgentListView, AgentDetailView, TopSellerListView


urlpatterns = [
    path('', AgentListView.as_view()),
    path('<int:pk>', AgentDetailView.as_view()),
    path('topseller', TopSellerListView.as_view()),
]