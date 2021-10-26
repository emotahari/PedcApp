from django.db import models


# Create your models here.


class Currency(models.Model):
    class Meta:
        verbose_name = 'ارز'
        verbose_name_plural = 'ارز'

    currencyName = models.CharField('نام ارز', max_length=100)
    currencyRate = models.IntegerField("نرخ تبدیل به ریال", default=1)
    yearOfForcast = models.IntegerField(default=1400)

    def __str__(self):
        return self.currencyName

    def __get__(self, instance, owner):
        return self


class Income(models.Model):
    class Meta:
        verbose_name = 'درآمد'
        verbose_name_plural = 'درآمد'

    projectName = models.CharField('نام محصول/خدمت درامدی', max_length=100, null=True)
    realIncomeQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realIncomeQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realIncomeQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realIncomeQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastIncomeQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastIncomeQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastIncomeQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastIncomeQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    isInGroupe = models.BooleanField('درآمد درون گروهی', default=0)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.projectName



class CostType(models.Model):
    class Meta:
        verbose_name = 'نوع هزینه'
        verbose_name_plural = 'نوع هزینه'

    costTypeName = models.CharField('نوع هزینه', max_length=100, null=True)

    def __str__(self):
        return self.costTypeName



class CostOfSales(models.Model):
    class Meta:
        verbose_name = 'قیمت تمام شده'
        verbose_name_plural = 'قیمت تمام شده'

    projectName = models.CharField('نام محصول/خدمت درامدی', max_length=100, null=True)
    realCostQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realCostQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realCostQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realCostQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastCostQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastCostQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastCostQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastCostQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    isInGroupe = models.BooleanField('هزینه درون گروهی', default=0)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)
    costType = models.ForeignKey(CostType, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.projectName


class PublicCostType(models.Model):
    class Meta:
        verbose_name = 'نوع هزینه عمومی، اداری'
        verbose_name_plural = 'نوع هزینه عمومی، اداری'

    publicCostTypeName = models.CharField('نوع هزینه', max_length=100, null=True)

    def __str__(self):
        return self.publicCostTypeName


class PublicCost(models.Model):
    class Meta:
        verbose_name = 'هزینه عمومی، اداری'
        verbose_name_plural = 'هزینه عمومی، اداری'

    subject = models.CharField('موضوع هزینه', max_length=100, null=True)
    realPublicCostQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realPublicCostQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realPublicCostQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realPublicCostQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastPublicCostQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastPublicCostQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastPublicCostQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastPublicCostQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    isInGroupe = models.BooleanField('هزینه درون گروهی', default=0)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)
    publicCostType = models.ForeignKey(PublicCostType, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.subject

class EtcOprationalIncome(models.Model):
    class Meta:
        verbose_name = 'سایر درآمدهای عملیاتی'
        verbose_name_plural = 'سایر درآمدهای عملیاتی'

    etcOprationIncome = models.CharField('موضوع درامدی', max_length=100, null=True)
    realetcOprationIncomeQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realetcOprationIncomeQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realetcOprationIncomeQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realetcOprationIncomeQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastetcOprationIncomeQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastetcOprationIncomeQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastetcOprationIncomeQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastetcOprationIncomeQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    isInGroupe = models.BooleanField('درآمد درون گروهی', default=0)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.etcOprationIncom


class EtcOprationalCost(models.Model):
    class Meta:
        verbose_name = 'سایر هزینه های عملیاتی'
        verbose_name_plural = 'سایر هزینه های عملیاتی'

    subject = models.CharField('موضوع هزینه', max_length=100, null=True)
    realEtcOprationCostQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realEtcOprationCostQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realEtcOprationCostQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realEtcOprationCostQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastEtcOprationCostQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastEtcOprationCostQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastEtcOprationCostQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastEtcOprationCostQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    isInGroupe = models.BooleanField('هزینه درون گروهی', default=0)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.subject

class NonOprationalIncome(models.Model):
    class Meta:
        verbose_name = 'درآمدهای غیر عملیاتی'
        verbose_name_plural = 'درآمدهای غیر عملیاتی'

    nonOprationIncom = models.CharField('موضوع درامدی', max_length=100, null=True)
    realNonOprationIncomeQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realNonOprationIncomeQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realNonOprationIncomeQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realNonOprationIncomeQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastNonOprationIncomeQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastNonOprationIncomeQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastNonOprationIncomeQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastNonOprationIncomeQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    isInGroupe = models.BooleanField('درآمد درون گروهی', default=0)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.NonOprationIncom

class NonOprationalCost(models.Model):
    class Meta:
        verbose_name = 'هزینه های غیر عملیاتی'
        verbose_name_plural = 'هزینه های غیر عملیاتی'

    subject = models.CharField('موضوع هزینه', max_length=100, null=True)
    realNonOprationCostQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realNonOprationCostQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realNonOprationCostQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realNonOprationCostQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastNonOprationCostQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastNonOprationCostQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastNonOprationCostQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastNonOprationCostQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    isInGroupe = models.BooleanField('هزینه درون گروهی', default=0)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.subject


class Tax(models.Model):
    class Meta:
        verbose_name = 'مالیات'
        verbose_name_plural = 'مالیات'

    subject = models.CharField('موضوع مالیات', max_length=100, null=True)
    realTaxQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realTaxQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realTaxQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realTaxQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastTaxQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastTaxQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastTaxQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastTaxQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.subject

class LoanCost(models.Model):
    class Meta:
        verbose_name = 'هزینه مالی'
        verbose_name_plural = 'هزینه مالی'

    subject = models.CharField('موضوع هزینه مالی', max_length=100, null=True)
    realLoanCostQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realLoanCostQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realLoanCostQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realLoanCostQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastLoanCostQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastLoanCostQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastLoanCostQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastLoanCostQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.subject




# #############################      Balance sheet      ################################


class CurrentAssetsType(models.Model):
    class Meta:
        verbose_name = 'نوع دارایی جاری'
        verbose_name_plural = 'نوع دارایی جاری'

    currentAssetName = models.CharField('نام حساب', max_length=100)
    description = models.CharField('توضیحات', max_length=500)
    accountCode = models.IntegerField(default=0)

    def __str__(self):
        return self.currentAssetName

class CurrentAsset(models.Model):
    class Meta:
        verbose_name = 'دارایی جاری'
        verbose_name_plural = 'دارایی جاری'

    currentAssetType = models.ForeignKey('CurrentAssetsType', on_delete=models.PROTECT, default=1)
    realQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    # currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return str(self.id)


class NonCurrentAssetsType(models.Model):
    class Meta:
        verbose_name = 'نوع دارایی غیر جاری'
        verbose_name_plural = 'نوع دارایی غیر جاری'

    nCurrentAssetName = models.CharField('نام حساب', max_length=100)
    description = models.CharField('توضیحات', max_length=500)
    accountCode = models.IntegerField(default=0)

    def __str__(self):
        return self.nCurrentAssetName

class NonCurrentAsset(models.Model):
    class Meta:
        verbose_name = 'دارایی غیر جاری'
        verbose_name_plural = 'دارایی غیر جاری'

    nCurrentAssetType = models.ForeignKey('NonCurrentAssetsType', on_delete=models.PROTECT, default=1)
    realQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    # currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return str(self.id)


class CurrentLiabilitiesType(models.Model):
    class Meta:
        verbose_name = 'نوع بدهی جاری'
        verbose_name_plural = 'نوع بدهی جاری'

    currentLbltName = models.CharField('نام حساب', max_length=100)
    description = models.CharField('توضیحات', max_length=500)
    accountCode = models.IntegerField(default=0)

    def __str__(self):
        return self.currentLbltName

class CurrentLiabilities(models.Model):
    class Meta:
        verbose_name = 'بدهی جاری'
        verbose_name_plural = 'بدهی جاری'

    currentLbltType = models.ForeignKey('CurrentLiabilitiesType', on_delete=models.PROTECT, default=1)
    realQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    # currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return str(self.id)

class NonCurrentLiabilitiesType(models.Model):
    class Meta:
        verbose_name = 'نوع بدهی غیر جاری'
        verbose_name_plural = 'نوع بدهی غیر جاری'

    nCurrentLbltName = models.CharField('نام حساب', max_length=100)
    description = models.CharField('توضیحات', max_length=500)
    accountCode = models.IntegerField(default=0)

    def __str__(self):
        return self.nCurrentLbltName

class NonCurrentLiabilities(models.Model):
    class Meta:
        verbose_name = 'بدهی غیر جاری'
        verbose_name_plural = 'بدهی غیر جاری'

    nCurrentLbltType = models.ForeignKey('NonCurrentLiabilitiesType', on_delete=models.PROTECT, default=1)
    realQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    # currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return str(self.id)



class PropertyRightsType(models.Model):
    class Meta:
        verbose_name = 'نوع حقوق مالکانه'
        verbose_name_plural = 'نوع حقوق مالکانه'

    prprtyRightsName = models.CharField('نام حساب', max_length=100)
    description = models.CharField('توضیحات', max_length=500)
    accountCode = models.IntegerField(default=0)

    def __str__(self):
        return self.prprtyRightsName

class PropertyRights(models.Model):
    class Meta:
        verbose_name = 'حقوق مالکانه'
        verbose_name_plural = 'حقوق مالکانه'

    prprtyRightsType = models.ForeignKey('PropertyRightsType', on_delete=models.PROTECT, default=1)
    realQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    # currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1)
    company = models.ForeignKey('accounts.Company', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return str(self.id)


