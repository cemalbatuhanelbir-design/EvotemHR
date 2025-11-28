#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to translate common English terms to Turkish in the django.po file
"""

# Common HR/HRMS terms translation dictionary (English -> Turkish)
TRANSLATIONS = {
    # Basic terms
    "Employee": "Çalışan",
    "Employees": "Çalışanlar",
    "Department": "Departman",
    "Departments": "Departmanlar",
    "Job Position": "İş Pozisyonu",
    "Work Type": "Çalışma Tipi",
    "Employee Type": "Çalışan Tipi",
    "Company": "Şirket",
    "Companies": "Şirketler",
    "Manager": "Yönetici",
    "Managers": "Yöneticiler",
    
    # Attendance
    "Attendance": "Devam",
    "Check In": "Giriş",
    "Check Out": "Çıkış",
    "Late": "Geç",
    "Early Out": "Erken Çıkış",
    "Overtime": "Fazla Mesai",
    "Work Record": "Çalışma Kaydı",
    "Validate": "Onayla",
    "Validated": "Onaylandı",
    
    # Leave
    "Leave": "İzin",
    "Leaves": "İzinler",
    "Leave Request": "İzin Talebi",
    "Leave Type": "İzin Tipi",
    "Available Leaves": "Kullanılabilir İzinler",
    "Approve": "Onayla",
    "Approved": "Onaylandı",
    "Reject": "Reddet",
    "Rejected": "Reddedildi",
    "Pending": "Beklemede",
    
    # Recruitment
    "Recruitment": "İşe Alım",
    "Candidate": "Aday",
    "Candidates": "Adaylar",
    "Job Opening": "İş İlanı",
    "Interview": "Görüşme",
    "Application": "Başvuru",
    "Applications": "Başvurular",
    
    # Payroll
    "Payroll": "Bordro",
    "Salary": "Maaş",
    "Salaries": "Maaşlar",
    "Allowance": "Ödeme",
    "Deduction": "Kesinti",
    "Net Pay": "Net Ücret",
    "Gross Pay": "Brüt Ücret",
    
    # Asset
    "Asset": "Varlık",
    "Assets": "Varlıklar",
    "Assign": "Ata",
    "Assigned": "Atandı",
    "Return": "İade",
    "Returned": "İade Edildi",
    
    # Common actions
    "Add": "Ekle",
    "Edit": "Düzenle",
    "Delete": "Sil",
    "Save": "Kaydet",
    "Cancel": "İptal",
    "Submit": "Gönder",
    "Update": "Güncelle",
    "Create": "Oluştur",
    "View": "Görüntüle",
    "Search": "Ara",
    "Filter": "Filtrele",
    "Export": "Dışa Aktar",
    "Import": "İçe Aktar",
    "Download": "İndir",
    "Upload": "Yükle",
    "Print": "Yazdır",
    "Close": "Kapat",
    "Back": "Geri",
    "Next": "İleri",
    "Previous": "Önceki",
    "Select": "Seç",
    "Remove": "Kaldır",
    
    # Form fields
    "Name": "Ad",
    "First Name": "Ad",
    "Last Name": "Soyad",
    "Email": "E-posta",
    "Phone": "Telefon",
    "Mobile": "Cep Telefonu",
    "Address": "Adres",
    "City": "Şehir",
    "State": "Eyalet",
    "Country": "Ülke",
    "Zip Code": "Posta Kodu",
    "Date": "Tarih",
    "Start Date": "Başlangıç Tarihi",
    "End Date": "Bitiş Tarihi",
    "Time": "Zaman",
    "Status": "Durum",
    "Active": "Aktif",
    "Inactive": "Pasif",
    "Description": "Açıklama",
    "Notes": "Notlar",
    "Comments": "Yorumlar",
    "Username": "Kullanıcı Adı",
    "Password": "Şifre",
    
    # Messages
    "Success": "Başarılı",
    "Error": "Hata",
    "Warning": "Uyarı",
    "Info": "Bilgi",
    "Confirmation": "Onay",
    "Please confirm": "Lütfen onaylayın",
    "Are you sure?": "Emin misiniz?",
    "No results found": "Sonuç bulunamadı",
    "Loading": "Yükleniyor",
    "Please wait": "Lütfen bekleyin",
    
    # Dashboard
    "Dashboard": "Panel",
    "Home": "Ana Sayfa",
    "Profile": "Profil",
    "Settings": "Ayarlar",
    "Logout": "Çıkış",
    "Login": "Giriş",
    "Sign In": "Giriş Yap",
    "Sign Out": "Çıkış Yap",
    "Register": "Kayıt Ol",
    
    # Reports
    "Report": "Rapor",
    "Reports": "Raporlar",
    "Generate Report": "Rapor Oluştur",
    "Summary": "Özet",
    "Details": "Detaylar",
    "Statistics": "İstatistikler",
    
    # Time
    "Today": "Bugün",
    "Yesterday": "Dün",
    "Tomorrow": "Yarın",
    "Week": "Hafta",
    "Month": "Ay",
    "Year": "Yıl",
    "Daily": "Günlük",
    "Weekly": "Haftalık",
    "Monthly": "Aylık",
    "Yearly": "Yıllık",
    
    # Permissions
    "Permission": "İzin",
    "Permissions": "İzinler",
    "Access Denied": "Erişim Reddedildi",
    "You dont have access to the feature": "Bu özelliğe erişim izniniz yok",
    "Unauthorized": "Yetkisiz",
    
    # Common phrases
    "All": "Tümü",
    "None": "Hiçbiri",
    "Yes": "Evet",
    "No": "Hayır",
    "Total": "Toplam",
    "Count": "Sayı",
    "Actions": "İşlemler",
    "Options": "Seçenekler",
    "Required": "Gerekli",
    "Optional": "İsteğe Bağlı",
    "Default": "Varsayılan",
    "Custom": "Özel",
}

def translate_po_file(po_file_path):
    """Read and translate the .po file"""
    print(f"Reading file: {po_file_path}")
    
    with open(po_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    translated_count = 0
    total_msgid = 0
    
    # Update header
    for i, line in enumerate(lines):
        if '"Language: \\n"' in line:
            lines[i] = '"Language: tr\\n"\n'
        elif '"Last-Translator:' in line:
            lines[i] = '"Last-Translator: EVOTEM HR Team <hr@evotem.com>\\n"\n'
        elif '"PO-Revision-Date:' in line:
            from datetime import datetime
            now = datetime.now().strftime("%Y-%m-%d %H:%M+0000")
            lines[i] = f'"PO-Revision-Date: {now}\\n"\n'
    
    # Process msgid/msgstr pairs
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Find msgid lines
        if line.startswith('msgid "') and not line.startswith('msgid ""'):
            msgid_value = line[7:-1]  # Extract text between quotes
            total_msgid += 1
            
            # Find corresponding msgstr
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith('msgstr'):
                j += 1
            
            if j < len(lines):
                msgstr_line = lines[j].strip()
                # Check if msgstr is empty
                if msgstr_line == 'msgstr ""':
                    # Look for translation
                    if msgid_value in TRANSLATIONS:
                        lines[j] = f'msgstr "{TRANSLATIONS[msgid_value]}"\n'
                        translated_count += 1
            
        i += 1
    
    # Write back to file
    print(f"Writing translations to file...")
    with open(po_file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"\nTranslation Summary:")
    print(f"Total msgid entries: {total_msgid}")
    print(f"Translated entries: {translated_count}")
    print(f"Translation dictionary size: {len(TRANSLATIONS)}")
    
    return translated_count, total_msgid

if __name__ == "__main__":
    po_file = "/home/ubuntu/evotem_hr/evotem_hr/locale/tr/LC_MESSAGES/django.po"
    translate_po_file(po_file)
