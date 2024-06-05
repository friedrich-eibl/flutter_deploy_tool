import os
import google.auth
from googleapiclient.discovery import build, Resource
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload


def connect_to_play_store() -> Resource:
    KEY_FILE = 'testdevtools-424919-57bfe0c8a634.json'
    SCOPES = ['https://www.googleapis.com/auth/androidpublisher']

    credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)

    return build('androidpublisher', 'v3', credentials=credentials)


def publish_to_play_store(service: Resource) -> None:
    package_name = 'com.friedricheibl.trackntrain'
    bundle = 'app-release.aab'

    # create edit
    edit = service.edits().insert(body={}, packageName=package_name).execute()
    edit_id = edit['id']
    print('Prepared Edit')
    # upload appbundle
    upload_request = service.edits().bundles().upload(
        editId = edit_id,
        packageName = package_name,
        media_body = MediaFileUpload(bundle, mimetype='application/octet-stream')
    )
    bundle_response = upload_request.execute()
    print('Version code: %s' % bundle_response['versionCode'])
    
    # Update health features
    health_features = {
        "health": False  # Change to True if your app includes health features
    }
    #track_response = service.edits().tracks().update(
     #   editId=edit_id,
     #   packageName=package_name,
     #   track='rollout',
     #   body={u'versionCode': [bundle_response['versionCode']]}
    #).execute()
    #print(track_response)

    commit_request = service.edits().commit(
            editId = edit_id,
            packageName = package_name
    )
    commit_request.execute()
    print('Edit commited successfully')


    pass


service = connect_to_play_store()
print('Connected Successfully')
publish_to_play_store(service)
print('Pusblished!')
