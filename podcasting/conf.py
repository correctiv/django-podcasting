from django.conf import settings  # noqa

from appconf import AppConf


class PodcastingAppConf(AppConf):
    PAGINATE_BY = 10
    FEED_ENTRIES = None
    IMG_PATH = 'podcast_covers'
    THUMBNAIL_ALIASES = {
        'podcasting.Episode.original_image': {
            'itunes_sm': {
                'size': (144, 144)
            },
            'itunes_lg': {
                'size': (1400, 1400)
            }
        },
        'podcasting.Show.original_image': {
            'itunes_sm': {
                'size': (144, 144)
            },
            'itunes_lg': {
                'size': (1400, 1400)
            }
        }
    }
    CATEGORIES = ("Podcast",)
