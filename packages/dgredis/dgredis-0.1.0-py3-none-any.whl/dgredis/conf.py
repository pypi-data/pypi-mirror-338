import dataclasses


@dataclasses.dataclass
class RedisCoonfig:
    host: str
    port: int
    password: str
