# استخدم نسخة Python الرسمية
FROM python:3.11-slim

# اعمل مجلد للتطبيق
WORKDIR /app

# انسخ ملفات المشروع
COPY . /app

# ثبت الاعتمادات
RUN pip install --no-cache-dir -r requirements.txt

# شغل التطبيق على البورت 5000
CMD ["python", "app.py"]


