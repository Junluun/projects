To create a PostgreSQL function that performs an insert on conflict update and delete for your Uploadfileformset, you can use the INSERT ... ON CONFLICT ... DO UPDATE and DELETE statements within a function. Here's an example of how you can achieve this:

CREATE OR REPLACE FUNCTION update_uploadfileformset(
    p_report_id INT,
    p_number INT,
    p_date DATE,
    p_expense_name VARCHAR,
    p_sum DECIMAL,
    p_spr_currency VARCHAR,
    p_file VARCHAR
)
RETURNS VOID AS $$
BEGIN
    -- Insert or update the record
    INSERT INTO report_expense (report_id, number, date, expense_name, sum, spr_currency, file)
    VALUES (p_report_id, p_number, p_date, p_expense_name, p_sum, p_spr_currency, p_file)
    ON CONFLICT (report_id) DO UPDATE
    SET number = EXCLUDED.number,
        date = EXCLUDED.date,
        expense_name = EXCLUDED.expense_name,
        sum = EXCLUDED.sum,
        spr_currency = EXCLUDED.spr_currency,
        file = EXCLUDED.file;
    
    -- Delete the record if necessary
    IF p_number IS NULL THEN
        DELETE FROM report_expense WHERE report_id = p_report_id;
    END IF;
END;
$$ LANGUAGE plpgsql;


In this example, the function update_uploadfileformset takes the necessary parameters (p_report_id, p_number, p_date, p_expense_name, p_sum, p_spr_currency, p_file) to update the report_expense table. It first tries to insert a new record, and if there is a conflict on the report_id column, it performs an update instead. If the p_number parameter is NULL, it deletes the record.

To execute this function in Django, you can use the django.db.connection object to execute raw SQL queries. Here's an example of how you can call the function in Django:

from django.db import connection

def update_uploadfileformset(report_id, number, date, expense_name, sum, spr_currency, file):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT update_uploadfileformset(%s, %s, %s, %s, %s, %s, %s);
            """,
            [report_id, number, date, expense_name, sum, spr_currency, file]
        )


In this example, the update_uploadfileformset function takes the necessary parameters and executes the SQL function using the cursor.execute() method.

You can then call this function in your Django code to update the Uploadfileformset:

update_uploadfileformset(report_id, number, date, expense_name, sum, spr_currency, file)


Make sure to modify the table name, column names, and return type in the PostgreSQL function according to your specific schema.



CREATE OR REPLACE FUNCTION update_uploadfileformset(report_id integer, updated_data json)
RETURNS void AS $$
DECLARE
  record_data json;
  existing_ids integer[];
  new_data json[] := '{}'; -- Initialize new_data as an empty array
BEGIN
  -- Get the IDs of the existing report_expense records
  SELECT array_agg(id) INTO existing_ids FROM report_expense WHERE report_id = report_id;
  
  -- Loop through the updated data and update existing records
  FOR record_data IN SELECT json_array_elements(updated_data)
  LOOP
    IF (record_data->>'id')::integer = 0 THEN
      -- Insert new record if ID is 0
      new_data := array_append(new_data, record_data);
    ELSE
      -- Update existing record
      UPDATE report_expense
      SET
        number = record_data->>'number',
        date = record_data->>'date',
        expense_name = record_data->>'expense_name',
        sum = (record_data->>'sum')::numeric,
        spr_currency = record_data->>'spr_currency',
        file = record_data->>'file'
      WHERE report_id = report_id AND id = (record_data->>'id')::integer;
      
      -- Remove the ID from the existing IDs list
      existing_ids := array_remove(existing_ids, (record_data->>'id')::integer);
    END IF;
  END LOOP;
  
  -- Delete any remaining records that weren't updated
  IF existing_ids IS NOT NULL THEN
    DELETE FROM report_expense WHERE report_id = report_id AND id = ANY(existing_ids);
  END IF;
  
  -- Insert new records
  IF array_length(new_data, 1) > 0 THEN -- Check if new_data array is not empty
    INSERT INTO report_expense (report_id, number, date, expense_name, sum, spr_currency, file)
    SELECT report_id, number, date, expense_name, sum, spr_currency, file FROM json_populate_recordset(null::report_expense, new_data)
    WHERE report_id = report_id;
  END IF;
END;
$$ LANGUAGE plpgsql;

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
CREATE OR REPLACE FUNCTION update_uploadfileformset(report_id integer, updated_data json)
RETURNS void AS $$
DECLARE
  record_data json;
  existing_ids integer[];
  new_data json[];
BEGIN
  -- Get the IDs of the existing report_expense records
  SELECT array_agg(id) INTO existing_ids FROM report_expense WHERE report_id = report_id;
  
  -- Loop through the updated data and update existing records
  FOR record_data IN SELECT json_array_elements(updated_data)
  LOOP
    IF (record_data->>'id')::integer = 0 THEN
      -- Insert new record if ID is 0
      new_data := array_append(new_data, record_data);
    ELSE
      -- Update existing record
      UPDATE report_expense
      SET
        number = record_data->>'number',
        date = record_data->>'date',
        expense_name = record_data->>'expense_name',
        sum = (record_data->>'sum')::numeric,
        spr_currency = record_data->>'spr_currency',
        file = record_data->>'file'
      WHERE report_id = report_id AND id = (record_data->>'id')::integer;
      
      -- Remove the ID from the existing IDs list
      existing_ids := array_remove(existing_ids, (record_data->>'id')::integer);
    END IF;
  END LOOP;
  
  -- Delete any remaining records that weren't updated
  IF existing_ids IS NOT NULL THEN
    DELETE FROM report_expense WHERE report_id = report_id AND id = ANY(existing_ids);
  END IF;
  
  -- Insert new records
  IF new_data IS NOT NULL THEN
    INSERT INTO report_expense (report_id, number, date, expense_name, sum, spr_currency, file)
    SELECT report_id, number, date, expense_name, sum, spr_currency, file FROM json_populate_recordset(null::report_expense, %s)
    WHERE report_id = report_id;
  END IF;
END;
$$ LANGUAGE plpgsql;
