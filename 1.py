import os

fs = FileSystemStorage()

for e in form:
    instance_file = e.instance.file
    file_path = None
    file = e.cleaned_data['file_1']
    
    if e.cleaned_data['DELETE_1'] == False:
        if file:
            if any(x in e.changed_data for x in ['file_1']):
                if instance_file:
                    try:
                        old_file = report_expense.objects.get(pk=e.instance.pk).file
                        if old_file:
                            with fs.open(old_file.name, 'rb') as f:
                                fs.delete(old_file.name)
                    except report_expense.DoesNotExist:
                        pass
                    file_path = fs.save(fs.get_available_name(file.name), file)
                else:
                    file_path = instance_file.name
            else:
                try:
                    old_file = report_expense.objects.get(pk=e.instance.pk).file
                    if old_file:
                        with fs.open(old_file.name, 'rb') as f:
                            fs.delete(old_file.name)
                    old_file.close()
                except report_expense.DoesNotExist:
                    pass

if form.is_valid():
    instance = form.save(commit=False)
    fs = FileSystemStorage()
    for e in form:
        instance_file = e.instance.file
        file = e.cleaned_data['file']
        if 'DELETE' in e.cleaned_data and e.cleaned_data['DELETE'] == False:
            if file:
                if any(x in e.changed_data for x in ['file']):
                    if instance_file:
                        if fs.exists(instance_file.path):
                            fs.delete(instance_file.path)
                        file_path = fs.save(fs.get_available_name(file.name), file)
                    else:
                        file_path = fs.save(fs.get_available_name(file.name), file)
                else:
                    file_path = fs.save(fs.get_available_name(file.name), file)
            else:
                file_path = instance_file.name
        else:
            if instance_file:
                if fs.exists(instance_file.path):
                    instance_file.close()
                    fs.delete(instance_file.path)

if form.is_valid():
    instance = form.save(commit=False)
    fs = FileSystemStorage()
    for e in form:
        instance_file = e.instance.file
        file_path = None
        file = e.cleaned_data['file']
        if e.cleaned_data['DELETE'] == False:
            if file:
                if any(x in e.changed_data for x in ['file']):
                    if instance_file:
                        if fs.exists(instance_file.path):
                            fs.delete(instance_file.path)
                    file_name = fs.get_available_name(file.name)
                    file_path = fs.save(file_name, file)
                else:
                    file_path = instance_file.name
            else:
                file_path = instance_file.name
        else:
            if instance_file:
                if fs.exists(instance_file.path):
                    fs.delete(instance_file.path)
                instance_file.close()
    instance.save()


if form.is_valid():
    instance = form.save(commit=False)
    fs = FileSystemStorage()
    for e in form:
        instance_file = e.instance.file
        file_path = None
        file = e.cleaned_data['file']
        if e.cleaned_data['DELETE'] == False:
            if file:
                if any(x in e.changed_data for x in ['file']):
                    if instance_file:
                        if fs.exists(instance_file.path):
                            fs.delete(instance_file.path)
                    file_path = fs.get_available_name(file.name)
                    file_path = fs.save(file_path, file)
                else:
                    file_path = instance_file.name
            else:
                file_path = instance_file.name
        else:
            if instance_file:
                if fs.exists(instance_file.path):
                    fs.delete(instance_file.path)
                instance_file.close()
    instance.save()


if form.is_valid():
    instance = form.save(commit=False)
    fs = FileSystemStorage()
    for e in form:
        instance_file = e.instance.file
        file_path = None
        file = e.cleaned_data['file']
        if e.cleaned_data['DELETE'] == False:
            if file:
                if any(x in e.changed_data for x in ['file']):
                    if instance_file:
                        if fs.exists(instance_file.path):
                            fs.delete(instance_file.path)
                    file_path = fs.save(fs.get_available_name(file.name), file)
            else:
                file_path = instance_file.name
        else:
            if instance_file:
                if fs.exists(instance_file.path):
                    fs.delete(instance_file.path)
                instance_file.close()
    instance.save()




