import os, django
from django.apps import apps
import sys
project_name = sys.argv[1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
django.setup()

models_list = apps.get_models()
models_data = []
relations = []

for model in models_list:
    model_dict = {}
    model_fields = []
    for field in model._meta.get_fields():
        model_fields.append(field)

    model_dict[model.__name__] = model_fields
    models_data.append(model_dict)

with open('models.md', 'w') as f:
    f.write("erDiagram\n")
    for model in models_data:
        for model_name in model:
            f.write(model_name + "{\n")
            for field in model[model_name]:

                field_type = field.get_internal_type()
                field_name = field.name

                if field.related_model:
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

