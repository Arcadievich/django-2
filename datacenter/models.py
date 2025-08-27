from django.db import models
from django.utils.timezone import localtime


SECONDS_IN_MINUTE = 60


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        now_time = localtime()
        if self.leaved_at:
            time_delta = self.leaved_at - self.entered_at
        else:
            time_delta = now_time - self.entered_at
        return time_delta
    
    def is_long(self, minutes=60):
        time_delta = self.get_duration()
        visit_seconds = time_delta.total_seconds()
        visit_minutes = visit_seconds // SECONDS_IN_MINUTE
        return visit_minutes > minutes