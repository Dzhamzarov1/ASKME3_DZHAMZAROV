from IPython.core.release import author
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from random import randint, choice, sample
from ...models import Profile, Question, Answer, Tag, QuestionLike, AnswerLike, QuestionManager


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Коэффициент заполнения')
    def handle(self, *args, **options):
        ratio = options['ratio']
        for i in range(ratio):
            username = f'user_{i}'
            password = 'password'
            user = User.objects.create_user(username=username, password=password)
            profile = Profile.objects.create(user=user, rating=randint(0, 1000))

        for i in range(ratio):
            name = f'tag {i}'
            tag = Tag.objects.create(name=name)

        users = Profile.objects.all()
        tags = Tag.objects.all()
        for user in users:
            for i in range(10):
                title = f'Title {user} {i}'
                text = f'Text for quest {i}'
                author = user
                tag = tags[i%ratio]
                question = Question.objects.create(
                    title=title,
                    text=text,
                    user=author
                )
                question.tag.add(tag)

        questions = Question.objects.all()
        for quest in questions:
            for i in range(100):
                text = f'for {quest.id}, for {i}'
                author = users[i%ratio]
                answer = Answer.objects.create(
                    text=text,
                    user_id=author,
                    correct='N',
                    question=quest
                )
        answers = Answer.objects.all()
        for user in users:
            for quest in questions:
                QuestionLike.objects.create(user=user, question=quest)
            for answer in answers:
                AnswerLike.objects.create(user=user, answer=answer)