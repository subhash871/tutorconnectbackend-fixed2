from rest_framework import serializers
from apps.wishlist.models import Wishlist
from apps.teachers.serializers import TeacherProfileListSerializer


class WishlistSerializer(serializers.ModelSerializer):
    teacher_detail = TeacherProfileListSerializer(source='teacher', read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'student', 'teacher', 'teacher_detail', 'created_at']
        read_only_fields = ['id', 'student', 'created_at']

    def validate(self, attrs):
        request = self.context.get('request')
        if request and request.user:
            attrs['student'] = request.user
        return attrs