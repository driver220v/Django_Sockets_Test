from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UserInfoSerializer(ModelSerializer):
    valid = None

    def is_valid(self, raise_exception=False):
        if self.valid:
            return True

    def validate(self, attrs):
        pass

# check the incoming data. Data from host should follow some standards
class IncomingDataSerializer(serializers.Serializer):

    def validate(self, attrs):
        """
         do something to check if data is correct and follow some standards
        """
        for entry in attrs:
            """
            do something to validate entry
            """
            # raise serializers.ValidationError("finish must occur after start")
        return attrs
