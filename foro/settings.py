# -*- coding: utf-8 -*-
from django.conf import settings

PUBLIC = 'PUB'
PRIVATE = 'PRI'

DEFAULT_VISIBILITY = (
    (PUBLIC, 'Pública'),
    (PRIVATE, 'Privada')
)

VISIBILITY = getattr(settings, 'VISIBILITY', DEFAULT_VISIBILITY)
