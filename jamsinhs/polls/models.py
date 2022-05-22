from django.db import models


class Activity(models.Model):
    title = models.CharField(max_length=512, verbose_name='활동명')
    start_date = models.DateTimeField(verbose_name='신청 시작')
    end_date = models.DateTimeField(verbose_name='신청 마감')
    description = models.TextField(verbose_name='내용')
    hour = models.IntegerField(verbose_name='부여하는 수과학 활동 시간')

    class Meta:
        verbose_name = '활동'
        verbose_name_plural = '활동'

    def __str__(self):
        return self.title


class Plan(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    title = models.CharField(max_length=512, verbose_name='내용')
    due_date = models.DateTimeField(verbose_name='날짜/시간')

    class Meta:
        verbose_name = '계획'
        verbose_name_plural = '계획'

    def __str__(self):
        return self.title


class Apply(models.Model):
    APPLY_STATE = (
        (1, '신청'),
        (2, '취소'),
        (3, '승인'),
        (4, '이수')
    )

    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, verbose_name='활동')
    student_id = models.IntegerField(verbose_name='학번')
    name = models.CharField(max_length=512)
    reg_date = models.DateTimeField('date published')
    state = models.IntegerField(choices=APPLY_STATE, default=1)

    class Meta:
        verbose_name = '신청'
        verbose_name_plural = '신청'

    def __str__(self):
        return f'{self.student_id}-{self.name}-{self.activity}'

    def _get_completed_time(self):
        if self.state != 4:
            return 0

        a_list = Additonal_hour.objects.filter(apply=self)
        total_time = self.activity.hour
        for a_hour in a_list:
            total_time = total_time + a_hour.extra_hour
        return total_time

    completed_time = property(_get_completed_time)


class User(models.Model):
    studentid = models.CharField(max_length=64, unique=True, verbose_name='학번')
    name = models.CharField(max_length=10, verbose_name="이름")
    password = models.CharField(max_length=512, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    class Meta:
        verbose_name = '학생'
        verbose_name_plural = '학생'
        db_table = 'test_user'

    def __str__(self):
        return self.studentid

    def get_applylist(self):
        return Apply.objects.filter(student_id=int(self.studentid))

    def _get_completed_time(self):
        a_list = self.get_applylist().filter(state=4)
        total_time = 0
        for apply in a_list:
            total_time = total_time + apply.completed_time
        return total_time

    completed_time = property(_get_completed_time)


class Additonal_hour(models.Model):
    apply = models.ForeignKey(Apply, on_delete=models.CASCADE)
    title = models.CharField(max_length=512, verbose_name='사유')
    extra_hour = models.IntegerField(default=0, verbose_name='추가 시간')

    class Meta:
        verbose_name = '추가 시간'
        verbose_name_plural = '추가 시간'

    def __str__(self):
        return self.title
