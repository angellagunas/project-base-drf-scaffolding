# -*- coding: utf-8 -*-
from drf_scaffolding.management.core.api import mixins
from drf_scaffolding.management.core.api.viewsets import GenericViewSet

from polls.serializers import poll as serializers
from polls.models import Poll


class PollViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.PartialUpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = serializers.PollSerializer
    list_serializer_class = serializers.PollSerializer
    retrieve_serializer_class = serializers.PollSerializer
    create_serializer_class = serializers.PollSerializer
    update_serializer_class = serializers.PollSerializer

    permission_classes = []  # put your custom permissions here

    def create(self, request, *args, **kwargs):
        """
        Allows create a Poll in project_base_drf_scaffolding.
        ---
        request_serializer: serializers.PollSerializer
        response_serializer: serializers.PollSerializer
        responseMessages:
            - code: 201
                message: CREATED
            - code: 400
                message: BAD REQUEST
            - code: 403
                message: FORBIDDEN
            - code: 500
                message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super(PollViewSet, self).create(
            request, *args, **kwargs
        )

    def list(self, request, *args, **kwargs):
        """
        Returns a list of project_base_drf_scaffolding Poll.
        ---
        response_serializer: serializers.PollSerializer
        responseMessages:
            - code: 200
              message: OK
            - code: 404
              message: NOT FOUND
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super(PollViewSet, self).list(
            request, *args, **kwargs
        )

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves information about a project_base_drf_scaffolding Poll.
        ---
        response_serializer: serializers.PollSerializer
        responseMessages:
            - code: 200
              message: OK
            - code: 403
              message: FORBIDDEN
            - code: 404
              message: NOT FOUND
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super(PollViewSet, self).retrieve(
            request, *args, **kwargs
        )

    def partial_update(self, request, pk=None):
        """
        Updates a Poll.
        ---
        request_serializer: serializers.PollSerializer
        response_serializer: serializers.PollSerializer
        responseMessages:
            - code: 200
              message: OK
            - code: 400
              message: BAD REQUEST
            - code: 403
              message: FORBIDDEN
            - code: 404
              message: NOT FOUND
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super(PollViewSet, self).partial_update(request)

    def destroy(self, request, pk=None):
        """
        Deletes a Poll.
        ---
        responseMessages:
            - code: 204
              message: NO CONTENT
            - code: 400
              message: BAD REQUEST
            - code: 403
              message: FORBIDDEN
            - code: 404
              message: NOT FOUND
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super(PollViewSet, self).destroy(request)

    def get_queryset(self, *args, **kwargs):
        queryset = Poll.objects.all()
        return queryset
