# dj_vditor

**Django-vditor** 是基于 [vditor v3.8.0](https://github.com/Vanessa219/vditor) 的一个 [django](djangoproject.com) Markdown 文本编辑插件应用。

**Django-mdeditor** 的灵感参考自伟大的项目 [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor).

## Installation

```bash
pip install dj-vditor-widget

```

## Quick Start

1. Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'dj_vditor',
]
```

2. Add URL route in `urls.py`:

```python
# 当然你也可以自定义url和view, 只要跟配置中的upload.url一致即可
from dj_vditor.views import vditor_images_upload_view

urlpatterns = [
   ...
    path('upload-to-oss/', vditor_images_upload_view, name='vditor_upload'),
]
```

3. Use in Model:

```python
from dj_vditor.models import VditorTextField

class Article(models.Model):
    content = VditorTextField()
```

4. Configure settings:

```python
# settings.py
# 如果你需要使用OSS上传, 请设置以下配置
DJ_IMAGE_UPLOADER_OSS_CONFIG = {
    'ACCESS_KEY_ID': 'your_aliyun_key',
    'ACCESS_KEY_SECRET': 'your_aliyun_secret',
    'ENDPOINT': 'oss-cn-beijing.aliyuncs.com',
    'BUCKET_NAME': 'your-bucket-name',
    'BASE_PATH': 'your-pathname'  # 定义你的上传路径, 可选
}
# 这是默认配置, 如果不需要修改的话, 可以不设置, 直接使用默认配置
VDITOR_CONFIGS = {
    "width": "100%",
    "height": 720,
    "cache": {"enable": False},
    "mode": "sv",
    "debugger": "false",
    "icon": "ant",
    "outline": "",
    "counter": {
        "enable": True,
    },
    "lang": "zh_CN",
    "toolbar": [
        "emoji",
        "headings",
        "bold",
        "italic",
        "strike",
        "link",
        "|",
        "list",
        "ordered-list",
        "check",
        "outdent",
        "indent",
        "|",
        "quote",
        "line",
        "code",
        "inline-code",
        "insert-after",
        "table",
        "|",
        "upload",
        "fullscreen",
        "export",
        "|",
        "outline",
    ],
    "upload": {
        "url": "/upload-to-oss/",  # 上传接口地址
        "max": 5 * 1024 * 1024,  # 5MB
        "accept": "image/png,image/jpeg,image/gif,image/webp",  # 允许类型
        "fieldName": "file[]",
        "multiple": True,
    },
}
```
