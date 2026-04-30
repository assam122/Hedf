from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='.')

# قاعدة بيانات الخدمات
SERVICES = {
    "telegram": {
        "title": "خدمات تيليجرام الاحترافية",
        "icon": "Send",
        "items": [
            {"name": "تيليجرام المميز (Premium)", "desc": "سرعة مضاعفة، رفع ملفات كبرى، تحويل الصوت لنص، وشارة التوثيق.", "order_url": "@B_B_A_W", "details": "https://t.me/H_E_D_F/5237", "icon": "Star"},
            {"name": "نجوم تيليجرام (Stars)", "desc": "العملة الجديدة لدعم الصناع وشراء المنتجات الرقمية والهدايا.", "order_url": "@B_B_A_W", "details": "https://t.me/H_E_D_F/3108", "icon": "Sparkles"},
            {"name": "تعزيز القنوات (Boosts)", "desc": "ارفع مستوى قناتك لنشر الستوري وتخصيص المظهر.", "order_url": "@B_B_A_W", "details": "https://t.me/H_E_D_F/5214", "icon": "Crown"},
            {"name": "سحب الأرباح", "desc": "حول أرباح TON أو النجوم إلى كاش أو USDT بعمولة رمزية.", "order_url": "@B_B_A_W", "details": None, "icon": "Wallet"},
            {"name": "شحن عملة TON", "desc": "توفير عملة تون لمحفظتك لتداول اليوزرات أو الاستثمار.", "order_url": "@B_B_A_W", "details": None, "icon": "CircleDollarSign"}
        ]
    },
    "ai_design": {
        "title": "الذكاء الاصطناعي والتصميم",
        "icon": "Cpu",
        "items": [
            {"name": "ChatGPT Plus", "desc": "الوصول لأحدث نماذج GPT-4o وتحليل البيانات المتقدم.", "order_url": "@B_B_A_W", "details": "https://t.me/H_E_D_F/5212", "icon": "Bot"},
            {"name": "Gemini Premium", "desc": "أقوى ذكاء اصطناعي من جوجل مع سعة تخزين سحابية.", "order_url": "@B_B_A_W", "details": "https://t.me/H_E_D_F/5210", "icon": "BrainCircuit"},
            {"name": "Canva Pro", "desc": "افتح جميع أدوات التصميم والقوالب المدفوعة.", "order_url": "@B_B_A_W", "details": "https://t.me/H_E_D_F/5213", "icon": "Palette"},
            {"name": "Duolingo Plus", "desc": "تعلم اللغات بدون إعلانات وبقلوب غير محدودة.", "order_url": "@B_B_A_W", "details": "https://t.me/H_E_D_F/5214", "icon": "Languages"}
        ]
    },
    "financial": {
        "title": "الخدمات المالية والعامة",
        "icon": "ShieldCheck",
        "items": [
            {"name": "تداول العملات الرقمية", "desc": "بيع وشراء USDT وتوفير التحويلات الدولية.", "order_url": "@B_B_A_W", "details": None, "icon": "Bitcoin"},
            {"name": "أرقام تفعيل الحسابات", "desc": "توفير أرقام لتفعيل تيليجرام وواتساب وحماية خصوصيتك.", "order_url": "@B_B_A_W", "details": None, "icon": "Smartphone"},
            {"name": "توثيق المحافظ (KYC)", "desc": "مساعدة تقنية في إجراءات توثيق الهوية للتطبيقات.", "order_url": "@B_B_A_W", "details": None, "icon": "FileCheck"},
            {"name": "الخدمات الطلابية", "desc": "إعداد أبحاث وتصاميم تعليمية وتوفير المراجع.", "order_url": "@B_B_A_W", "details": None, "icon": "GraduationCap"}
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html', services=SERVICES)

if __name__ == '__main__':
    # بورت 5000 للتشغيل محلياً أو 3000 كما هو معتاد في الاستضافة
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)