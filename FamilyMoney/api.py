from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import FamilyMember
from .serializers import FamilyMemberSerializer
from django.contrib.auth.models import User


class AddFamilyMemberAPI(APIView):
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        is_family_member = FamilyMember.objects.filter(
            user=request.user, member=user).exists()
        if not is_family_member:
            family_member = FamilyMember.objects.create(
                user=request.user, member=user)
            serializer = FamilyMemberSerializer(family_member)
            return Response(serializer.data, status=201)
        else:
            return Response({'detail': 'Already a family member.'}, status=400)
