from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'firstapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('savedata/', views.crud.savedata, name='savedata'),
    path('updatedata/', views.crud.updatedata, name='updatedata'),
    re_path(r'^(\d+)/editdata/$', views.crud.editdata, name='editdata'),
    re_path(r'^(\d+)/deletedata/$', views.crud.deletedata, name='deletedata'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
