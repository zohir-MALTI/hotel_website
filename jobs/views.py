from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import *
from .models import *


def home(request):
    return render(request, 'jobs/home.html', {'jobs_count': Job.objects.count()})


def contact(request):
    return render(request, 'jobs/contact.html')


def jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/jobs.html', {'jobs': jobs,
                                              'jobs_count': Job.objects.count()})


def show_CVs(request):
    CVs = CV.objects.all()
    return render(request, 'jobs/show_CVs.html', {'CVs': CVs,
                                                  'CVs_count': CV.objects.count()})


@login_required(login_url="/accounts/login")
def hiring(request):
    if request.method == 'POST':
        print("JJJJJJJJJJJJJJJJJJ")
        job = Job.objects.create(
            title= request.POST["title"],
            company= request.POST["company"],
            location= request.POST["location"],
            salary= request.POST["salary"],
            link= request.POST["link"],
            category= request.POST["category"],
            contract_type= request.POST["contract_type"],
            description= request.POST["description"]
        )
        job.save()
        return render(request, 'jobs/hiring.html', {'success': 'Annonce créée avec succés !'})
    else:
        return render(request, 'jobs/hiring.html')


@login_required(login_url="/accounts/login")
def drop_CV(request):
    if request.method == 'POST':

        cv_file = CV.objects.create(
            picture= request.POST["picture"],
            firstname= request.POST["firstname"].capitalize(),
            lastname= request.POST["lastname"].upper(),
            email= request.POST["email"].lower(),
            location= request.POST["location"].capitalize(),
            category= request.POST["category"],
            description= request.POST["description"],
            cv_file= request.POST["cv_file"],
            user_id= request.user,
        )
        cv_file.save()
        return render(request, 'jobs/drop_CV.html', {'success': 'Votre CV a été déposé avec succés !'})
    else:
        return render(request, 'jobs/drop_CV.html')


def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job_likes_count = Likes.objects.filter(job_id=job_id).count()
    job_comments = Comments.objects.filter(job_id=job_id)

    exists_app = Applications.objects.filter(job_id=job_id, user_id=request.user.id).exists()

    return render(request, 'jobs/detail.html',
                  {'job': job, 'likes_count': job_likes_count, 'job_comments': job_comments, "already_exists": exists_app})


def add_action(request, job_likes, job_id):
    if job_likes.filter(user_id=request.user.id, job_id=job_id).exists():
        job_likes.filter(user_id=request.user, job_id=get_object_or_404(Job, pk=job_id)).delete()
    else:
        job_likes.create(user_id=request.user, job_id=get_object_or_404(Job, pk=job_id))


@login_required(login_url="/accounts/login")
def add_like(request, job_id):
    if request.method == 'POST':
        job_likes = Likes.objects.all()
        add_action(request, job_likes, job_id)
        return redirect('/' + str(job_id))


@login_required(login_url="/accounts/login")
def favorites(request):
    pks = Likes.objects.all().filter(user_id=request.user.id)
    pks = [job.job_id for job in pks]
    liked_jobs = Job.objects.filter(title__in=list(pks)).all()
    jobs_count = len(liked_jobs)
    # liked_jobs = Job.objects.filter(pk__in=Likes.objects.filter(user_id=request.user.id))

    return render(request, 'jobs/jobs.html', {'jobs': liked_jobs,
                                              'jobs_count': jobs_count})


def detail_CV(request, CV_id):
    cv = get_object_or_404(CV, pk=CV_id)
    associated_jobs = Job.objects.filter(category=cv.category)

    return render(request, 'jobs/detail_CV.html', {'cv': cv, "jobs": associated_jobs, "jobs_count": associated_jobs.count()})


@login_required(login_url="/accounts/login")
def apply(request, job_id):
    if request.method == 'POST':
        try:
            job_app = Applications.objects.get(job_id=job_id, user_id = request.user)
            return redirect('/' + str(job_id))
        except Applications.DoesNotExist:
            job = Job.objects.get(pk=job_id)
            job_app = Applications.objects.create(job_id=job, user_id = request.user)
            job_app.save()
            return redirect('/' + str(job_id))


@login_required(login_url="/accounts/login")
def admin_dashboard(request):
    jobs = Job.objects.all()
    jobs_apps_dict = {}
    for job in jobs:
        ass_apps = Applications.objects.filter(job_id=job.pk)
        ass_users_idx = [app.user_id for app in ass_apps]
        jobs_apps_dict[job] = CV.objects.filter(user_id__in=ass_users_idx)

    return render(request, 'jobs/admin_dashboard.html', {'jobs_apps_dict': jobs_apps_dict, "jobs_count": len(jobs_apps_dict)})





