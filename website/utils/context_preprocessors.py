from main.models import Article

def side_notice_context(request):
    articles=Article.objects.all().filter(notice_type=0)
    return {"articles":articles}