شاید به علابق تحصیلیت شک کنی اما این پروژه شک رو از بین میبره با سوالات دقیقی که داره  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-success)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-red?logo=sqlalchemy)
![License](https://img.shields.io/badge/License-MIT-green)


---

# ✨ امکانات پروژه

* ⚡ توسعه API با FastAPI
* 📦 استفاده از SQLAlchemy برای ارتباط با پایگاه داده
* 🔐 احراز هویت با JWT
* 🔒 رمزنگاری رمزهای عبور با bcrypt
* 📄 مستندات خودکار Swagger
* 📚 مستندات ReDoc
* 🔄 راه‌اندازی خودکار پس از تغییر کد (Hot Reload)
* ✅ اعتبارسنجی داده‌ها با Pydantic

---

# 📋 پیش‌نیازها

قبل از اجرا، موارد زیر باید نصب باشند:

* Python 3.10 یا بالاتر
* pip

---

# 📥 نصب پروژه

ابتدا پروژه را دریافت کنید:

```bash
git clone <آدرس-مخزن>
cd <نام-پروژه>
```

سپس یک محیط مجازی ایجاد کنید:

```bash
python -m venv venv
```

فعال‌سازی محیط مجازی

### ویندوز

```bash
venv\Scripts\activate
```

### لینوکس / مک

```bash
source venv/bin/activate
```

نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
```

---

# ▶️ اجرای پروژه

اجرای برنامه:

```bash
python run.py
```

یا به‌صورت مستقیم:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

---

# 🌐 دسترسی به برنامه

پس از اجرای موفق پروژه:

| بخش     | آدرس                        |
| ------- | --------------------------- |
| API     | http://localhost:8001       |
| Swagger | http://localhost:8001/docs  |
| ReDoc   | http://localhost:8001/redoc |

> **توجه:**
> آدرس `http://0.0.0.0:8001` را در مرورگر باز نکنید.
> برای دسترسی از مرورگر از یکی از آدرس‌های زیر استفاده کنید:
>
> * http://localhost:8001
> * http://127.0.0.1:8001


# ⚙️ فایل تنظیمات (.env)

یک فایل با نام `.env` در ریشه پروژه ایجاد کنید.

نمونه:

```env
DATABASE_URL=sqlite:///database.db

SECRET_KEY=یک_کلید_امن

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# 📚 مستندات API

پس از اجرای پروژه می‌توانید مستندات را مشاهده کنید:

### Swagger UI

```
http://localhost:8001/docs
```

### ReDoc

```
http://localhost:8001/redoc
```

---

# 🔧 دستورات کاربردی

نصب کتابخانه‌ها

```bash
pip install -r requirements.txt
```

به‌روزرسانی فایل وابستگی‌ها

```bash
pip freeze > requirements.txt
```

اجرای پروژه

```bash
python run.py
```

---

# 🤝 مشارکت

اگر قصد توسعه پروژه را دارید:

1. پروژه را Fork کنید.
2. یک شاخه (Branch) جدید ایجاد کنید.
3. تغییرات خود را ثبت (Commit) کنید.
4. تغییرات را Push کنید.
5. یک Pull Request ارسال کنید.

---

# 📜 مجوز

این پروژه تحت مجوز **MIT License** منتشر شده است.

---

# ❤️ توسعه داده شده با

* Python
* FastAPI
* SQLAlchemy
* Uvicorn
* Pydantic
* JWT
* bcrypt
