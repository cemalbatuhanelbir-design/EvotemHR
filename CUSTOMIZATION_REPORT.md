# EVOTEM HR Özelleştirme Raporu

## Genel Bakış
Bu rapor, Horilla HRMS projesinin EVOTEM HR olarak yeniden markalaması ve Türkçe dil desteği eklenmesi işlemlerini detaylandırmaktadır.

## Proje Bilgileri
- **Kaynak Proje:** Horilla HRMS (https://github.com/horilla-opensource/horilla.git)
- **Hedef Proje:** EVOTEM HR
- **Proje Dizini:** /home/ubuntu/evotem_hr
- **Tarih:** 27 Kasım 2024

## Yapılan İşlemler

### 1. Türkçe Dil Desteği Ekleme ✅

#### 1.1 Django i18n Yapılandırması
- **settings.py** dosyasında LANGUAGES listesine Türkçe dil desteği eklendi:
  ```python
  ("tr", "Türkçe")
  ```
- Proje zaten i18n için yapılandırılmıştı:
  - `USE_I18N = True` mevcut
  - `LocaleMiddleware` middleware zaten aktif
  - `LOCALE_PATHS` zaten tanımlı

#### 1.2 Türkçe Çeviri Dosyaları Oluşturma
- **Komut:** `python manage.py makemessages -l tr --ignore=venv`
- **Oluşturulan Dizin:** `/home/ubuntu/evotem_hr/horilla/locale/tr/LC_MESSAGES/`
- **Oluşturulan Dosyalar:**
  - `django.po` (880 KB, 25,079 satır)
  - Toplam 3,963 çevrilebilir metin (msgid) tespit edildi

#### 1.3 Türkçe Çeviriler
- **Otomatik Çeviri Scripti:** `translate_po.py` oluşturuldu
- **Çevrilen Terim Sayısı:** 119 temel HR terimi
- **Çeviri Kategorileri:**
  - Temel terimler (Çalışan, Departman, vb.)
  - Devam/Attendance terimleri
  - İzin/Leave terimleri
  - İşe Alım/Recruitment terimleri
  - Bordro/Payroll terimleri
  - Varlık/Asset terimleri
  - Genel eylemler (Ekle, Düzenle, Sil, vb.)
  - Form alanları
  - Mesajlar ve bildirimler
  - Zaman terimleri

#### 1.4 Çeviri Dosyalarını Derleme
- **Komut:** `python manage.py compilemessages --ignore=venv`
- **Oluşturulan Dosya:** `django.mo` (5.0 KB)
- Tüm diller için çeviri dosyaları başarıyla derlendi

### 2. Rebranding (Horilla → EVOTEM HR) ✅

#### 2.1 Değiştirilen Kelime/İfadeler
- `HORILLA` → `EVOTEM_HR` (sabitler, environment değişkenleri)
- `Horilla` → `EVOTEM HR` (görünen metinler, başlıklar)
- `horilla` → `evotem_hr` (URL'ler, tanımlayıcılar - Django module isimleri hariç)

#### 2.2 Etkilenen Dosya Türleri
- Python dosyaları (*.py)
- HTML template dosyaları (*.html)
- JavaScript dosyaları (*.js)
- CSS dosyaları (*.css)
- Markdown dosyaları (*.md)
- JSON dosyaları (*.json)
- YAML/YML dosyaları (*.yml, *.yaml)
- Text dosyaları (*.txt)

#### 2.3 Özel Düzeltmeler
Django proje yapısını korumak için aşağıdaki dosyalarda modül referansları düzeltildi:
- `manage.py`: `horilla.settings` referansı korundu
- `horilla/wsgi.py`: `horilla.settings` referansı korundu
- `horilla/asgi.py`: `horilla.settings` referansı korundu
- `horilla/settings.py`: 
  - `ROOT_URLCONF = "horilla.urls"` korundu
  - `WSGI_APPLICATION = "horilla.wsgi.application"` korundu
  - `LOCALE_PATHS` içinde `horilla` klasör adı korundu
- Tüm Python dosyalarında `from horilla` import'ları korundu
- Django app isimleri korundu:
  - `horilla_automations`
  - `horilla_views`
  - `horilla_widgets`
  - `horilla_audit`
  - `horilla_documents`
  - `horilla_ldap`
  - `horilla_crumbs`
  - `horilla_backup`

#### 2.4 Rebranding İstatistikleri
- **Değiştirilen Dosya Sayısı:** ~409 dosya
- **EVOTEM HR içeren dosya:** 409 dosya tespit edildi

### 3. Sürüm Kontrolü (Git) ✅

#### 3.1 Git Yapılandırması
```bash
git config user.email "evotem_hr@example.com"
git config user.name "EVOTEM HR Team"
```

#### 3.2 Branch Oluşturma
- **Branch Adı:** `feature/turkish-locale-and-rebranding`
- Ana branch'ten ayrıldı ve yeni özellikler bu branch'e commit edildi

#### 3.3 Commit İstatistikleri
```
Commit: Add Turkish locale support and rebrand Horilla to EVOTEM HR
- 349 dosya değiştirildi
- 27,268 satır eklendi
- 1,891 satır silindi
```

#### 3.4 Yeni Oluşturulan Dosyalar
1. `horilla/locale/tr/LC_MESSAGES/django.po` - Türkçe çeviri kaynağı
2. `horilla/locale/tr/LC_MESSAGES/django.mo` - Derlenmiş Türkçe çeviriler
3. `translate_po.py` - Otomatik çeviri scripti
4. `rebrand.sh` - Rebranding scripti
5. `CUSTOMIZATION_REPORT.md` - Bu rapor

## Teknik Detaylar

### Kullanılan Araçlar ve Kütüphaneler
- **Django:** 4.2.23
- **Python:** 3.x
- **gettext:** GNU gettext tools 0.15+
- **Git:** Sürüm kontrolü için

### Oluşturulan Script'ler

#### translate_po.py
- 147 terimlik çeviri sözlüğü
- 3,963 msgid'den 119'unu otomatik çevirdi
- UTF-8 encoding desteği
- Header bilgilerini güncelledi

#### rebrand.sh
- Tüm kaynak dosyaları tarar
- venv, .git, node_modules klasörlerini atlar
- 3 farklı varyasyonu değiştirir (HORILLA, Horilla, horilla)
- Güvenli sed işlemleri kullanır

## Sonraki Adımlar (Öneriler)

### 1. Çeviri Tamamlama
- Kalan 3,844 çevrilmemiş terim için çeviri eklenebilir
- Profesyonel bir çevirmen ile gözden geçirme yapılabilir
- Context-specific çeviriler eklenebilir

### 2. Test Etme
```bash
# Virtual environment'ı aktifleştir
source venv/bin/activate

# Geliştirme sunucusunu başlat
python manage.py runserver

# Tarayıcıda http://localhost:8000 adresine git
# Dil seçeneğinde Türkçe'yi seç ve test et
```

### 3. Logo ve Görsel Değişiklikleri
- EVOTEM HR logosu eklenebilir
- Favicon değiştirilebilir
- Renkler ve tema EVOTEM markasına göre özelleştirilebilir

### 4. Veritabanı Migrasyonları
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Static Dosyaları Toplama
```bash
python manage.py collectstatic --noinput
```

### 6. Production Ayarları
- `DEBUG = False` olarak ayarlanmalı
- `SECRET_KEY` güvenli bir değerle değiştirilmeli
- `ALLOWED_HOSTS` production domain ile güncellenmeli
- Güvenlik ayarları gözden geçirilmeli

## Önemli Notlar

### Django Module Yapısı Korundu ⚠️
- Proje klasör adı hala `horilla` (değiştirilmedi)
- Python import'ları `from horilla` şeklinde devam ediyor
- Bu Django'nun çalışması için kritik öneme sahiptir
- Sadece görünen metinler ve display string'ler değiştirildi

### Çeviri Dosyaları
- `.po` dosyası insan tarafından düzenlenebilir kaynak dosyadır
- `.mo` dosyası derlenmiş binary dosyadır
- Çeviri güncellemelerinden sonra her zaman `compilemessages` çalıştırılmalıdır

### Git Branch Stratejisi
- Ana geliştirme `feature/turkish-locale-and-rebranding` branch'inde
- Test edildikten sonra main branch'e merge edilebilir
- Orijinal Horilla projesinden güncellemeler almak için:
  ```bash
  git remote add upstream https://github.com/horilla-opensource/horilla.git
  git fetch upstream
  git merge upstream/main
  ```

## İletişim ve Destek

Herhangi bir sorun veya soru için:
- **Email:** hr@evotem.com
- **Proje Dizini:** /home/ubuntu/evotem_hr
- **Branch:** feature/turkish-locale-and-rebranding

---

**Rapor Tarihi:** 27 Kasım 2024  
**Oluşturan:** EVOTEM HR Team  
**Durum:** ✅ Tamamlandı
