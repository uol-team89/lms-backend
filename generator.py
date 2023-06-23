def generate_view(output_file: str, model_name: str):
    """
    A piece of script to help me generate some boring boilerplate codes.
    Run with this command: python -c "from generator import *; generate_view('output.py', 'Entity')"
    """

    content = f"""
class {model_name}ListView(BaseListView):
    name = "{model_name} list view"
    model = models.{model_name}
    serializer = serializers.{model_name}Serializer
    
    
class {model_name}DetailsView(BaseDetailsView):
    name = "{model_name} details view"
    model = models.{model_name}
    serializer = serializers.{model_name}Serializer
    
    
class {model_name}SearchView(BaseSearchView):
    name = "{model_name} search view"
    model = models.{model_name}
    serializer = serializers.{model_name}Serializerc
    """
    f = open(output_file, "w")
    f.write(content)
    print("finished.")


def generate_urls(output_file: str, model_name: str, base_path_name: str):
    """
    Similar with the generate_view() function. This, instead, will generate urlpatterns.
    Run with this command: python -c "from generator import *; generate_urls('output.py', 'Entity', 'entities')"

    """

    content = f"""path("{base_path_name}", views.{model_name}ListView.as_view(), name="{model_name}-list"),\n"""
    content += f"""path("{base_path_name}/<int:obj_id>", views.{model_name}DetailsView.as_view(), name="{model_name}-details"),\n"""
    content += f"""path("{base_path_name}/search", views.{model_name}SearchView.as_view(), name="{model_name}-search"),\n"""
    f = open(output_file, "w")
    f.write(content)
    print("finished")
