from typing import List

LEN_TITLE: int = 150
LEN_DESCRIPTION: int = 10000
LEN_DISCTIPLINE: int = 15
LEN_CITY: int = 20
LEN_TYPE_AREA: int = 20
LEN_ADDRESS: int = 150
LEN_PLAN: int = 10000
TYPE_AREA = [
    ('OPEN', 'Открытая'),
    ('CLOSED', 'Закрытая'),
]
MAX_FILE_SIZE: int = 10 * 1024 * 1024
ALLOWED_EXTENSIONS: List[str] = []