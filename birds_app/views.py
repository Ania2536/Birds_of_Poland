import random
import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.forms import LoginFormView, RegisterFormView
from birds_app.forms import AddBirdForm, AddCommentForm, WishListForm
from birds_app.models import Birds, Family, Images, Comments, Region, Wishlist, Quiz, Question, Answer, Carousel


class MainPage(View):
    def get(self, request):
        # Random Bird of a day
        seed = f'{settings.SECRET_KEY}{datetime.date.today()}'
        random_bird = random.Random(seed).choice(Birds.objects.all())
        # Search engine
        name = request.GET.get('search', '')
        birds = Birds.objects.filter(name__icontains=name)
        # statistics
        birds_number = len(Birds.objects.all())
        users_number = len(User.objects.all())
        image_number = len(Images.objects.all())
        # carousel
        carousel = Carousel.objects.all()
        return render(request, 'main.html', {'birds': birds, 'random_bird': random_bird, 'birds_number': birds_number, 'users_number': users_number, 'image_number': image_number, 'carousel': carousel})

class AddBird(LoginRequiredMixin, View):
    def get(self, request):
        form = AddBirdForm()
        return render(request, 'add_bird.html', {'form': form})
    def post(self, request):
        form = AddBirdForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            population = form.cleaned_data['population']
            family, created = Family.objects.get_or_create(name=form.cleaned_data['family'])
            region = form.cleaned_data['region']
            bird = Birds.objects.create(name=name, description=description, population=population, family=family)
            bird.region.set(region)
            return redirect('main')
        return render(request, 'add_bird.html', {'form': form})

class BirdList(View):
    def get(self, request):
        birds = Birds.objects.all().order_by('name')
        return render(request, 'bird_list.html', {'birds': birds})

class BirdDetails(View):
    def get(self, request, id):
        bird = Birds.objects.get(pk=id)
        comments = bird.comments_set.filter(approve=True)
        return render(request, 'bird-details.html', {'bird': bird, 'comments': comments})

class EditBirdDetails(LoginRequiredMixin, View):
    def get(self, request, id):
        bird = Birds.objects.get(pk=id)
        comments = bird.comments_set.all()
        form = AddBirdForm(instance=bird)
        return render(request, 'bird-details.html', {'bird': bird, 'comments': comments, 'form': form})
    def post(self, request, id):
        bird = Birds.objects.get(pk=id)
        comments = bird.comments_set.all()
        form = AddBirdForm(request.POST, instance=bird)
        if form.is_valid():
            family, created = Family.objects.get_or_create(name=form.cleaned_data['family'])
            bird = form.save(commit=False)
            bird.family = family
            bird.save()
            return redirect(f'/birds_app/bird/{bird.id}/')
        return render(request, 'bird-details.html', {'bird': bird, 'comments': comments})


class AddCommentsView(LoginRequiredMixin, View):
    def get(self, request, id):
        bird = Birds.objects.get(pk=id)
        form = AddCommentForm()
        return render(request, 'bird-details.html', {'form': form, 'bird': bird})
    def post(self, request, id):
        bird = Birds.objects.get(pk=id)
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.birds = bird
            comment.save()
            return redirect(f'/birds_app/bird/{bird.id}')
        return render(request, 'bird-details.html', {'form': form})

class AddBirdToWishlist(LoginRequiredMixin, View):
    def get(self, request):
        form = WishListForm(request.user)
        return render(request, 'wish_list.html', {'form': form})
    def post(self, request):
        form = WishListForm(request.user, request.POST)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.user = request.user
            wishlist.save()
            return redirect('wish-list')
        return render(request, 'wish_list.html', {'form': form})


class ButtonWishlist(LoginRequiredMixin, View):
    def get(self, request, id):
        bird = Birds.objects.get(pk=id)
        return render(request, 'bird-details.html', {'bird': bird})
    def post(self, request, id):
        bird = Birds.objects.get(pk=id)
        form = WishListForm(request.POST)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.user = request.user
            wishlist.save()
            return redirect('wish-list')
        return render(request, 'wish_list.html', {'form': form})


class QuizView(View):
    def get(self, request):
        quiz = Quiz.objects.get(name='Ultimate Bird Quiz')
        questions = quiz.question_set.all()
        return render(request, 'quiz.html', {'quiz': quiz, 'questions': questions})

    def post(self, request):
        quiz = Quiz.objects.get(name='Ultimate Bird Quiz')
        questions = quiz.question_set.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            answer_id = int(request.POST.get(str(q.id), 0))
            correct_answer = q.answer_set.get(correct=True)
            if correct_answer.id == answer_id:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        ctx = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quiz_results.html', ctx)




# class QuizView(View):
#     def get(self, request):
#         questions = Quiz.objects.all()
#         return render(request, 'quiz.html', {'questions': questions})
#     def post(self, request):
#         questions = Quiz.objects.all()
#         score = 0
#         wrong = 0
#         correct = 0
#         total = 0
#         for q in questions:
#             total += 1
#             print(request.POST.get(q.question))
#             print(q.answer)
#             print()
#             if q.answer == request.POST.get(q.question):
#                 score += 10
#                 correct += 1
#             else:
#                 wrong += 1
#             percent = score / (total * 10) * 100
#         ctx = {
#             'score': score,
#             'correct': correct,
#             'wrong': wrong,
#             'percent': percent,
#             'total': total
#         }
#         return render(request, 'quiz_results.html', ctx)


