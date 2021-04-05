from django.urls import path

from dashboard import views as d_views
from registration import views as r_views
from questionnaire import views as q_views
from medications import views as m_views

urlpatterns = [
    path('', d_views.postsign, name="login"),
    path('register/', r_views.register_new_doctor, name="register"),
    path('add_patient/', r_views.register_new_patient, name="add_patient"),
    path('home/', d_views.home, name="home"),
    path('logout/', d_views.user_logout, name="logout"),
    path('patient_detail/', d_views.patient_detail, name="patient_detail"),
    path('patient_detail/med_update', d_views.update_medicine, name="patient_detail_update_med"),
    path('patient_detail/med_delete', d_views.delete_medicine, name="patient_detail_delete_med"),
    path('patient_detail/check', d_views.patient_detail_check, name="patient_detail"),
    path('patient_detail/send_medication_notif', d_views.send_medication_notif, name="send_medication_notification"),
    path('patient_detail/send_questionnaire_notif', d_views.send_questionnaire_notif, name="send_questionnaire_notification"),


]