if form.is_valid():
    instance = form.save(commit=False)
    fs = FileSystemStorage()
    for e in form:
        instance_file = e.instance.file
        file_path = None
        file = e.cleaned_data['file']
        if e.cleaned_data['DELETE'] == False:
            if file:
                if any(x in e.changed_data for x in ['file']):
                    if instance_file:
                        if fs.exists(instance_file.path):
                            fs.delete(instance_file.path)
                    file_path = fs.save(fs.get_available_name(file.name), file)
            else:
                file_path = instance_file.name
        else:
            if instance_file:
                if fs.exists(instance_file.path):
                    fs.delete(instance_file.path)
                instance_file.close()
    instance.save()



if form.is_valid():
    instance = form.save(commit=False)
    del_exp = [p.exp_id for p in form.deleted_objects]
    fs = FileSystemStorage()
    changed_fields = form.changed_data

    for field_name in changed_fields:
        if field_name == 'exp_file':
            exp_file = form.cleaned_data['exp_file']
            if form.cleaned_data['DELETE'] == False:
                if exp_file:
                    if instance.exp_file:
                        if fs.exists(instance.exp_file.path):
                            fs.delete(instance.exp_file.path)
                        file_path = fs.save(fs.get_available_name(exp_file.name), exp_file)
                        instance.exp_file.name = file_path
                    else:
                        file_path = fs.save(fs.get_available_name(exp_file.name), exp_file)
                        instance.exp_file.name = file_path
            else:
                if instance.exp_file:
                    if fs.exists(instance.exp_file.path):
                        instance.exp_file.close()
                        fs.delete(instance.exp_file.path)
                    instance.exp_file = None

    instance.save()

To set initial values for a multi-select field without using Django's ORM, you can use a list or tuple to represent the selected values. Here's an example of how you can set initial values for a multi-select field without using the ORM:

```python
from django.shortcuts import render

def my_view(request):
    initial_values = [1, 3, 5]  # A list of primary keys for selected objects
    options = [(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4'), (5, 'Option 5')]
    context = {'my_field': options, 'selected_values': initial_values}
    return render(request, 'my_template.html', context)
```

In this example, the view sets the initial values of a multi-select field called `my_field`. The initial values are represented as a list of primary keys for the selected objects. The view then manually creates a list of options, and passes it to the template as part of the `context` dictionary. The `selected_values` variable is also passed to the template to indicate which options should be selected.

In the template, you can use a for loop to render the options for the multi-select field, and set the `selected` attribute for the options that match the initial values:

```html
<form>
    <select multiple name="my_field">
        {% for value, label in my_field %}
            <option value="{{ value }}" {% if value in selected_values %}selected{% endif %}>{{ label }}</option>
        {% endfor %}
    </select>
</form>
```

Here, the `for` loop iterates over the list of options, and renders an `<option>` tag for each option. The `value` attribute of the `<option>` tag is set to the value of the option, and the `selected` attribute is set if the value matches one of the initial values.

Note that this example assumes that the options for the multi-select field are fixed and do not change frequently. If the options are dynamic or come from a database, you may need to modify the code to retrieve the options and selected values from the appropriate source. Additionally, you may need to modify the template to match your specific use case.

<row>
  <div class="col-12">This row will be hidden</div>
  <div class="col-12">
    <input type="checkbox">
  </div>
</row>
<row>
  <div class="col-12">This row will be hidden</div>
  <div class="col-12">
    <input type="checkbox">
  </div>
</row>

<script>
  const checkboxes = document.querySelectorAll('input[type="checkbox"]');

  checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('click', function() {
      const row = this.parentNode.parentNode;
      if (this.checked) {
        row.style.display = 'none';
      } else {
        row.style.display = 'block';
      }
    });
  });
