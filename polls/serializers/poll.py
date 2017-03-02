# -*- coding: utf-8 -*-
from drf_scaffolding.management.core.api.serializers import ModelSerializer

from polls.models import Poll


class PollSerializer(ModelSerializer):

    class Meta:
        model = Poll
        fields = (
            'id',
        )
