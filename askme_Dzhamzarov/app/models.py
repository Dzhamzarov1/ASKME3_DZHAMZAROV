from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


class QuestionManager(models.Manager):
    def get_new(self):
        return self.order_by('-date_created').annotate(
            count_likes=Count('questionlike'),
            count_answer=Count('answer')
        )

    def get_hot(self):
        return self.annotate(
            count_likes=Count('questionlike'),
            count_answer=Count('answer')
        ).order_by('-count_likes')

    def get_tag(self, tag):
        return self.filter(tag__name=tag).annotate(
            count_likes=Count('questionlike'),
            count_answer=Count('answer')
        )

    def get_question(self, question_id):
        return self.filter(pk=question_id).annotate(count_likes=Count('questionlike'))


class AnswerManager(models.Manager):
    def get_quest(self, quest):
        return self.filter(question=quest).annotate(count_likes=Count('answerlike'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)
    data_register = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    STATUS_CORRECT = [
        ('T', 'Correct'),
        ('N', 'NotCorrect')
    ]
    text = models.CharField(max_length=255)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created= models.DateTimeField(auto_now_add=True)
    correct = models.CharField(max_length=10, choices=STATUS_CORRECT)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    objects = AnswerManager()

    def __str__(self):
        return f'{self.user_id.user.username}: {self.text}'


class QuestionLike(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'question')

    def __str__(self):
        return f'{self.user} лайкнул вопрос {self.question}'


class AnswerLike(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('user', 'answer')

  def __str__(self):
    return f'{self.user} лайкнул ответ {self.answer}'