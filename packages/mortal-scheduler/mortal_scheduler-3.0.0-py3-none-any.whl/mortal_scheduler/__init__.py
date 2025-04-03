#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: MaJian
@Time: 2025/4/3 14:24
@SoftWare: PyCharm
@Project: mortal
@File: __init__.py
"""
from datetime import datetime

from .scheduler_main import MortalSchedulerMain


class MortalScheduler(MortalSchedulerMain):
    def __init__(self):
        super().__init__()

    def add_jobstore(
            self, jobstore='memory', alias='default', slchemy_url=None, host=None, port=None,
            database=None, collection=None, **kwargs
    ):
        """添加jobstore"""
        self._add_jobstore(jobstore, alias, slchemy_url, host, port, database, collection, **kwargs)

    def remove_jobstore(self, alias):
        """删除jobstore"""
        self._remove_jobstore(alias)

    def add_executor(self, executor='thread', alias='default', max_workers=1, **kwargs):
        """添加executor"""
        self._add_executor(executor, alias, max_workers, **kwargs)

    def remove_executor(self, alias):
        """删除executor"""
        self._remove_executor(alias)

    def add_cron_job(
            self, func, job_id=None, year=None, month=None, day=None, week=None, day_of_week=None, hour=None,
            minute=None, second=None, start_date=datetime.now(), end_date=None, timezone=None, jitter=None,
            jobstore='default', executor='default', **kwargs
    ):
        return self._add_cron_job(
            func, job_id, year, month, day, week, day_of_week, hour, minute, second,
            start_date, end_date, timezone, jitter, jobstore, executor, **kwargs
        )

    def add_interval_job(
            self, func, job_id=None, weeks=0, days=0, hours=0, minutes=0, seconds=0, start_date=datetime.now(),
            end_date=None, timezone=None, jitter=None, jobstore='default', executor='default', **kwargs
    ):
        return self._add_interval_job(
            func, job_id, weeks, days, hours, minutes, seconds, start_date,
            end_date, timezone, jitter, jobstore, executor, **kwargs
        )

    def add_date_job(
            self, func, run_date, job_id=None, timezone=None, jobstore='default', executor='default', **kwargs
    ):
        return self._add_date_job(func, run_date, job_id, timezone, jobstore, executor, **kwargs)

    def add_after_job(
            self, func, job_id=None, weeks=0, days=0, hours=0, minutes=0, seconds=0, start_date=datetime.now(),
            timezone=None, jobstore='default', executor='default', **kwargs
    ):
        return self._add_after_job(
            func, job_id, weeks, days, hours, minutes, seconds,
            start_date, timezone, jobstore, executor, **kwargs
        )

    def remove_job(self, job_id):
        self._remove_job(job_id)

    def pause_job(self, job_id):
        self._pause_job(job_id)

    def resume_job(self, job_id):
        self._resume_job(job_id)

    def get_jobs(self):
        return self._get_jobs()

    def shutdown(self, wait=True):
        self._shutdown(wait=wait)

    def modify_job_trigger(self, job_id, trigger_type, **trigger_args):
        self._modify_job_trigger(job_id, trigger_type, **trigger_args)

    def get_job_details(self, job_id):
        return self._get_job_details(job_id)

    def pause_all_jobs(self):
        """暂停所有任务"""
        self._pause_all_jobs()

    def resume_all_jobs(self):
        """恢复所有任务"""
        self._resume_all_jobs()

    def job_exists(self, job_id):
        """检查任务是否存在"""
        return self._job_exists(job_id)

    def get_all_job_ids(self):
        """获取所有任务的ID"""
        return self._get_all_job_ids()

    def clear_all_jobs(self):
        """清理所有任务"""
        self._clear_all_jobs()

    def modify_job(self, job_id, func=None, args=None, kwargs=None, trigger=None):
        """修改任务的参数"""
        self._modify_job(job_id, func, args, kwargs, trigger)

    def get_scheduler_state(self):
        """获取调度器的当前状态"""
        return self._get_scheduler_state()

    def modify_job_run_date(self, job_id, run_date):
        """修改任务的执行时间"""
        self._modify_job_run_date(job_id, run_date)

    def get_job_state(self, job_id):
        return self._get_job_state(job_id)
