import json
import os, sys
from jinja2 import Environment, FileSystemLoader
from flask_script import Command

def trans_pytype( dbType ) : 
    if dbType.startswith("Integer") :
        return "int"
    if dbType.startswith("String") : 
        return "str"
    return 'na'

def trans_schematype( dbType ) : 
    if dbType.startswith("Integer") :
        return "Number"
    if dbType.startswith("String") : 
        return "String"
    return 'na'

classes = ["User", "Company"] 
def load_model ( kclass ) :
    f = open ( "model/{}.json".format(kclass) )
    data = json.load(f) 
    f.close() 
    data['tablename'] = data['classname'].lower() 
    for col in data['columns'] :
        col['pytype'] = trans_pytype(col['type'])
        col['schematype'] = trans_schematype(col['type'])

    return data 

class  GenCodeCommand ( Command ) : 
    def run(self):
        for kclass in classes :
            dirname=kclass.lower() 
            model = load_model ( kclass )
            templatedir = 'template'
            template_loader = FileSystemLoader(templatedir)
            env = Environment(loader=template_loader)
            templates = os.listdir (templatedir)
            for tmfile in list ( filter ( lambda s: s.endswith("template"), templates) )  :
                template = env.get_template(tmfile)
                pyfile = open("app/{}/{}".format( dirname ,  tmfile.replace(".template", ".py") ), "w") 
                pyfile.write(template.render(model) ) 
                pyfile.close() 


