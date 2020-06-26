from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            author=self.user,
            title='A good title',
            body='Nice body content'
        )

    def test_string_representation(self) -> None:
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self) -> None:
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self) -> None:
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self) -> None:
        response = self.client.get(reverse('blog:home',))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_post_detail_view(self) -> None:
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'blog/detail.html')

    def test_post_create_view(self) -> None:
        response = self.client.post(reverse('blog:create'), {
            'title': 'New Title',
            'body': 'New text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self) -> None:
        response = self.client.post(reverse('blog:update', args=('1',)), {
            'title': 'Updated title',
            'body': 'Updated body',
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self) -> None:
        response = self.client.post(reverse('blog:delete', args=('1',)),)
        self.assertEqual(response.status_code, 302)