</script>

from django.forms.models import inlineformset_factory

def my_view(request):
    MyModelFormSet = inlineformset_factory(MyModel, MyRelatedModel)
    if request.method == 'POST':
        formset = MyModelFormSet(request.POST, instance=my_instance)
        if formset.is_valid():
            # Удаляем объекты, помеченные для удаления
            for form in formset.deleted_forms:
                if not form.instance.pk:
                    # Объект еще не сохранен в базе данных, поэтому нет необходимости его удалять
                    continue
                form.instance.delete()
            formset.save()
            # Редирект на другую страницу, если форма валидна
        else:
            # Если форма не прошла валидацию, удаляем объекты, которые были помечены для удаления, но не прошли валидацию
            for form in formset.forms:
                if form in formset.deleted_forms:
                    continue
                if not form.is_valid():
                    formset.deleted_forms.append(form)
            # Очищаем данные формы, чтобы скрытые строки не отправлялись на сервер
            formset.data = formset.data.copy()
            for form in formset.deleted_forms:
                prefix = formset.add_prefix(form.prefix)
                formset.data[prefix + '-DELETE'] = 'on'
                for field in form.fields:
                    formset.data[prefix + '-' + field] = ''
    else:
        formset = MyModelFormSet(instance=my_instance)
    return render(request, 'my_template.html', {'formset': formset})




from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.forms import inlineformset_factory

def my_view(request):
    MyModelFormSet = inlineformset_factory(MyParentModel, MyModel, fields=('file', 'other_field'), extra=1)
    if request.method == 'POST':
        formset = MyModelFormSet(request.POST, request.FILES, instance=my_parent_model_instance)
        if formset.is_valid():
            # Iterate over the forms in the formset
            for form in formset:
                # Get the cleaned data from the form
                data = form.cleaned_data
                # Get the file from the form
                file = data['file']
                if file:
                    # Generate a unique filename
                    filename = default_storage.get_available_name(file.name)
                    try:
                        # Save the file to the storage backend
                        default_storage.save(filename, ContentFile(file.read()))
                    except FileExistsError:
                        # Handle the case where the file already exists
                        filename = default_storage.get_available_name(file.name)
                        default_storage.save(filename, ContentFile(file.read()))
                    # Create a new model instance with the file path and other fields
                    my_model = form.save(commit=False)
                    my_model.file = filename
                    my_model.save()
            # Return a success message to the user
            return render(request, 'my_template.html', {'success': True})
    else:
        formset = MyModelFormSet(instance=my_parent_model_instance)
    return render(request, 'my_template.html', {'formset': formset})




from django.core.files.storage import FileSystemStorage

# get the formset instance
formset = MyInlineFormSet(request.POST, request.FILES, instance=my_object)

# iterate over each form in the formset
for form in formset:
    # get the instance of the form
    instance = form.instance
    # get the cleaned data of the form
    cleaned_data = form.cleaned_data
    if 'file_field' in cleaned_data and cleaned_data['file_field'] is not None:
        # if the file field is not blank, save the new file to FileSystemStorage
        fs = FileSystemStorage()
        fs.save(instance.file_field.name, cleaned_data['file_field'])
    elif instance.file_field:
        # if the file field is blank and there is an existing file, delete the existing file from FileSystemStorage
        filename = instance.file_field.name
        fs = FileSystemStorage()
        if fs.exists(filename):
            fs.delete(filename)

# call your PostgreSQL function to update the data in the database
# your PostgreSQL function should accept the updated formset data as parameters
from django.core.files.storage import FileSystemStorage

# get the formset instance
formset = MyInlineFormSet(request.POST, request.FILES, instance=my_object)

# iterate over each form in the formset
for form in formset:
    if form.cleaned_data.get('file_field') is None:
        # if the file field is blank, delete the existing file from FileSystemStorage
        filename = form.instance.file_field.name
        fs = FileSystemStorage()
        if fs.exists(filename):
            fs.delete(filename)

