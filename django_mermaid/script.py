import os
import sys

def generate_md_file(project_name):

    import sys, os
    sys.path.append(project_name)
    os.environ['DJANGO_SETTINGS_MODULE'] = f'{project_name}.settings'
    from django.conf import settings
    import django
    django.setup()
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
    #project_settings_mod = f"{project_name}.settings"
    #project_settings = __import__(project_settings_mod)
    #settings.configure(default_settings=project_settings, DEBUG=True)

    #django.setup()
    from django.apps import apps
    models_list = apps.get_models()
    model_file = f"{project_name}_model.md"
    models_data = []
    relations = []

    try:
        from django.apps import apps
        from django.conf import settings
        if settings.APP_EXCLUDE:
            for app in settings.APP_EXCLUDE:
                models = apps.get_app_config(app).models
                for model in models:
                    if models[model] in models_list:
                        models_list.remove(models[model])
    except Exception as e:
        print("There was a error in loading the models/app to exclude")
        pass
            
    for model in models_list:
        model_dict = {}
        model_fields = []
        for field in model._meta.get_fields():
            model_fields.append(field)

        model_dict[model.__name__] = model_fields
        models_data.append(model_dict)

    with open(model_file, 'w') as f:
        f.write(f"## {project_name}'s ER Diagram\n\n```mermaid\n")
        f.write("erDiagram\n")
        for model in models_data:
            for model_name in model:
                f.write(model_name + "{\n")
                for field in model[model_name]:

                    field_type = field.get_internal_type()
                    field_name = field.name

                    if field.related_model and field.related_model in models_list:
                        field_related_model = field.related_model.__name__
                        field_model = field.model.__name__
                        if field_type == 'ForeignKey':
                            relationship = "||--|{"
                        elif field_type == "ManyToManyField":
                            relationship = "}|--|{"
                        elif field_type == 'OneToOneField':
                            relationship = "||--||"
                        relations.append(field_model + relationship + field_related_model + " : " + field_name + "\n")
                    else:
                        f.write(f"{field_type} {field_name}\n")
                f.write("}\n")
        f.writelines(relations)
        f.write("```\n")
        print(f"ER Diagram for {project_name} generated in the file -> {model_file}")

