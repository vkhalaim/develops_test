from news.celery import app


from .models import Post


@app.task
def reset_upvote():
    Post.objects.filter(upvotes__gt=0).update(upvotes=0)
