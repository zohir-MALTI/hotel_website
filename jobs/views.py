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

    return render(request, 'jobs/detail.html',
                  {'job': job, 'likes_count': job_likes_count, 'job_comments': job_comments})


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























@login_required(login_url="/accounts/login")
def add_dislike(request, recipe_id):
    if request.method == 'POST':
        recipe_dislikes = Dislikes.objects
        add_action(request, recipe_dislikes, recipe_id)
        return redirect('/' + str(recipe_id))


@login_required(login_url="/accounts/login")
def add_comment(request, recipe_id):
    if request.method == 'POST':
        recipe_comments = Comments.objects
        #add_action(request, recipe_comments, recipe_id)
        recipe_comments.create(user_id=request.user,
                               recipe_id=get_object_or_404(Job, pk=recipe_id),
                               comment=request.POST["comment"])

        return redirect('/' + str(recipe_id))


def search(request):
    if request.method == 'GET':
        keys = request.GET.get("search")
        page_number = request.GET.get("page")
        #jobs = Job.objects.filter(
        #    Q(title__icontains=keys) #| Q(ingredients__icontains=keys)
        #Q(equipments__icontains=keys)
        #)  # filter(search='cheese')  / filter(body_text__search='cheese')
        #jobs = Job.objects.annotate(search=SearchVector('ingredients')).filter(search=keys)
        jobs = Job.objects.annotate(search=SearchVector('ingredients')).filter(search=SearchQuery(keys))
        #jobs = Job.objects.annotate(rank=SearchRank(SearchVector('ingredients'), SearchQuery(keys))).order_by('-rank')
        paginator = Paginator(jobs, 36)
        try:
            jobs_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            jobs_obj = paginator.get_page(1)
        except EmptyPage:
            jobs_obj = paginator.get_page(1)

        return render(request, 'jobs/jobs.html', {'jobs': jobs_obj, 'result_count': len(jobs),
                                                  'query': keys})