# call your PostgreSQL function to update the data in the database
# your PostgreSQL function should accept the updated formset data as parameters

# iterate over each form in the formset again and save the file to FileSystemStorage if the file field is not blank
for form in formset:
    if form.cleaned_data.get('file_field'):
        fs = FileSystemStorage()
        fs.save(form.instance.file_field.name, form.cleaned_data['file_field'])

from django.core.files.storage import FileSystemStorage

def update_form_with_file(request, form, instance):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            uploaded_file = form.cleaned_data['file_field']
            file_instance = form.instance.file_field
            fs = FileSystemStorage()

            if uploaded_file == file_instance.path:
                # file has not changed, do nothing
                file_path = file_instance.path
            elif file_instance:
                # save new file
                if fs.exists(file_instance.path):
                    fs.delete(file_instance.path)
                file_path = fs.save(fs.get_available_name(uploaded_file.name), uploaded_file)
            else:
                # save new file
                file_path = fs.save(fs.get_available_name(uploaded_file.name), uploaded_file)

            # update file instance with new file path
            form.instance.file_field = file_path
            form.save()

    # update form data with new file path
    for field in form:
        if field.name == 'file_field':
            # get file instance for this field
            file_instance = field.instance.file_field

            # update field data with file path from instance
            if file_instance:
                field.data = file_instance.url

    return form
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


CREATE OR REPLACE FUNCTION save_report_and_expenses(
    p_spr_report INTEGER,
    p_accountable_person VARCHAR,
    p_attorney_file BYTEA,
    p_expenses JSON[]
)
RETURNS VOID AS $$
DECLARE
    report_id INTEGER;
BEGIN
    -- Insert the report
    INSERT INTO yourapp_report (spr_report, accountable_person, attorney_file)
    VALUES (p_spr_report, p_accountable_person, p_attorney_file)
    RETURNING id INTO report_id;
    
    -- Insert the expenses
    FOR i IN 1 .. array_length(p_expenses, 1)
    LOOP
        INSERT INTO yourapp_report_expense (number, date, expense_name, sum, spr_currency, file, report_id)
        VALUES (
            p_expenses[i] ->> 'number',
            p_expenses[i] ->> 'date',
            p_expenses[i] ->> 'expense_name',
            p_expenses[i] ->> 'sum',
            p_expenses[i] ->> 'spr_currency',
            p_expenses[i] ->> 'file',
            report_id
        );
    END LOOP;
END;
$$ LANGUAGE plpgsql;
Now, create a Django view that calls this function to save the form data:

python
Copy
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
import json

def save_report_and_expenses(request):
    if request.method == 'POST':
        report_form = ReportGoodsForm(request.POST, request.FILES)
        upload_formset = UploadFileFormset(request.POST, request.FILES, prefix='upload')

        if report_form.is_valid() and upload_formset.is_valid():
            # Prepare the data for the PostgreSQL function
            spr_report = report_form.cleaned_data['spr_report'].id
            accountable_person = report_form.cleaned_data['accountable_person']
            attorney_file = report_form.cleaned_data['attorney_file'].file.read()

            expenses = []
            for form in upload_formset:
                expense = {
                    'number': form.cleaned_data['number'],
                    'date': form.cleaned_data['date'].strftime('%Y-%m-%d'),
                    'expense_name': form.cleaned_data['expense_name'].id,
                    'sum': form.cleaned_data['sum'],
                    'spr_currency': form.cleaned_data['spr_currency'].id,
                    'file': form.cleaned_data['file'].file.read(),
                }
                expenses.append(expense)

            # Call the PostgreSQL function
            with connection.cursor() as cursor:
                cursor.execute("SELECT save_report_and_expenses(%s, %s, %s, %s::json[]);",
                               [spr_report, accountable_person, attorney_file, json.dumps(expenses)])

            return JsonResponse({'success': True})
        else:
            # Handle form errors here
            pass

    return render(request, 'your_template.html', {
        'report_form': ReportGoodsForm(),
        'upload_formset': UploadFileFormset(prefix='upload'),
    })



