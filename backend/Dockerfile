FROM python:3.8

WORKDIR /app

# 環境変数の設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

# 依存関係のインストール
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# django-cors-headersのインストール
RUN pip install django-cors-headers

# プロジェクトファイルのコピー
COPY . .

# ポートの公開
EXPOSE 8000

# 起動コマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]