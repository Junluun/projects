Чтобы отправить уведомления в Центр уведомлений Windows без использования сторонних библиотек, можно воспользоваться Windows API через Python, используя модуль ctypes. Этот метод требует немного сложных манипуляций, но теоретически это возможно. Однако важно отметить, что прямой доступ к системным уведомлениям может быть ограничен.

Вот пример кода, который создает уведомление с использованием Windows API через ctypes и win32 функции. В этом примере используется COM-объект для создания уведомления:

import ctypes
import time

class Notification:
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        # Имя класса для уведомлений
        class_name = "Windows.UI.Xaml.Application"
        # Создание объектного запроса
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        notify = ctypes.windll.user32.Shell_NotifyIconW
        # Создаем структуру, представляющую уведомление
        nid = (ctypes.c_ulong * 1)()
        nid[0] = hwnd

        notify(0, nid)

        # Отобразить уведомление
        ctypes.windll.user32.MessageBoxW(0, self.message, self.title, 1)

# Пример использования
notification = Notification("Уведомление", "Это уведомление в Центре уведомлений Windows.")
notification.show()


Однако нужно учитывать, что эта реализация не создает полноценные уведомления в Центре уведомлений Windows 10, а только открывает простое сообщение.

### Рекомендуемый способ
На практике для создания завершенных уведомлений в Windows 10 из Python без использования сторонних библиотек необходимо использовать Windows Runtime API, что значительно усложняет код и требует больше усилий.

Если вы все же хотите полноценные уведомления, то лучшим решением будет использовать библиотеку winrt, которая позволяет работать с Windows API более удобно. Кроме того, для более сложных уведомлений можно рассмотреть возможность использования PowerShell через subprocess, но это также требует дополнительных усилий.

Если вам нужна информация по особенностям Windows API или какие-то конкретные аспекты, дайте знать!

Для того чтобы отправить полноценные уведомления в Центр уведомлений Windows из Python без сторонних библиотек, можно использовать Windows API через ctypes, но это потребует немного более сложного подхода. Давайте рассмотрим код, который будет создавать уведомления в Центре уведомлений Windows. Обратите внимание, что использование ctypes требует знания структуры типов и функций.

Ниже приведён пример создания уведомления с использованием ctypes и API Windows:

### Пример кода
import ctypes
from ctypes import wintypes
import time

# Определяем необходимые структуры и константы
class NOTIFYICONDATA(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.DWORD),
        ("hWnd", wintypes.HWND),
        ("uID", wintypes.UINT),
        ("uFlags", wintypes.UINT),
        ("uCallbackMessage", wintypes.UINT),
        ("hIcon", wintypes.HICON),
        ("szTip", wintypes.WCHAR * 128),
        ("dwState", wintypes.DWORD),
        ("dwStateMask", wintypes.DWORD),
        ("szInfo", wintypes.WCHAR * 256),
        ("uTimeoutOrVersion", wintypes.ULONG),
        ("dwInfoFlags", wintypes.DWORD),
        ("guidItem", wintypes.GUID),
        ("hBalloonIcon", wintypes.HICON),
    ]

# Константы для уведомлений
NIM_ADD = 0x00000000
NIM_MODIFY = 0x00000001
NIM_DELETE = 0x00000002
NIIF_INFO = 0x00000001

# Определяем функцию для уведомлений
def show_notification(title, message):
    nid = NOTIFYICONDATA()
    nid.cbSize = ctypes.sizeof(NOTIFYICONDATA)
    nid.hWnd = 0
    nid.uID = 1
    nid.uFlags = 0x00000001 | 0x00000002 | 0x00000004 | 0x00000010 # NIF_ICON | NIF_MESSAGE | NIF_TIP | NIF_INFO
    nid.hIcon = 0  # Здесь вы можете установить свой значок
    nid.szTip = "Это трюк с уведомлениями"
    nid.szInfo = message
    nid.uTimeoutOrVersion = 10  # время отображения уведомления
    nid.dwInfoFlags = NIIF_INFO  # вид уведомления

    # Получаем дескриптор для системного трея
    hwnd = ctypes.windll.user32.GetConsoleWindow()

    # Вызов функции
    ctypes.windll.shell32.Shell_NotifyIconW(NIM_ADD, ctypes.byref(nid))
    ctypes.windll.shell32.Shell_NotifyIconW(NIM_MODIFY, ctypes.byref(nid))

    # Задержка перед удалением уведомления
    time.sleep(5)

    # Удаляем уведомление
    ctypes.windll.shell32.Shell_NotifyIconW(NIM_DELETE, ctypes.byref(nid))

