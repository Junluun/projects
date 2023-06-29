'''
To overwrite the save method with a raw SQL query in your Django app, you can follow these steps:

First, import the necessary libraries in your views.py:
'''
from django.db import connection
from django.shortcuts import render, redirect
Create a function to execute raw SQL queries:
python
Copy
def execute_raw_query(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        return cursor.rowcount
 '''       
Modify your create function to use the execute_raw_query function when saving the main form and inline formset instances:
python
Copy
'''
def create(request):
    if request.method == 'POST':
        form = YourMainForm(request.POST)
        inline_formset = YourInlineFormSet(request.POST, prefix='inline_formset')

        if form.is_valid() and inline_formset.is_valid():
            main_form_data = form.cleaned_data

            # Save the main form using raw SQL query
            main_form_query = '''
                INSERT INTO your_main_model_table (field1, field2, field3)
                VALUES (%s, %s, %s)
            '''
            main_form_params = (main_form_data['field1'], main_form_data['field2'], main_form_data['field3'])
            execute_raw_query(main_form_query, main_form_params)

            # Get the latest inserted ID for foreign key referencing
            with connection.cursor() as cursor:
                cursor.execute("SELECT LAST_INSERT_ID()")
                main_form_id = cursor.fetchone()[0]

            # Save the inline formset instances using raw SQL query
            for inline_form in inline_formset:
                inline_form_data = inline_form.cleaned_data
                inline_form_query = '''
                    INSERT INTO your_inline_model_table (foreign_key_field, field1, field2)
                    VALUES (%s, %s, %s)
                '''
                inline_form_params = (main_form_id, inline_form_data['field1'], inline_form_data['field2'])
                execute_raw_query(inline_form_query, inline_form_params)

            return redirect('your_success_view')
        else:
            # Handle the case when the form or formset is not valid
            pass

    else:
        form = YourMainForm()
        inline_formset = YourInlineFormSet(prefix='inline_formset')

    return render(request, 'your_template.html', {'form': form, 'inline_formset': inline_formset})


'''

Yes, you can modify the PostgreSQL function to accept the inline formset data as a list of tuples instead of a JSON object. Here's an updated version of the function that accepts a list of tuples:

'''
CREATE OR REPLACE FUNCTION save_main_form_and_inline_formset(
    field1_value TEXT,
    field2_value TEXT,
    field3_value TEXT,
    inline_formset_data TEXT[]
) RETURNS VOID AS $$
DECLARE
    main_form_id INTEGER;
BEGIN
    -- Save the main form instance to the database
    INSERT INTO your_main_model_table (field1, field2, field3)
    VALUES (field1_value, field2_value, field3_value)
    RETURNING id INTO main_form_id;

    -- Save the inline formset instances to the database
    FOREACH inline_formset_row IN ARRAY inline_formset_data LOOP
        INSERT INTO your_inline_model_table (foreign_key_field, field1, field2)
        VALUES (main_form_id, inline_formset_row[1], inline_formset_row[2]);
    END LOOP;
END;
$$ LANGUAGE plpgsql;
In this version of the function, we define inline_formset_data as a TEXT[] array, and we use a FOREACH loop to iterate through each row in the array. Each row is a tuple of two values that correspond to the field1 and field2 values of the inline formset.

To call this function from your Django app, you can modify the create view to pass the inline formset data as a list of tuples. Here's an example of how you can modify the create view:


def create(request):
    if request.method == 'POST':
        form = YourMainForm(request.POST)
        inline_formset = YourInlineFormSet(request.POST, prefix='inline_formset')

        if form.is_valid() and inline_formset.is_valid():
            main_form_data = form.cleaned_data
            inline_formset_data = [(f.cleaned_data['field1'], f.cleaned_data['field2']) for f in inline_formset.forms]

            # Call the PostgreSQL function to save the main form and inline formset
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT save_main_form_and_inline_formset(%s, %s, %s, %s)',
                    [main_form_data['field1'], main_form_data['field2'], main_form_data['field3'], inline_formset_data]
                )

            return redirect('your_success_view')
        else:
            # Handle the case when the form or formset is not valid
            pass

    else:
        form = YourMainForm()
        inline_formset = YourInlineFormSet(prefix='inline_formset')

    return render(request, 'your_template.html', {'form': form, 'inline_formset': inline_formset})
    from django.views.generic.edit import CreateView
from django.db import connection, transaction
from .models import Report, Report_status
from .forms import ReportForm, UploadFileFormset
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

class ReportCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('reports')
    template_name = 'report_create.html'

    def test_func(self):
        return (self.request.user.current_user.group.name == 'Сотрудник' or
                self.request.user.current_user.group.name == 'Секретарь')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['order_number'] = self.kwargs['pk_trip']
        if self.request.POST:
            data['reports'] = UploadFileFormset(self.request.POST, self.request.FILES)
        else:
            data['reports'] = UploadFileFormset()
        return data

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.order_number_id = self.kwargs['pk_trip']
        reports = self.get_context_data()['reports']
        with transaction.atomic():
            if reports.is_valid() and form.is_valid():
                if 'draft' in self.request.POST:
                    report_status = Report_status.objects.get(name='Черновик')
                else:
                    report_status = Report_status.objects.get(name='На согласовании у руководителя')

                cursor = connection.cursor()
                cursor.execute(
                    'SELECT save_report_with_files(%s, %s, %s, %s, %s, %s);',
                    [form.instance.report_date, form.instance.report_name, form.instance.report_text,
                     report_status.id, self.request.user.id, self.request.user.current_user.group.id]
                )
                report_id = cursor.fetchone()[0]

                # Loop through the formset data and call the PostgreSQL function to save each child record
                for report in reports:
                    if report.cleaned_data:
                        cursor.execute(
                            'SELECT save_report_file(%s, %s);',
                            [report.cleaned_data['file_field'], report_id]
                        )

                        cursor.execute(
                            'SELECT save_report_status_history(%s, %s, %s, %s, %s);',
                            [timezone.now(), report_id, report_status.id, self.request.user.id, self.request.user.current_user.group.id]
                        )

                messages.success(self.request, 'Запись сохранена')
                return super().form_valid(form)
            else:
                return self.render_to_response(self.get_context_data(form=form, reports=reports))
