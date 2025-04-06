from datetime import timedelta
from django.utils import timezone
from core.choices import JobIntervalChoices
from netbox.jobs import JobRunner, system_job
from django.db.models import Q
from .. import models


@system_job(interval=JobIntervalChoices.INTERVAL_DAILY)
class HousekeepingJob(JobRunner):
    class Meta:
        name = "Sync Status Cleanup Job"

    def run(self, *args, **kwargs):
        models.SyncStatus.objects.filter(
            Q(is_latest=False)
            & Q(created__lt=timezone.now() - timedelta(days=90))
        ).delete()