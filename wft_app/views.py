import os
from time import localtime, strftime

from django.shortcuts import render

from wft.settings import BASE_DIR

MAX_UPLOAD_SIZE_MB = 10
MAX_UPLOAD_COUNT = 10


def index(request):
    return render(request, 'index.html')


def browser(request):
    return render(request, 'browser.html')


def element(request):
    return render(request, 'element.html')


def mouse_and_keyboard(request):
    return render(request, 'mouse-and-keyboard.html')


def specific_page(request, level_1_menu, level_2_menu):
    return render(request, 'specific-page.html', {'level_1_menu': level_1_menu, 'level_2_menu': level_2_menu})


def wait(request):
    return render(request, 'wait.html')


def javascript(request):
    return render(request, 'javascript.html')


def upload_and_download(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file is None:
            return render(request, 'upload-and-download.html', {'msg': '上传失败：无待上传的文件！', 'files': _get_files()})
        if int(request.META.get('CONTENT_LENGTH')) > 1024 * 1024 * MAX_UPLOAD_SIZE_MB:
            return render(request, 'upload-and-download.html',
                          {'msg': '上传失败：上传的文件超过了 {} MB！'.format(MAX_UPLOAD_SIZE_MB), 'files': _get_files()})
        path = os.path.join(BASE_DIR, 'upload')
        if not os.path.exists(path):
            os.mkdir(path)
        files = os.listdir(path)
        if len(files) > MAX_UPLOAD_COUNT - 1:
            new_files = sorted(files, key=lambda tmp: os.path.getmtime(os.path.join(path, tmp)))
            for new_file in new_files[:-MAX_UPLOAD_COUNT + 1]:
                os.remove(os.path.join(path, new_file))
        new_file = os.path.join(BASE_DIR, 'upload', file.name)
        with open(new_file, 'wb') as target_file:
            for chunk in file.chunks():
                target_file.write(chunk)
        return render(request, 'upload-and-download.html', {'msg': '上传成功！', 'files': _get_files()})
    else:
        return render(request, 'upload-and-download.html', {'files': _get_files()})


def _get_files():
    path = os.path.join(BASE_DIR, 'upload')
    if not os.path.exists(path):
        os.mkdir(path)
    files = os.listdir(path)
    tmp_files = sorted(files, key=lambda tmp: os.path.getmtime(os.path.join(path, tmp)), reverse=True)
    new_files = []
    for tmp_file in tmp_files:
        modify_time = strftime('%Y-%m-%d %H:%M:%S', localtime(int(os.path.getmtime(os.path.join(path, tmp_file)))))
        new_files.append({'modify_time': modify_time, 'file_name': tmp_file})
    return new_files
