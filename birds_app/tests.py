from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.test import Client
from django.test import TestCase
import pytest
from django.urls import reverse
from birds_app.models import Birds, Comments, Wishlist


# Create your tests here.


# Register entry
@pytest.mark.django_db
def test_register_entry():
    client = Client()
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200

# Login entry
@pytest.mark.django_db
def test_login_entry():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200

# Register new member / login
@pytest.mark.django_db
def test_register():
    client = Client()
    url = reverse('register')
    d = {
        'username': 'x',
        'mail': 'a@wp.pl',
        'password1': 'aaa',
        'password2': 'aaa'
    }
    response = client.post(url, d)
    assert response.status_code == 302  # main page
    User.objects.get(username='x') # login x user
    assert client.login(username='x', password='aaa')

# Admin
@pytest.mark.django_db
def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200


# Bird add functionality
@pytest.mark.django_db
def test_add_birds_not_logged():
    client = Client()
    url = reverse('add-bird')
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_check_add_bird_logged(user):
    client = Client()
    client.force_login(user)
    url = reverse('add-bird')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_birds(user):
    client = Client()
    url = reverse('add-bird')
    client.force_login(user)
    d = {
        'name': 'a',
        'description': 'b',
        'population': 1,
        'region': 'c',
        'family': 'd',
    }
    response = client.post(url, d)
    assert response.status_code == 200
    # Birds.objects.get(name='a', description='b', population=1)

# Bird List
@pytest.mark.django_db
def test_bird_list_access():
    client = Client()
    url = reverse('bird-list')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_bird_list_view(birds):
    client = Client()
    url = reverse('bird-list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['birds'].count() == len(birds)
    for bird in birds:
        assert bird in response.context['birds']

# Bird Details
@pytest.mark.django_db
def test_bird_details(birds):
    bird = birds[0]
    client = Client()
    url = reverse('bird-details', args=(bird.id, ))
    response = client.get(url)
    assert response.status_code == 200

# Edit Bird
@pytest.mark.django_db
def test_bird_edit(birds):
    bird = birds[0]
    client = Client()
    url = reverse('edit-bird', args=(bird.id, ))
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_edit_birds_add(birds):
    bird = birds[0]
    client = Client()
    url = reverse('edit-bird', args=(bird.id, ))
    d = {
        'name': 'a',
        'description': 'b',
        'population': 1,
        'region': 'c',
        'family': 'd',
    }
    response = client.post(url, d)
    assert response.status_code == 302
    # Birds.objects.get(name='a'', description='b', population=1')

# Add Comment
@pytest.mark.django_db
def test_add_comment_not_logged(birds):
    bird = birds[0]
    client = Client()
    url = reverse('add-comment', args=(bird.id, ))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_comment(user, birds):
    bird = birds[0]
    client = Client()
    url = reverse('add-comment', args=(bird.id, ))
    client.force_login(user)
    d = {
        'text': 'abcd'
    }
    response = client.post(url, d)
    assert response.status_code == 302
    Comments.objects.get(text='abcd')

# Wishlist
@pytest.mark.django_db
def test_wishlist_not_logged():
    client = Client()
    url = reverse('wish-list')
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_wishlist_entry(user, wishlist):
    client = Client()
    client.force_login(user)
    url = reverse('wish-list')
    response = client.get(url)
    assert response.status_code == 200
    assert Wishlist.objects.first()

@pytest.mark.django_db
def test_wishlist_add_bird(user, wishlist):
    client = Client()
    client.force_login(user)
    url = reverse('wish-list')
    b = {
        'wishlist': wishlist[0].id
    }
    response = client.post(url, b)
    assert response.status_code == 200


# Quiz
@pytest.mark.django_db
def test_quiz(answers):
    client = Client()
    url = reverse('quiz')
    response = client.get(url)
    assert response.status_code == 200



# # Main page carousel
@pytest.mark.django_db
def test_carousel(carousel):
    client = Client()
    url = reverse('main')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['carousel'].count() == len(carousel)


@pytest.mark.django_db
def test_check_index(users, birds, images):
    client = Client()
    url = reverse('main')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['users'].count() == len(users)
    assert response.context['birds'].count() == len(birds)
    assert response.context['images'].count() == len(images)