# Пример использования
show_notification("Уведомление", "Это уведомление в Центре уведомлений Windows.")


### Как это работает
1. Структура NOTIFYICONDATA: Определяет данные для уведомления, включая текст уведомления, его иконку, флаги и т. д.
2. Константы: Определяют различные параметры для уведомлений.
3. Функция show_notification:
   - Заполняет структуру NOTIFYICONDATA с необходимыми данными.
   - Вызывает Shell_NotifyIconW для добавления уведомления.
   - Удаляет уведомление через некоторое время.

### Замечания
- Для успешной работы вам может понадобиться запускать Python скрипт с правами администратора, особенно если он вызывает функции, требующие повышенных привилегий.
- Убедитесь, что вы используете Python версии 3.x, так как код может зависеть от различных особенностей версии.

### Рекомендуемый способ
Хотя вышеизложенный метод работает, для более простого и эффективного способа создания уведомлений рекомендую использовать такие библиотеки, как plyer или winrt, которые значительно упрощают работу с уведомлениями.import
  ComObj, Variants, Dialogs;

procedure ExportGridToODS(Grid: TDBGrid);
var
  ExcelApp: Variant;
  Sheet: Variant;
  i, j: Integer;
  SaveDialog: TSaveDialog;
begin
  SaveDialog := TSaveDialog.Create(nil);
  SaveDialog.Filter := 'ODS files (.ods)|.ods';
  SaveDialog.DefaultExt := 'ods';

  if SaveDialog.Execute then
  begin
    ExcelApp := CreateOleObject('Excel.Application');
    ExcelApp.Visible := False;
  
    ExcelApp.Workbooks.Add;
    Sheet := ExcelApp.Workbooks1.WorkSheets1;
  
    // Write column headers
    for i := 0 to Grid.Columns.Count - 1 do
      Sheet.Cells1, i+1.Value := Grid.Columnsi.Title.Caption;
  
    // Write data from the Grid
    for i := 0 to Grid.DataSource.DataSet.RecordCount - 1 do
    begin
      Grid.DataSource.DataSet.RecNo := i + 1;
    
      for j := 0 to Grid.Columns.Count - 1 do
        Sheet.Cellsi+2, j+1.Value := Grid.Fieldsj.AsString;
    end;
  
    // Save the file
    Sheet.SaveAs(SaveDialog.FileName);
  
    ExcelApp.Quit;
  end;

  SaveDialog.Free;
end;


Usage example:

procedure TForm1.Button1Click(Sender: TObject);
begin
  ExportGridToODS(DBGrid1);
  ShowMessage('Export completed successfully!');
end;

In the modified code, a SaveDialog is added to allow the user to choose the save path and filename. The file is then saved with the .ods extension.

Для выгрузки данных из хранимой процедуры в Excel с использованием компонентов TADODataSet и FastReport, вам понадобится выполнить следующие шаги:

1. Создайте новый проект в среде разработки Delphi.
2. Разместите компонент TADODataSet на форме.
3. Установите соединение с вашей базой данных и настройте компонент TADODataSet для выполнения хранимой процедуры. Для этого задайте свойство CommandText, указывающее имя хранимой процедуры, и укажите необходимые параметры хранимой процедуры, если они есть.
4. Добавьте компонент TDBGrid на форму для отображения результатов из TADODataSet.
5. Создайте кнопку "Выгрузить в Excel" на форме для инициирования процесса выгрузки.
6. Обработайте событие нажатия кнопки "Выгрузить в Excel" и добавьте следующий код:

uses
  frxExportXLS;

procedure TForm1.Button1Click(Sender: TObject);
var
  Report: TfrxReport;
  Export: TfrxXLSExport;
begin
  // Создаем объект отчета FastReport
  Report := TfrxReport.Create(nil);
  try
    // Назначаем источник данных отчета
    Report.DataSets.Add(TfrxDBDataset.Create(Report)).DataSet := ADODataSet1;

    // Создаем экспортер для выгрузки в Excel
    Export := TfrxXLSExport.Create(nil);
    try
      // Устанавливаем параметры экспорта
      Export.FileName := 'путь_к_файлу.xls';
      Export.ShowHeaders := True;
      Export.OpenAfterExport := True;

      // Выполняем экспорт в Excel
      Report.PrepareReport;
      Report.Export(Export);
    finally
      Export.Free;
    end;
  finally
    Report.Free;
  end;
