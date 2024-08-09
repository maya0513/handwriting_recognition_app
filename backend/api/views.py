from django.shortcuts import render
from django.conf import settings
import os

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from ml_model.model import predict_digit

class PredictDigitView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        image_file = request.data.get('image')
        if not image_file:
            return Response({'error': 'No image provided'}, status=400)

        # 画像を一時的に保存
        path = default_storage.save('tmp/image.png', ContentFile(image_file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        # 予測を実行
        prediction = predict_digit(tmp_file)

        # 一時ファイルを削除
        default_storage.delete(path)

        return Response({'prediction': int(prediction)})