CREATE OR REPLACE FUNCTION update_yourapp_report_expense(
    p_report_expense_id INTEGER,
    p_number VARCHAR,
    p_date DATE,
    p_expense_name INTEGER,
    p_sum DECIMAL,
    p_spr_currency INTEGER,
    p_file BYTEA,
    p_new_expenses JSON[]
)
RETURNS VOID AS $$
DECLARE
    report_id INTEGER;
    expense_id INTEGER;
BEGIN
    -- Update the existing expense record
    UPDATE yourapp_report_expense
    SET
        number = p_number,
        date = p_date,
        expense_name = p_expense_name,
        sum = p_sum,
        spr_currency = p_spr_currency,
        file = p_file
    WHERE id = p_report_expense_id;

    -- Insert new expenses
    FOR i IN 1 .. array_length(p_new_expenses, 1)
    LOOP
        INSERT INTO yourapp_report_expense (number, date, expense_name, sum, spr_currency, file, report_id)
        VALUES (
            p_new_expenses[i] ->> 'number',
            p_new_expenses[i] ->> 'date',
            p_new_expenses[i] ->> 'expense_name',
            p_new_expenses[i] ->> 'sum',
            p_new_expenses[i] ->> 'spr_currency',
            p_new_expenses[i] ->> 'file',
            report_id
        )
        RETURNING id INTO expense_id;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
This modified function takes in an additional parameter p_new_expenses which is a JSON array of new expenses to be inserted into the yourapp_report_expense table. The function first updates the existing expense record identified by p_report_expense_id using the UPDATE statement. Then, it uses a loop to insert each new expense record into the table using the INSERT statement.

In your Django code, you can modify the update_report_expense function to pass the new expenses as a parameter to the cursor.execute() method. Here is an example:

stylus
Copy
def update_report_expense(request, id):
    if request.method == 'POST':
        form = UpdateReportExpenseForm(request.POST, request.FILES)

        if form.is_valid():
            number = form.cleaned_data['number']
            date = form.cleaned_data['date'].strftime('%Y-%m-%d')
            expense_name = form.cleaned_data['expense_name'].id
            sum = form.cleaned_data['sum']
            spr_currency = form.cleaned_data['spr_currency'].id
            file = form.cleaned_data['file'].file.read()

            new_expenses = []
            for form in upload_formset:
                expense = {
                    'number': form.cleaned_data['number'],
                    'date': form.cleaned_data['date'].strftime('%Y-%m-%d'),
                    'expense_name': form.cleaned_data['expense_name'].id,
                    'sum': form.cleaned_data['sum'],
                    'spr_currency': form.cleaned_data['spr_currency'].id,
                    'file': form.cleaned_data['file'].file.read(),
                }
                new_expenses.append(expense)

            with connection.cursor() as cursor:
                cursor.execute("SELECT update_yourapp_report_expense(%s, %s, %s, %s, %s, %s, %s, %s::json[]);",
                               [id, number, date, expense_name, sum, spr_currency, file, json.dumps(new_expenses)])

            return JsonResponse({'success': True})
        else:
            # Handle form errors here
            pass

    report_expense = YourappReportExpense.objects.get(id=id)
    form = UpdateReportExpenseForm(instance=report_expense)
    upload_formset = UploadFileFormset(prefix='upload')

    return render(request, 'your_template.html', {
        'form': form,
        'upload_formset': upload_formset,
    })
In this modified function, you first extract the new expense data from the inline formset and store it in a JSON array called new_expenses. Then, you pass this array as an additional parameter to the cursor.execute() method when calling the update_yourapp_report_expense function. This way, the function will update the existing expense record and insert the new expense records at the same time.
