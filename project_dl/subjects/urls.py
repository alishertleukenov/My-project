from django.urls import path, include

import subjects.views

urlpatterns = [
    path('', subjects.views.students),
    path('subjects/<int:page_number>/', subjects.views.students),
    path('subjects/get/<int:student_id>/', subjects.views.student),
    path('page/<int:page_number>/', subjects.views.students),

]