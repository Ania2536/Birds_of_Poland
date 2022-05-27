import pytest
from django.contrib.auth.models import User

# Adding fictional users to database
from birds_app.models import Birds, Wishlist, Comments, Images, Carousel, Quiz, Question, Answer


@pytest.fixture
def carousel():
    carousel = []
    for x in range(3):
        c = Carousel.objects.create(image='', title='x', action_name='y')
        carousel.append(c)
    return carousel

@pytest.fixture
def images():
    images = []
    for x in range(3):
        i = Images.objects.create()
        images.append(i)
    return images


@pytest.fixture
def users():
    users = []
    for x in range(10):
        u = User.objects.create(username=x)
        users.append(u)
    return users

@pytest.fixture
def user():
    u = User.objects.create(username='pluto', password='user123')
    return u

# Adding birds to database
@pytest.fixture
def birds(users):
    birds = []
    for user in users:
        for x in range(3):
            b = Birds.objects.create(name='x', description='x', population=5)
            birds.append(b)
    return birds

# Adding birds to wishlist
@pytest.fixture
def wishlist(users, birds):
    birds = birds[0]
    wishlist = []
    for user in users:
            b = Wishlist.objects.create(birds=birds)
            wishlist.append(b)
    return wishlist

# Adding comments
@pytest.fixture
def comment(users):
    comments = []
    for user in users:
        for x in range(3):
            b = Comments.objects.create(birds='x', text='ala ma kota')
            comments.append(b)
    return comments


# Adding quiz
@pytest.fixture
def quiz():
    quiz = Quiz.objects.create(name='Ultimate Bird Quiz', description='Check your knowledge about birds in Poland!')
    return quiz

@pytest.fixture
def questions(quiz):
    questions = []
    for x in range(3):
        x = Question.objects.create(question='x', quiz=quiz)
        questions.append(x)
    return questions

@pytest.fixture
def answers(questions):
    answers = []
    for question in questions:
        for x in range(3):
            if x == 0:
                correct = True
            else:
                correct = False
            x = Answer.objects.create(answer=x, question=question, correct=correct)  # answer == 0 jest poprawne
            answers.append(x)
    return answers