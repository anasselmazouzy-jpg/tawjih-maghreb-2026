<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>توجيه برو | مستقبلك يبدأ من هنا</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
        
        body {
            font-family: 'Cairo', sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .card {
            background: white;
            width: 90%;
            max-width: 450px;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            text-align: center;
        }

        .logo-img {
            width: 120px;
            height: 120px;
            object-fit: cover;
            border-radius: 50%;
            border: 4px solid #007bff;
            margin-bottom: 1rem;
        }

        h2 { color: #1a1a1a; margin-bottom: 0.5rem; }
        p { color: #666; font-size: 0.9rem; margin-bottom: 1.5rem; }

        .input-group {
            position: relative;
            margin-bottom: 1rem;
        }

        .input-group i {
            position: absolute;
            right: 15px;
            top: 15px;
            color: #007bff;
        }

        input {
            width: 100%;
            padding: 12px 45px 12px 15px;
            border: 2px solid #e1e1e1;
            border-radius: 10px;
            font-size: 1rem;
            box-sizing: border-box;
            transition: 0.3s;
        }

        input:focus {
            border-color: #007bff;
            outline: none;
        }

        .btn {
            background: #007bff;
            color: white;
            border: none;
            padding: 15px;
            width: 100%;
            border-radius: 10px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn:hover { background: #0056b3; }

        .error-msg {
            color: #dc3545;
            font-size: 0.85rem;
            margin-top: -10px;
            margin-bottom: 10px;
            display: none;
            text-align: right;
        }

        /* تنسيق الصور الاحترافي */
        .image-container {
            margin-top: 20px;
            display: flex;
            gap: 10px;
        }

        .image-container img {
            width: 50%;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }
    </style>
</head>
<body>

<div class="card">
    <img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=300" alt="Tawjih Pro" class="logo-img">
    
    <h2>توجيه برو</h2>
    <p>منصة التوجيه التربوي الأولى للتلاميذ</p>

    <div class="input-group">
        <i class="fas fa-envelope"></i>
        <input type="email" id="email" placeholder="أدخل البريد الإلكتروني (Gmail)">
    </div>
    <div id="emailError" class="error-msg">⚠️ يرجى إدخال بريد إلكتروني صحيح (Gmail) للمتابعة.</div>

    <div id="phoneBox" style="display: none;">
        <div class="input-group">
            <i class="fas fa-phone"></i>
            <input type="tel" id="phone" placeholder="أدخل رقم الهاتف">
        </div>
        <div id="phoneError" class="error-msg">⚠️ يرجى إدخال رقم الهاتف قبل المرور.</div>
    </div>

    <button class="btn" onclick="validateAndProceed()">متابعة التسجيل</button>

    <div class="image-container">
        <img src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=200" alt="دراسة">
        <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=200" alt="توجيه">
    </div>
</div>

<script>
    function validateAndProceed() {
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const phoneBox = document.getElementById('phoneBox');
        
        // التحقق من الإيميل (يجب أن يحتوي على @ و .)
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(email)) {
            document.getElementById('emailError').style.display = 'block';
            return;
        } else {
            document.getElementById('emailError').style.display = 'none';
            // إظهار خانة الهاتف بعد التأكد من الإيميل
            phoneBox.style.display = 'block';
        }

        // إذا كانت خانة الهاتف ظاهرة، نتحقق منها
        if (phoneBox.style.display === 'block') {
            if (phone.length < 10) {
                document.getElementById('phoneError').style.display = 'block';
                return;
            } else {
                document.getElementById('phoneError').style.display = 'none';
                alert("تم التحقق بنجاح! جاري توجيهك إلى المنصة...");
                // هنا نضع رابط التوجيه الفعلي
                window.location.href = "https://your-success-page.com"; 
            }
        }
    }
</script>

</body>
</html>
