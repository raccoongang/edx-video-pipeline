"""
Common utils.
"""
import os
import urllib
import urlparse
import yaml
from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey

CONFIG_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CONFIG_FILE_NAME = 'instance_config.yaml'
STATIC_CONFIG_FILE_PATH = os.path.join(CONFIG_ROOT_DIR, 'static_config.yaml')


def extract_course_org(course_id):
    """
    Extract video organization from course url.
    """
    org = None

    try:
        org = CourseKey.from_string(course_id).org
    except InvalidKeyError:
        pass

    return org


def build_url(*urls, **query_params):
    """
    Build a url from specified params.

    Arguments:
        base_url (str): base url
        relative_url (str): endpoint
        query_params (dict): query params

    Returns:
        absolute url
    """
    url = '/'.join(item.strip('/') for item in urls)
    if query_params:
        url = '{}?{}'.format(url, urllib.urlencode(query_params))

    return url


def get_config(yaml_config_file=DEFAULT_CONFIG_FILE_NAME):
    """
    Read yaml config file.

    Arguments:
        yaml_config_file (str): yaml config file name

    Returns:
        dict: yaml config
    """
    config_dict = {}

    try:
        yaml_config_file = os.environ['VIDEO_PIPELINE_CFG']
    except KeyError:
        yaml_config_file = os.path.join(
            CONFIG_ROOT_DIR,
            yaml_config_file
        )

    with open(yaml_config_file, 'r') as config:
        config_dict = yaml.load(config)

    # read static config file
    with open(STATIC_CONFIG_FILE_PATH, 'r') as config:
        static_config_dict = yaml.load(config)

    return dict(config_dict, **static_config_dict)


def scrub_query_params(url, params_to_scrub):
    """
    Scrub query params present in `params_to_scrub` from `url`

    Arguments:
        url (str): url
        params_to_scrub (list): name of query params to be scrubbed from url

    Returns:
        url with query params scrubbed

    >>> old_url = https://sandbox.veda.com/api/do?api_token=veda_api_key&job_name=12345&language=en&v=1
    >>> new_url = https://sandbox.veda.com/api/do?v=1&job_name=12345&language=en&api_token=XXXXXXXXXXXX
    """
    parsed = urlparse.urlparse(urllib.unquote(url))

    # query_params will be in the form of [('v', '1'), ('job_name', '12345')]
    query_params = urlparse.parse_qsl(parsed.query)

    new_query_params = {}
    for key, value in query_params:
        new_query_params[key] = len(value) * 'X' if key in params_to_scrub else value

    return build_url(
        '{scheme}://{netloc}'.format(scheme=parsed.scheme, netloc=parsed.netloc),
        parsed.path,
        **new_query_params
    )
