from django.db import models
import datetime
# Create your models here.
class Product(models.Model):
    primary_category_id = models.CharField(max_length=30) # 大分類_id
    secondary_category_id = models.CharField(max_length=30) # 細分類_id
    secondary_category_desc = models.TextField() # 細分類敘述
    pcces_encode = models.CharField(primary_key = True, max_length=30) # 編碼
    name = models.TextField()
    image = models.TextField() # 產品圖片
    origin = models.CharField(max_length=50) # 製造地點
    product_desc = models.TextField() # 產品描述
    scope = models.CharField(max_length=30) # 產品邊界
    co2_allocation_id = models.CharField(max_length=30) # 碳足跡數值_id
    analytic_method_id = models.CharField(max_length=30) # 生命週期盤查分析方法
    emission_coefficient_source = models.CharField(max_length=30) # 排放係數來源
    ISO_standard = models.CharField(max_length=30) # 國際規範
    analysis_time_resource = models.CharField(max_length=30) # 分析時間依據
    data_level = models.CharField(max_length=10) # 數據品質等級
    product_flow_image = models.TextField() # 產品製造流程
    company_name = models.CharField(max_length=512) # 建置單位名稱
    company_phone = models.CharField(max_length=30) # 建置單位聯絡電話
    company_address = models.TextField() # 建置單位聯絡地址
    company_mail = models.CharField(max_length=50) # 建置單位聯絡信箱
    create_date = models.DateTimeField(null=True, blank=True) # 建置日期
    reviewer_name = models.CharField(max_length=512) # 審查單位
    reviewer_phone = models.CharField(max_length=50) # 審查單位聯絡電話
    reviewer_address = models.TextField() # 審查單位聯絡地址
    reviewer_mail = models.CharField(max_length=50) # 審查單位聯絡信箱
    review_date = models.DateTimeField(null=True, blank=True)# 審查日期
    refresh_time = models.DateTimeField(default=datetime.datetime.now) # 資料更新日期

    class Meta:
        app_label = "carbon_footprint_web"

    def __str__(self):
        return self.name