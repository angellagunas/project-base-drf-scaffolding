# -*- coding: utf-8 -*-
from .viewsets import (
    poll,
    question,
)
from api.v1.routers import router


router.register(
    r"polls",
    poll.PollViewSet,
    base_name="polls",
)

router.register(
    r"questions",
    question.QuestionViewSet,
    base_name="questions",
)