end;


В коде выше создается объект отчета FastReport и назначается источник данных отчета, который связывается с TADODataSet. Затем создается экспортер TfrxXLSExport и устанавливаются параметры для выгрузки в Excel. После этого вызывается метод PrepareReport для подготовки отчета и метод Export для выполнения выгрузки в Excel. Убедитесь, что вы указали правильный путь к файлу в строке Export.FileName := 'путь_к_файлу.xls'.

После выполнения кода, данные из хранимой процедуры будут выгружены в файл Excel по указанному пути. Файл будет автоматически открыт после успешного экспорта.

Надеюсь, эта информация поможет вам решить вашу задачу! Если у вас возникнут еще вопросы, не стесняйтесь задавать их.


Если бы вы хотели экспортировать данные в файл Excel при нажатии кнопки, вы бы добавили процедуру ExportDataSetToExcel в обработчик события OnClick для этой кнопки. Допустим, у вас есть кнопка на форме, которую вы назвали Button1, и датасет, который вы хотите экспортировать, назван DataSet1. Ниже приведён пример, как это сделать:

Во-первых, в основой части вашего модуля объявите процедуру ExportDataSetToExcel:

uses
  ..., frxClass, frxExportXLS;

procedure TForm1.ExportDataSetToExcel(dataset: TDataSet; fileName: string);
var
  report: TfrxReport;
  xlsExport: TfrxXLSExport;
begin
  report := TfrxReport.Create(nil);
  xlsExport := TfrxXLSExport.Create(nil);

  try
    report.DataSets.Add(dataset); // Добавляем датасет в отчет
    report.PrepareReport();

    xlsExport.FileName := fileName;
    xlsExport.OptimizeColumnsWidth := True;

    report.Export(xlsExport);
  finally
    report.Free;
    xlsExport.Free;
  end;
end;


Затем добавьте обработчик события OnClick для вашей кнопки Button1:

procedure TForm1.Button1Click(Sender: TObject);
begin
  // Запускаем экспорт в Excel при клике на кнопку
  // Замените 'output.xlsx' на имя файла, который вам нужен
  ExportDataSetToExcel(DataSet1, 'output.xlsx');
end;


Теперь при каждом нажатии кнопки Button1 выбранный вами набор данных будет экспортироваться в файл Excel.



Чтобы в Django создать возможность загружать несколько файлов с помощью input type="file", вам понадобится использовать JavaScript для динамического добавления новых инпутов при выборе файла. Вот пример, как можно реализовать такую функциональность:

HTML:
<form method="post" enctype="multipart/form-data">
  <div id="fileInputsContainer">
    <input type="file" name="files[]" id="fileInput" multiple>
  </div>
  <button type="button" id="addFileInput">Добавить файл</button>
  <button type="submit">Отправить</button>
</form>


JavaScript:
document.getElementById("addFileInput").addEventListener("click", function() {
  var container = document.getElementById("fileInputsContainer");
  var newInput = document.createElement("input");
  newInput.type = "file";
  newInput.name = "files[]";
  container.appendChild(newInput);
});


В этом примере мы создали форму, включающую контейнер с id="fileInputsContainer", содержащий первый input type="file" с name="files[]" для загрузки файлов.

Затем мы добавили кнопку с id="addFileInput". При нажатии на эту кнопку, с помощью JavaScript создается новый input type="file", и он добавляется в контейнер.

Теперь, каждый раз при нажатии на кнопку "Добавить файл", будет появляться новый input type="file" для загрузки дополнительных файлов.

На сервере вам также понадобится обработать загруженные файлы в соответствии с вашими потребностями. В Django для обработки множественной загрузки файлов, вам может потребоваться использовать форму с FileField или FileField в сочетании с MultiValueField.

Однако помните, что загрузка файлов требует дополнительной обработки на стороне сервера, включая проверку безопасности и обработку загруженных данных. Убедитесь, что вы применяете соответствующие меры безопасности при обработке файлов, чтобы предотвратить возможные атаки.

Надеюсь, это поможет вам создать возможность загружать несколько файлов в Django. Если у вас возникнут дополнительные вопросы, пожалуйста, не стесняйтесь задавать их!


