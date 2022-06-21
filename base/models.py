from django.db import models
import datetime
# Create your models here.
class PrimaryCategory(models.Model):
    id = models.CharField(max_length=30, primary_key=True) # 大分類_id
    category_id = models.CharField(max_length=30)
    name = models.TextField() # 產品描述

    class Meta:
        app_label = "carbon_footprint_web"

    def __str__(self):
        return self.name

class IndustrialCategory(models.Model):
    id = models.CharField(max_length=30, primary_key=True) # 細分類_id
    name = models.TextField() # 產品描述
    desc = models.TextField() # 細分類敘述
    primary_category = models.ForeignKey(PrimaryCategory, related_name = "industrial_categories", on_delete = models.CASCADE) # 大分類_id

    class Meta:
        app_label = "carbon_footprint_web"

    def __str__(self):
        return self.name

class AnalyticMethod(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    method = models.TextField() 
    desc = models.TextField() 

    class Meta:
        app_label = "carbon_footprint_web"

    def __str__(self):
        return self.id

class DataQuality(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    desc = models.TextField() 

    class Meta:
        app_label = "carbon_footprint_web"

    def __str__(self):
        return self.id

class Co2Allocation(models.Model):
    pcces_encode = models.CharField(max_length=30, primary_key=True)
    cradle_to_gate  = models.FloatField(null = True) # 搖籃到大門
    factory_gate_to_site = models.FloatField(null = True) # 工廠大門到工地
    total_carbon_footprint = models.FloatField(null = True)
    unit = models.CharField(max_length=30)

    class Meta:
        app_label = "carbon_footprint_web"

    def __str__(self):
        return self.pcces_encode

class PccesEncode(models.Model): 
    pcces_encode = models.CharField(max_length=30, primary_key=True)
    name = models.TextField()
    common_name = models.TextField(null = True)
    chapter = models.TextField()
    six_desc = models.TextField()
    senven_desc = models.CharField(max_length=50)
    eight_desc = models.CharField(max_length=50)
    nine_desc = models.CharField(max_length=50)
    ten_desc = models.CharField(max_length=30)
    eleven_desc = models.CharField(max_length=50, null = True)

    class Meta:
        app_label = "carbon_footprint_web"

    def __str__(self):
        return self.pcces_encode

class Product(models.Model):
    primary_category = models.ForeignKey(PrimaryCategory, null=True, on_delete = models.CASCADE) # 大分類_id
    industrial_category = models.ForeignKey(IndustrialCategory, null=True, on_delete = models.CASCADE) # 細分類_id
    industrial_category_desc = models.TextField() # 細分類敘述
    pcces_encode = models.CharField(primary_key=True, max_length=30) # 編碼
    name = models.TextField()
    image = models.ImageField(upload_to='product_image/') # 產品圖片
    origin = models.CharField(max_length=50) # 製造地點
    technology_desc = models.TextField() # 技術描述
    lifecycle_category = models.CharField(max_length=30) # 生命週期範疇(系統邊界)
    excluded_item = models.CharField(max_length=50) # 排除項目
    co2_allocation = models.ForeignKey(Co2Allocation, null=True, on_delete = models.CASCADE) # 碳足跡數值_id
    lifecycle_analytic_method = models.ForeignKey(AnalyticMethod, null=True, on_delete = models.CASCADE) # 生命週期盤查分析方法
    data_generator = models.CharField(max_length=30, null=True) # 活動數據來源
    emission_coefficient_source = models.CharField(max_length=30) # 排放係數來源
    ISO_standard = models.CharField(max_length=30) # 國際規範
    analysis_time_resource = models.CharField(max_length=30) # 分析時間依據
    valid_time_span = models.CharField(max_length=20) # 盤查起訖日
    data_quality = models.ForeignKey(DataQuality, null=True, on_delete = models.CASCADE) # 數據品質等級
    product_flow_image = models.ImageField(upload_to='product_flow_image/') # 產品製造流程
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