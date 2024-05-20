from typing import List

LEN_TITLE: int = 150
LEN_DESCRIPTION: int = 10000
LEN_DISCIPLINE_NAME: int = 30
LEN_SUBDISCTIPLINE_NAME: int = 30
LEN_TYPE_EVENT_NAME: int = 30
LEN_CITY_NAME: int = 20
LEN_REGION_NAME: int = 50
LEN_TYPE_AREA_NAME: int = 20
LEN_ADDRESS: int = 150
TYPE_AREA = [
    ('OPEN', 'Открытая'),
    ('CLOSED', 'Закрытая'),
]
MAX_FILE_SIZE: int = 10 * 1024 * 1024
ALLOWED_EXTENSIONS: List[str] = []
