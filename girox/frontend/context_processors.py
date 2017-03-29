from django.conf import settings

def context_processor(request):
    my_dict = {
        'site_short_name': settings.SITE_SHORT_NAME,
        'site_name': settings.SITE_NAME,
        'canonical': settings.SITE_CANONICAL,
        'keywords': settings.SITE_KEYWORDS,
        'description': settings.SITE_DESCRIPTION,
        'image': settings.SITE_IMAGE,
        'twitter_site': settings.TWITTER_SITE,
        'twitter_creator': settings.TWITTER_CREATOR,
        'site_fb_app_id': settings.SITE_FB_APP_ID,
    }

    return my_dict