from logging import LoggerAdapter


class GameLogger(LoggerAdapter):
    def process(self, msg, kwargs):
        new_msg = [msg]
        if 'game_id' in self.extra:
            new_msg.insert(0, '[%s]' % self.extra['game_id'])

        new_msg = ' '.join(new_msg)
        return new_msg, kwargs


def make_logger(base_logger, game_id=None):
    logger_extra = {}
    if game_id is not None:
        logger_extra['game_id'] = game_id

    return GameLogger(base_logger, logger_extra)
