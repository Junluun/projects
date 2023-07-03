Чтобы объединить две функции в одну, вы можете сначала создать общий базовый класс формы, затем создать две подклассы для каждой из форм, и в итоге создать одну функцию представления для обработки обеих форм. Вот как это можно сделать:

Создайте общий базовый класс формы:
python
Copy
class BaseReportForm(forms.ModelForm):
    class Meta:
        model = models.Report
        fields = ('spr_report', 'attorney_file')
Создайте подклассы для каждой из форм:
python
Copy
class ReportGoodsForm(BaseReportForm):
    class Meta(BaseReportForm.Meta):
        fields = BaseReportForm.Meta.fields + ('accountable_person',)

class ReportForm(BaseReportForm):
    class Meta(BaseReportForm.Meta):
        fields = BaseReportForm.Meta.fields + ('order_number',)
Создайте одну функцию представления для обработки обеих форм:
python
Copy
def report_create(request, report_type):
    group = request.user.current_user.group.name
    user = request.user

    if report_type == 'goods':
        queryset = Users.objects.raw(
            'SELECT * FROM xv.xv26p_lk_userselect(%s,%s,%s)',
            [group, user.user.id, user.user.division]
        )
        FormClass = ReportGoodsForm
    elif report_type == 'trip':
        queryset = WC07P.objects.raw(
            'SELECT * FROM xv.xv26p_1k_wc07p_select_report_form(%s,%s,%s,%s)',
            [group, user.user.id, user.user.division, user.id]
        )
        FormClass = ReportForm
    else:
        raise ValueError(f"Unknown report type: {report_type}")

    form = FormClass(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            main_form_data = form.cleaned_data
            group = request.user.current_user.group.id
            order_number = main_form_data.get('order_number', None)
            with connection.cursor() as c:
                c.execute('SELECT * FROM xv.xv26p_lk_report_create(%s, %s, %s, %s, %s)',
                          [main_form_data.get('accountable_person', None).id, order_number,
                           main_form_data['attorney_file'], user.id, group])
                report_id = c.fetchone()[0]
                messages.success(request, ("Запись сохранена"))
                return redirect(reverse('show_rep', args=[report_id]))

    return render(request, "XV26P_LK/report_form.html", {
        'form': form,
        'queryset': queryset,
    })