// JavaScript code
document.getElementById('countryDropdown').addEventListener('change', function() {
    var countryId = this.value;
    var regionDropdown = document.getElementById('regionDropdown');
    var regionFstList = regionDropdown.nextElementSibling.lastElementChild.lastElementChild;
    var cityDropdown = document.getElementById('cityDropdown');
    regionDropdown.innerHTML = regionFstList.innerHTML = cityDropdown.innerHTML =
        '<option value="">Выберите регион</option>' +
        '<div data-value="">Выберите регион</option>' +
        '<option value="***">Выберите город</option>';
    console.log(countryId);
    if (countryId) {
        // Fetch regions based on the selected country
        fetch('/get_regions/?country_id=' + countryId)
            .then(response => response.json())
            .then(regions => {
                regions.forEach(function(region) {
                    var option = document.createElement('option');
                    option.value = region.dreg_id;
                    option.text = region.dreg_name;
                    var option1 = document.createElement('div');
                    option1.setAttribute('data-value', region.dreg_id);
                    option1.innerHTML += region.dreg_name;
                    regionDropdown.appendChild(option);
                    regionFstList.appendChild(option1);
                });
            });
    }
});

document.getElementById('regionDropdown').addEventListener('change', function() {
    var regionId = this.value;
    var cityDropdown = document.getElementById('cityDropdown');
    var cityFstList = cityDropdown.nextElementSibling.lastElementChild.lastElementChild;
    cityDropdown.innerHTML = '<option value="">Выберите город</option>';
    if (regionId) {
        // Fetch cities based on the selected region
        fetch('/get_cities/?region_id=' + regionId)
            .then(response => response.json())
            .then(cities => {
                cities.forEach(function(city) {
                    var option = document.createElement('option');
                    option.value = city.deit_id;
                    option.text = city.deit_name;
                    var option1 = document.createElement('div');
                    option1.setAttribute('data-value', city.deit_id);
                    option1.innerHTML += city.deit_name;
                    cityDropdown.appendChild(option);
                    cityFstList.appendChild(option1);
                });
            });
    }
});<select id="countryDropdown" name="country">
    <option value="">Select country</option>
    {% for country in countries %}
        <option value="{{ country.id }}">{{ country.name }}</option>
    {% endfor %}
</select>
<br>

<select id="regionDropdown" name="region">
    <option value="">Select region</option>
</select>
<br>

<select id="cityDropdown" name="city">
    <option value="">Select city</option>
</select>
<br>

<script>
    document.getElementById('countryDropdown').addEventListener('change', function() {
        var countryId = this.value;
        var regionDropdown = document.getElementById('regionDropdown');
        var cityDropdown = document.getElementById('cityDropdown');

        // Reset region and city dropdowns
        regionDropdown.innerHTML = '<option value="">Select region</option>';
        cityDropdown.innerHTML = '<option value="">Select city</option>';

        if (countryId) {
            // Fetch regions based on the selected country
            fetch('/get_regions/?country_id=' + countryId)
                .then(response => response.json())
                .then(regions => {
                    regions.forEach(function(region) {
                        var option = document.createElement('option');
                        option.value = region.id;
                        option.text = region.name;
                        regionDropdown.appendChild(option);
                    });
                });
        }
    });

    document.getElementById('regionDropdown').addEventListener('change', function() {
        var regionId = this.value;
        var cityDropdown = document.getElementById('cityDropdown');

        // Reset city dropdown
        cityDropdown.innerHTML = '<option value="">Select city</option>';

        if (regionId) {
            // Fetch cities based on the selected region
            fetch('/get_cities/?region_id=' + regionId)
                .then(response => response.json())
                .then(cities => {
                    cities.forEach(function(city) {
                        var option = document.createElement('option');
                        option.value = city.id;
                        option.text = city.name;
                        cityDropdown.appendChild(option);
                    });
                });
        }
    });
</script>


from django.http import JsonResponse
from .models import Region, City

def get_regions(request):
    country_id = request.GET.get('country_id')
    regions = Region.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse(list(regions), safe=False)

def get_cities(request):
    region_id = request.GET.get('region_id')
    cities = City.objects.filter(region_id=region_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)

urlpatterns = [
    path('select_location/', select_location, name='select_location'),
    path('get_regions/', get_regions, name='get_regions'),
    path('get_cities/', get_cities, name='get_cities'),
]


