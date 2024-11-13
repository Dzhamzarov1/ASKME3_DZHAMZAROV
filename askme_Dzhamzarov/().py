# coding: utf-8
quest = Question.objects.get_hot()
quest[0]
quest[0].count_answer
quest[0].count_likes
quest = Question.objects.annotate(likes=Count('questionlike'))
quest
quest[0]]
quest[0]
quest[0].likes
quest = Question.objects.annotate(likes=Count('questionlike')).annotate(answer=Count('answer'))
quest = Question.objects.annotate(likes=Count('questionlike')).annotate(answer=Count('answer'))
quest = Question.objects.annotate(answer=Count('answer'))
quest = Question.objects.annotate(likes=Count('questionlike')).annotate(answer1=Count('answer'))
quest[0]
quest[0].likes
quest[0].answer
quest[0].answer1
quest = Question.objects.annotate(likes=Count('questionlike')).annotate(answer=Count('answer'))
quest = Question.objects.annotate(likes=Count('questionlike')).annotate(answer_count=Count('answer'))
quest = Question.objects.annotate(likes=Count('questionlike'), answer_count=Count('answer'))
quest[0].likes
quest[0].likes quest = Question.objects.annotate(likes=Count('questionlike')).annotate(answer1=Count('answer'))

In [14]: quest[0]
Out[14]: <Question: WHAT???>

In [15]: quest[0].likes
Out[15]: 202
Question.objects.all().delete()
quest = Question.objects.annotate(likes=Count('questionlike'), answer_count=Count('answer'))
quest
quest.save()
quest = Question.objects.all().delete()
quest.save
quest.save()
