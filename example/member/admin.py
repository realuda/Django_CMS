from django.contrib import admin
from member.models import Member
from member.forms import SetCertificationDateFrom


class MemberAdmin(admin.ModelAdmin):
    actions = ['set_certification_date']
    action_form = SetCertificationDateForm

    def set_certification_date(self, request, queryset):
        year, month, day = . . .

        if year and month and day:
            date_str = '{0}-{1}-{2}'.format(year, month, day)
            date = strptime(date_str, "%Y-%d-%m").date()

            for member in queryset:
                Member.objects.filter(id=member.id).update(is_certificated=True,certification_date=date)
            messages.success(request, '{0}명의 회원을 인증했습니다.'.format(len(queryset)))
        else:
            messages.error(request, '날짜가 선택되지 않았습니다.')
    serticiation_date.short_description = '선택된 유저를 해당 날짜 기준으로 인증합니다.'

    list_per_page = 5
    list_display = ( 'id', 'email', 'username', 'permission', 'is_certificated', 'certification_date', 'post_count', )
    list_editable = ('permission', )
    list_filter = ('permission', )
    search_fields = ('username', )
    ordering = ('-id', 'email', 'permission', )
   
    def post_count(self, obj):
        return Post.objects.filter(member=obj).count()

    post_count.short_description = '작성한 글 수'

admin.site.register(Member, MemberAdmin)

# Register your models here.
