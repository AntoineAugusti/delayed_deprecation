import datetime
import warnings


class DelayedDeprecation(object):
    def __init__(self, reason, reconsider_after, owner=None):
        super(DelayedDeprecation, self).__init__()

        if not isinstance(reconsider_after, datetime.date):
            raise ValueError("`reconsider_after` should be a datetime.date")

        if reconsider_after < datetime.date.today():
            message = (
                f'"{reason}" to be reconsidered on {str(reconsider_after)} is overdue.'
            )
            if owner:
                message += f" Owner of this task: {owner}"
            warnings.warn(message, category=DeprecationWarning)
