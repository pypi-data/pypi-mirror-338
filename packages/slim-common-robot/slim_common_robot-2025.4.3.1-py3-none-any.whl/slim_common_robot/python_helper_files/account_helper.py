import os
import json
import re
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from robot.api.deco import keyword


@keyword("Render Env Variables for JSON File")
def walk_and_render_templates(template_dir, env_variables):
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=False
    )

    # Walk through the directory
    rendered_content = []
    for root, _, files in os.walk(template_dir):
        for filename in files:
            template = env.get_template(filename)
            render = template.render(env_variables)
            payloads = json.loads(render)
            rendered_content.append(payloads)
    return rendered_content


@keyword("Retrieve Asset Id")
def retrieve_asset_id(list_account_response_json):
    try:
        entries = list_account_response_json.get('response_map', {}).get('entries', [])
        if entries:
            return entries[0]['asset_id']
        else:
            raise Exception("Account not found in the response.")
    except KeyError as e:
        raise Exception(f"Missing expected key in response JSON: {e}")


@keyword("Load Env Variables")
def load_env_variables(env_file_path):
    """
    Load variables from a .env file.
    """
    # Load the environment variables from .env file
    load_dotenv(env_file_path)
    
    # Create a dictionary with all environment variables
    env_variables = {}
    for key, value in os.environ.items():
        env_variables[key] = value
    
    return env_variables