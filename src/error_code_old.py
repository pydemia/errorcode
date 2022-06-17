from enum import Enum, unique


__all__ = [
    "ResponseCode"
]

@unique
class ResponseCode(Enum):

    # general(~)
    SUCCESS  = (1, "성공")
    FAIL = (-1, "실패")
    UNDEFINED_ERROR = (-2, "정의되지 않은 오류입니다.")
    RESPONSECODE_NOT_SET = (-3, "ErrorResponse에 응답 코드가 정의되지 않았습니다.")
    INVALID_APP_CONFIG_ERROR = (-4, "Application의 Config 값에 문제가 있습니다." )

    # http message error
    NOT_DEFINED_REQUEST = (-110, "시스템에 정의되지 않은 요청입니다.")
    REQUEST_FORMAT_ERROR = (-120, "잘못된 요청입니다.")

    # Gateway & Account = (-1000 ~ 1099)
    EXPIRED_TOKEN = (-1002, "토큰이 만료되었습니다.")
    FORGERY_TOKEN = (-1003, "위변조된 토큰입니다.")
    NON_EXISTENT_ACCESS_KEY = (-1004, "존재하지 않는 인증키 입니다.")
    INVALID_PASSWORD = (-1005, "비밀번호가 일치하지 않습니다.")
    PAUSED_ACCOUNT = (-1006, "사용 정지된 계정입니다.")
    NON_EXISTENT_ID = (-1007, "로그인에 실패했습니다.")
    ID_ALREADY_EXISTS = (-1008, "이미 존재하는 ID 입니다.")
    DELETED_ID = (-1009, "삭제된 ID 입니다.")
    DO_NOT_HAVE_PERMISSION = (-1010, "권한이 없습니다.")
    WRONG_SORT_TYPE = (-1011, "잘못된 정렬 형식입니다.")
    INVALID_OLD_PASSWORD = (-1012, "기존 비밀번호가 일치하지 않습니다.")
    NEW_PWD_MUST_BE_DIFFERENT = (-1013, "새로운 비밀번호는 기존 비밀번호와 동일할 수 없습니다.")
    REDIS_SERVER_ERROR = (-1014, "캐시 서버 접속 실패")
    INVALID_PWD_REGEX = (-1015, "규칙에 어긋나는 비밀번호입니다.")
    INVALID_ID = (-1016, "존재하지 않는 ID입니다.")


    def __init__(self, code: int, message: str):
        # self._value_ = code
        self.code = code
        self.message = message
        cls = self.__class__
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value, self.message).name
            raise ValueError(
                "aliases not allowed to prevent duplicatation:  %r --> %r"
                % (a, e))

    @property
    def describe(self):
        # self is the member here
        return self.name, self.code, self.message

    def __new__(cls, code: int, message: str):
        obj = object.__new__(cls)
        # obj._value_ = code
        obj.code = code
        obj.message = message
        return obj

    def __str__(self) -> str:
        return f'[{self.code}]: {self.message}'
    
    @classmethod
    def of(cls, code: int) -> "ResponseCode":
        for item in cls:
            if item.value[0] == code:
                return item
        return super()._missing_(code)

