import requests
from django.conf import settings


#
# intent
#

def query_speech(session_id, text, lang=None, timezone=None):
    data = {
        'lang': lang or settings.LANGUAGE_CODE.split('-')[0],
        'timezone': timezone or settings.TIME_ZONE,
        'sessionId': session_id,
        'query': text,
    }

    path = '/query'
    url, headers = prepare(path, is_developer_request=False)
    res = requests.post(url, headers=headers, json=data)
    res.raise_for_status()
    return res.json()


#
# entity
#

def get_entity_list():
    path = '/entities'
    url, headers = prepare(path, is_developer_request=True)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json()


def get_entity_detail(entity_id):
    path = '/entities/{}'.format(entity_id)
    url, headers = prepare(path, is_developer_request=True)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json()


def create_entity(name, entry_dict):
    data = {
        'name': name,
        'entries': entry_dict_to_list(entry_dict),
    }

    path = '/entities'
    url, headers = prepare(path, is_developer_request=True)
    res = requests.post(url, headers=headers, json=data)
    res.raise_for_status()
    return res.json()


def update_entry(entity_id, name, entry_dict):
    data = {
        'name': name,
        'entries': entry_dict_to_list(entry_dict),
    }

    path = '/entities/{}'.format(entity_id)
    url, headers = prepare(path, is_developer_request=True)
    res = requests.put(url, headers=headers, json=data)
    res.raise_for_status()
    return res.json()


def delete_entity(entity_id):
    path = '/entities/{}'.format(entity_id)
    url, headers = prepare(path, is_developer_request=True)
    res = requests.delete(url, headers=headers)
    res.raise_for_status()
    return res.json()


#
# entries
#

def update_entries(entity_id, entry_dict):
    data = entry_dict_to_list(entry_dict)

    path = '/entities/{}/entries'.format(entity_id)
    url, headers = prepare(path, is_developer_request=True)
    res = requests.put(url, headers=headers, json=data)
    res.raise_for_status()
    return res.json()


def delete_entries(entity_id, entry_id_list):
    data = entry_id_list

    path = '/entities/{}/entries'.format(entity_id)
    url, headers = prepare(path, is_developer_request=True)
    res = requests.delete(url, headers=headers, json=data)
    res.raise_for_status()
    return res.json()


#
# utilities
#

def prepare(path, headers=None, is_developer_request=False):
    if headers is None:
        headers = {}

    if is_developer_request:
        access_token = settings.DIALOGFLOW['DEVELOPER_ACCESS_TOKEN']
    else:
        access_token = settings.DIALOGFLOW['CLIENT_ACCESS_TOKEN']

    protocol_version = settings.DIALOGFLOW['V1_PROTOCOL_VERSION']

    headers.update({
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + access_token,
    })

    url = 'https://api.dialogflow.com/v1' + path + '?v=' + protocol_version

    return (url, headers)


def entry_dict_to_list(entry_dict):
    return [
        {'value': value, 'synonyms': synonyms}
        for (value, synonyms) in entry_dict.items()]

