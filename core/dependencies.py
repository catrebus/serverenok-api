from core import container


def get_info_service():
    return container.info_service

def get_storage_service():
    return container.storage_service

def get_folders_helper():
    return container.folders_helper