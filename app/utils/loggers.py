import logging


def configure_logging(level: int = logging.INFO) -> None:
    return logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)-3d %(levelname)-s - %(message)s",
    )