<form method="GET" action="{% url 'select_location' %}">
    <select name="country">
        <option value="">Select country</option>
        {% for country in countries %}
            <option value="{{ country.id }}">{{ country.name }}</option>
        {% endfor %}
    </select>
    <br>
    
    {% if regions %}
        <select name="region">
            <option value="">Select region</option>
            {% for region in regions %}
                <option value="{{ region.id }}">{{ region.name }}</option>
            {% endfor %}
        </select>
        <br>
    {% endif %}
    
    {% if cities %}
        <select name="city">
            <option value="">Select city</option>
            {% for city in cities %}
                <option value="{{ city.id }}">{{ city.name }}</option>
            {% endfor %}
        </select>
        <br>
    {% endif %}

    <input type="submit" value="Submit">
</form>



<form method="GET" action="{% url 'select_location' %}">
    <select name="country">
        <option value="">Select country</option>
        {% for country in countries %}
            <option value="{{ country.id }}">{{ country.name }}</option>
        {% endfor %}
    </select>
    <br>
    
    {% if regions %}
        <select name="region">
            <option value="">Select region</option>
            {% for region in regions %}
                <option value="{{ region.id }}">{{ region.name }}</option>
            {% endfor %}
        </select>
        <br>
    {% endif %}
    
    {% if cities %}
        <select name="city">
            <option value="">Select city</option>
            {% for city in cities %}
                <option value="{{ city.id }}">{{ city.name }}</option>
            {% endfor %}
        </select>
        <br>
    {% endif %}

    <input type="submit" value="Submit">
</form>



<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <!-- Поле выбора страны -->
  <select id="countrySelect" name="country">
    <option value="">---------</option>
    {% for country_id, country_name in country_choices %}
      <option value="{{ country_id }}">{{ country_name }}</option>
    {% endfor %}
  </select>
  <!-- Поле выбора региона -->
  <select id="regionSelect" name="region" disabled>
    <option value="">---------</option>
  </select>
  <!-- Поле выбора города -->
  <select id="citySelect" name="city" disabled>
    <option value="">---------</option>
  </select>
  <button type="submit">Submit</button>
</form>

<script>
  // Получение ссылок на элементы формы
  const countrySelect = document.getElementById('countrySelect');
  const regionSelect = document.getElementById('regionSelect');
  const citySelect = document.getElementById('citySelect');

  // Обработчик изменения выбранной страны
  countrySelect.addEventListener('change', function() {
    const countryId = countrySelect.value;
    if (countryId) {
      // Активация поля выбора региона
      regionSelect.disabled = false;
      // Очистка и заполнение списка регионов
      regionSelect.innerHTML = '<option value="">---------</option>';
      const regions = getRegions(countryId);
      for (const region of regions) {
        const option = document.createElement('option');
        option.value = region.id;
        option.textContent = region.name;
        regionSelect.appendChild(option);
      }
      // Очистка и деактивация списка городов
      citySelect.innerHTML = '<option value="">---------</option>';
      citySelect.disabled = true;
    } else {
      // Очистка и деактивация полей выбора региона и города
      regionSelect.innerHTML = '<option value="">---------</option>';
      regionSelect.disabled = true;
      citySelect.innerHTML = '<option value="">---------</option>';
      citySelect.disabled = true;
    }
  });

  // Обработчик изменения выбранного региона
  regionSelect.addEventListener('change', function() {
    const regionId = regionSelect.value;
    if (regionId) {
      // Активация поля выбора города
      citySelect.disabled = false;
      // Очистка и заполнение списка городов
      citySelect.innerHTML = '<option value="">---------</option>';
      const cities = getCities(regionId);
      for (const city of cities) {
        const option = document.createElement('option');
        option.value = city.id;
        option.textContent = city.name;
        citySelect.appendChild(option);
      }
    } else {
      // Очистка и деактивация списка городов
      citySelect.innerHTML = '<option value="">---------</option>';
      citySelect.disabled = true;
    }
  });

  // Функция для получения списка регионов через AJAX
  function getRegions(countryId) {
    // Замените URL на ваше соответствующее представление Django
    const url = `/load_regions/?country_id=${countryId}`;
    // Выполнение AJAX-запроса
    return fetch(url)
      .then(response => response.json())
      .then(data => data.regions)
      .catch(error => {
        console.error('Error:', error);
        return [];
      });
  }

  // Функция для получения списка городов через AJAX
  function getCities(regionId) {
    // Замените URL на ваше соответствующее представление Django
    const url = `/load_cities/?region_id=${regionId}`;
    // Выполнение AJAX-запроса
    return fetch(url)
      .then(response => response.json())
      .then(data => data.cities)
      .catch(error => {
        console.error('Error:', error);
        return [];
      });
  }
</script>



