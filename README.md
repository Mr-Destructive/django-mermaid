## Django Mermaid

Create ER Diagrams (Entity Relationship Diagrams) of your Django projects related to different models of associated applications in Mermaid.

Get a Markdown representation of the relationships in your Django project models with Mermaid.

```
python mermaid.py <settings_project_folder>
```

TODO:

- Create a python/django package
- Provide various options for saving the diagram

Example: Base Django Project

```mermaid
erDiagram
LogEntry{
AutoField id
DateTimeField action_time
TextField object_id
CharField object_repr
PositiveSmallIntegerField action_flag
TextField change_message
}
Permission{
AutoField id
CharField name
CharField codename
}
Group{
AutoField id
CharField name
}
User{
AutoField id
CharField password
DateTimeField last_login
BooleanField is_superuser
CharField username
CharField first_name
CharField last_name
CharField email
BooleanField is_staff
BooleanField is_active
DateTimeField date_joined
}
ContentType{
AutoField id
CharField app_label
CharField model
}
Session{
CharField session_key
TextField session_data
DateTimeField expire_date
}
LogEntry||--|{User : user
LogEntry||--|{ContentType : content_type
Permission}|--|{Group : group
Permission}|--|{User : user
Permission||--|{ContentType : content_type
Group}|--|{User : user
Group}|--|{Permission : permissions
User||--|{LogEntry : logentry
User}|--|{Group : groups
User}|--|{Permission : user_permissions
ContentType||--|{LogEntry : logentry
ContentType||--|{Permission : permission
```
