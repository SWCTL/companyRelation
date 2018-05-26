# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TCorp(models.Model):
    org = models.IntegerField(db_column='ORG', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    seq_id = models.IntegerField(db_column='SEQ_ID')  # Field name made lowercase.
    reg_no = models.CharField(db_column='REG_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    corp_name = models.CharField(db_column='CORP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(db_column='ADDR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    belong_dist_org = models.CharField(db_column='BELONG_DIST_ORG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    belong_trade = models.CharField(db_column='BELONG_TRADE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    econ_kind = models.CharField(db_column='ECON_KIND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admit_main = models.CharField(db_column='ADMIT_MAIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    check_date = models.DateField(db_column='CHECK_DATE', blank=True, null=True)  # Field name made lowercase.
    open_man_ident_no = models.CharField(db_column='OPEN_MAN_IDENT_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    open_man_name = models.CharField(db_column='OPEN_MAN_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    corp_status = models.CharField(db_column='CORP_STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reg_capi = models.FloatField(db_column='REG_CAPI', blank=True, null=True)  # Field name made lowercase.
    fare_team_start = models.DateField(db_column='FARE_TEAM_START', blank=True, null=True)  # Field name made lowercase.
    fare_team_end = models.CharField(db_column='FARE_TEAM_END', max_length=255, blank=True, null=True)  # Field name made lowercase.

    fare_scope = models.TextField(db_column='FARE_SCOPE', blank=True, null=True)  # Field name made lowercase.
    uni_scid = models.CharField(db_column='UNI_SCID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    web_url = models.CharField(db_column='WEB_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prac_person_num = models.IntegerField(db_column='PRAC_PERSON_NUM', blank=True, null=True)  # Field name made lowercase.
    org_inst_code = models.CharField(db_column='ORG_INST_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.

    taxpay_num = models.CharField(db_column='TAXPAY_NUM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    staff_size = models.CharField(db_column='STAFF_SIZE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    english_name = models.CharField(db_column='ENGLISH_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    former_name = models.CharField(db_column='FORMER_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    create_org = models.IntegerField(db_column='CREATE_ORG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_corp'
        unique_together = (('org', 'id', 'seq_id'),)


class TCorpDist(models.Model):
    org = models.IntegerField(db_column='ORG', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    seq_id = models.IntegerField(db_column='SEQ_ID')  # Field name made lowercase.
    dist_reg_no = models.CharField(db_column='DIST_REG_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dist_name = models.CharField(db_column='DIST_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dist_belong_org = models.CharField(db_column='DIST_BELONG_ORG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dist_corp_org = models.IntegerField(db_column='DIST_CORP_ORG', blank=True, null=True)  # Field name made lowercase.
    dist_corp_id = models.IntegerField(db_column='DIST_CORP_ID', blank=True, null=True)  # Field name made lowercase.
    dist_corp_seq_id = models.IntegerField(db_column='DIST_CORP_SEQ_ID', blank=True, null=True)  # Field name made lowercase.
    fare_place = models.CharField(db_column='FARE_PLACE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    oper_man_ident_no = models.CharField(db_column='OPER_MAN_IDENT_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    oper_man_name = models.CharField(db_column='OPER_MAN_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    fare_scope = models.CharField(db_column='FARE_SCOPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    check_date = models.DateField(db_column='CHECK_DATE', blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_corp_dist'
        unique_together = (('org', 'id', 'seq_id'),)


class TCorpPertains(models.Model):
    org = models.IntegerField(db_column='ORG', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    seq_id = models.IntegerField(db_column='SEQ_ID')  # Field name made lowercase.
    certificate_type = models.CharField(db_column='CERTIFICATE_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    person_name = models.CharField(db_column='PERSON_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    person_type = models.CharField(db_column='PERSON_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    certificate_no = models.CharField(db_column='CERTIFICATE_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    select_type = models.CharField(db_column='SELECT_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    holdpost_start = models.DateField(db_column='HOLDPOST_START', blank=True, null=True)  # Field name made lowercase.
    holdpost_edn = models.DateField(db_column='HOLDPOST_EDN', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_corp_pertains'
        unique_together = (('org', 'id', 'seq_id'),)


class TCorpStock(models.Model):
    org = models.IntegerField(db_column='ORG', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    sed_id = models.IntegerField(db_column='SEQ_ID')  # Field name made lowercase.
    stock_type = models.CharField(db_column='STOCK_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    certificate_type = models.CharField(db_column='CERTIFICATE_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    certificate_no = models.CharField(db_column='CERTIFICATE_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stock_name = models.CharField(db_column='STOCK_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stock_capi_type = models.IntegerField(db_column='STOCK_CAPI_TYPE', blank=True, null=True)  # Field name made lowercase.
    stock_capi = models.FloatField(db_column='STOCK_CAPI', blank=True, null=True)  # Field name made lowercase.
    stock_capi_dollar = models.IntegerField(db_column='STOCK_CAPI_DOLLAR', blank=True, null=True)  # Field name made lowercase.
    stock_capi_rmb = models.IntegerField(db_column='STOCK_CAPI_RMB', blank=True, null=True)  # Field name made lowercase.
    stock_percent = models.CharField(db_column='STOCK_PERCENT', max_length=255, blank=True, null=True)  # Field name made lowercase.

    stock_rate_rmb = models.IntegerField(db_column='STOCK_RATE_RMB', blank=True, null=True)  # Field name made lowercase.
    stock_rate_dollar = models.IntegerField(db_column='STOCK_RATE_DOLLAR', blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_corp_stock'
        unique_together = (('org', 'id', 'seq_id'),)


class TMCorpCorpDist(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    seq_id = models.IntegerField(db_column='SEQ_ID')  # Field name made lowercase.
    org = models.IntegerField(db_column='ORG')  # Field name made lowercase.
    sub_org = models.IntegerField(db_column='SUB_ORG')  # Field name made lowercase.
    sub_id = models.IntegerField(db_column='SUB_ID')  # Field name made lowercase.
    sub_seq_id = models.IntegerField(db_column='SUB_SEQ_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_m_corp_corp_dist'
        unique_together = (('id', 'seq_id', 'org', 'sub_org', 'sub_id', 'sub_seq_id'),)


class TMCorpCorpPertains(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    seq_id = models.IntegerField(db_column='SEQ_ID')  # Field name made lowercase.
    org = models.IntegerField(db_column='ORG')  # Field name made lowercase.
    sub_org = models.IntegerField(db_column='SUB_ORG')  # Field name made lowercase.
    sub_id = models.IntegerField(db_column='SUB_ID')  # Field name made lowercase.
    sub_seq_id = models.IntegerField(db_column='SUB_SEQ_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_m_corp_corp_pertains'
        unique_together = (('id', 'seq_id', 'org', 'sub_org', 'sub_id', 'sub_seq_id'),)


class TMCorpCorpStock(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    seq_id = models.IntegerField(db_column='SEQ_ID')  # Field name made lowercase.
    org = models.IntegerField(db_column='ORG')  # Field name made lowercase.
    sub_org = models.IntegerField(db_column='SUB_ORG')  # Field name made lowercase.
    sub_id = models.IntegerField(db_column='SUB_ID')  # Field name made lowercase.
    sub_seq_id = models.IntegerField(db_column='SUB_SEQ_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_m_corp_corp_stock'
        unique_together = (('id', 'seq_id', 'org', 'sub_org', 'sub_id', 'sub_seq_id'),)
