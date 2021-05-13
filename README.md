# DBookmark

- 프로젝트 구현 순서
    - models -> admin -> views -> templates -> urls

---

- 프로젝트 시작
    - django-admin startproject config .
        - config 라는 앱으로 현재 디렉토리에 만들기
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py runserver

---

- bookmark 앱 시작
    - python manage.py startapp bookmark
    - add 'bookmark', in INSTALLED_APPS

---

- bookmark/models Bookmark
    - python manage.py makemigrations bookmark
    - python manage.py migrate
    - \_\_str\__()

---

- bookmark/admin Bookmark
    - add admin.site.register(Bookmark) in admin.py

---

- List Bookmark
    - bookmark/views BookmarkListView
    - bookmark/templates/bookmark bookmark_list.html
    - urls; bookmark/urls bookmark:list

---

- Add Bookmark
    - bookmark/views BookmarkCreateView
    - bookmark/templates/bookmark bookmark_create.html, bookmark_list.html
    - bookmark/urls bookmark:add
---

- Bookmark Detail
  - bookmark/views BookmarkDetailView
  - bookmark/templates/bookmark bookmark_detail.html, bookmark_list.html
  - bookmark/urls bookmark:detail
---

- Bookmark Update
  - bookmark/views BookmarkUpdateView
  - bookmark/templates/bookmark_update.html, bookmark_list.html
  - bookmark/urls bookmark:update
  - bookmark/models get_absolute_url() in Bookmark
---

- Bookmark Delete
  - bookmark/views BookmarkDeleteView
  - bookmark/templates/bookmark bookmark_confirm_delete.html, bookmark_list.html
  - bookmark/urls bookmark:delete
---

- Function Complete 😁😁😁😁