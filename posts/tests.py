from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
from .models import Post

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        #create a user
        testuser1=User.objects.create_user(
            username='testuser1',password='abc123'
        )
        testuser1.save()

        #create blog post
        test_post = Post.objects.create(author=testuser1,title='Blog Title',body='Body content...')
        test_post.save()
    
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_author=f'{post.author}'
        expected_title=f'{post.title}'
        expected_body=f'{post.body}'
        self.assertEquals(expected_author,'testuser1')
        self.assertEquals(expected_title,'Blog Title')
        self.assertEquals(expected_body,'Body content...')
