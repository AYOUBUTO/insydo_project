__author__ = 'Apolikamixitos'
from insydoapp.api.serializers import LongestStringInputSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from insydoapp.utils import longest_substring

class LongestStringAPIView(APIView):

    """
        Post a list of strings and get the longest substring found

        ex:

            {
                "list_strings": [
                                    "aaa deeddeed cccc rrrrrr",
                                    "aa fhgk deed",
                                    "bbbn rrrrrssddedebt bbboo",
                                    "hello word, bbb"
                                ]
            }


    """
    def post(self, request, format=None):

        serializer = LongestStringInputSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"longest_string": longest_substring(serializer.data['list_strings']) }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