function checkFileExists(fileUrl) {
  var xhr = new XMLHttpRequest();
  xhr.open('HEAD', fileUrl, false);
  xhr.send();

  return xhr.status !== 404;
}

function validateForm() {
  var formset = document.getElementById('your-formset-id');
  var rows = formset.querySelectorAll('.your-formset-row-class');

  for (var i = 0; i < rows.length; i++) {
    var fileInput = rows[i].querySelector('.your-file-input-class');
    var fileUrl = fileInput.value;

    if (fileUrl && !checkFileExists(fileUrl)) {
      // Handle error here (e.g., show an alert message)
      alert('File not found: ' + fileUrl);
      return false; // Prevent form submission
    }
  }

  return true; // Allow form submission
}

function DeleteFile(button) {
  var fileInput = button.parentNode.querySelector('.your-file-input-class');
  fileInput.value = ''; // Clear the file input field
}

function restoreDeletedFile(button) {
  // Do something to restore the deleted file (e.g., show a file picker dialog)
}



import os

def update_formset_with_file(formset):
    fs = FileSystemStorage()
    for form in formset:
        if form.is_valid():
            instance = form.save(commit=False)
            deleted_objects = [p.exp_id for p in form.deleted_objects]
            
            # Check if the file field exists
            if 'exp_file' in form.cleaned_data:
                file = form.cleaned_data['exp_file']
                instance_file = instance.exp_file
                if form.cleaned_data['DELETE'] == False:
                    if file:
                        if any(x in form.changed_data for x in ['exp_file']):
                            if instance_file:
                                try:
                                    old_file = Expense.objects.get(pk=instance.pk).exp_file
                                    if old_file:
                                        fs.delete(old_file.path)
                                except Expense.DoesNotExist:
                                    pass
                                file_path = fs.save(fs.get_available_name(file.name), file)
                            else:
                                file_path = instance_file.name
                    elif instance_file:
                        file_path = instance_file.name
                        
                else:
                    if instance_file:
                        if fs.exists(instance_file.path):
                            instance_file.close()
                            fs.delete(instance_file.path)
                            file_path = None
            instance.save()



To achieve the desired functionality of crossing out the link and showing a "Restore" button on button click, you can update the HTML and add JavaScript code. Here's an example of how you can modify the existing code:

my_template.html:
```html
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ formset.management_form }}
  
  {% for form in formset %}
  {{ form.as_table }}
  
  {% if form.instance.filefield %}
  <a href="{{ form.instance.filefield.value.url }}" target="_blank" class="file-link" id="file-link-{{ form.prefix }}">{{ form.instance.filefield.name }}</a>
  <input type="checkbox" class="delete-checkbox" id="delete-checkbox-{{ form.prefix }}" name="deletefile">
  <button type="button" class="btn restore-btn" id="restore-btn-{{ form.prefix }}" style="display: none" onclick="toggleDeletedFile(this.id)">Restore</button>
  <button type="button" class="btn delete-btn" onclick="toggleDeleteFile(this, '{{ form.prefix }}')">Delete</button>
  {% endif %}
  
  {% endfor %}
  
  <input type="submit" value="Save">
</form>

<script>
  function toggleDeleteFile(buttonElement, formPrefix) {
    const fileLinkElement = document.getElementById('file-link-' + formPrefix);
    const deleteCheckboxElement = document.getElementById('delete-checkbox-' + formPrefix);
    const restoreBtnElement = document.getElementById('restore-btn-' + formPrefix);

if form.is_valid():
    instance = form.save(commit=False)
    fs = FileSystemStorage()
    for e in form:
        file_field = e.cleaned_data.get('file')
        delete_field = e.cleaned_data.get('DELETE')
        if delete_field:
            try:
                old_file = instance.file
                if old_file:
                    fs.delete(old_file.path)
            except ValueError:
                pass
            instance.file = None
        elif file_field:
            if instance.file:
                try:
                    old_file = instance.file
                    fs.delete(old_file.path)
                except ValueError:
                    pass
            instance.file = fs.save(fs.get_available_name(file_field.name), file_field)
    instance.save()


for e in form:
    if e.cleaned_data.get('DELETE') is True:
        if e.instance.file:
            fs.delete(e.instance.file.path)
        continue
        
    file = e.cleaned_data.get('file')
    if file:
        if e.instance.file:
            fs.delete(e.instance.file.path)
        file_path = fs.save(fs.get_available_name(file.name), file)
    elif e.instance.file:
        file_path = e.instance.file.name

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
