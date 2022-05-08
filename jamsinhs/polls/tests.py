from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import *

import datetime


def days_from_now(days):
    return timezone.now() + datetime.timedelta(days=days)


def create_activity(**kwargs):
    for k, v in create_activity.defaults.items():
        if not k in kwargs:
            kwargs[k] = v
    return Activity.objects.create(**kwargs)


create_activity.defaults = {'title': 'Test activity',
                            'start_date': days_from_now(0),
                            'end_date': days_from_now(1),
                            'description': 'Test activity description',
                            'hour': 1
                            }


class ActivityIndexViewTest(TestCase):
    def test_no_activity(self):
        """
        If no activity exists, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "신청 가능한 활동이 없습니다.")
        self.assertQuerysetEqual(response.context['latest_activity_list'], [])

    def test_past_activity(self):
        """
        Activity with a end_date in the past is not displayed
        on the index page.
        """
        activity = create_activity(title="Past activity",
                                   start_date=days_from_now(-2),
                                   end_date=days_from_now(-1)
                                   )
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "신청 가능한 활동이 없습니다.")
        self.assertQuerysetEqual(response.context['latest_activity_list'], [])

    def test_current_activity(self):
        """
        Activity with a start_date in the past and a end_date in the future
        is displayed on the index page.
        """
        activity = create_activity(title="Past activity",
                                   start_date=days_from_now(-1),
                                   end_date=days_from_now(1)
                                   )
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_activity_list'],
            [activity],
        )

    def test_future_activity(self):
        """
        Activity with a start_date in the future is displayed
        on the index page.
        """
        activity = create_activity(title="Past activity",
                                   start_date=days_from_now(1),
                                   end_date=days_from_now(2)
                                   )
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_activity_list'],
            [activity],
        )

    def test_future_activity_and_past_activity(self):
        """
        Even if both past and future activities exist, only future activity
        is displayed.
        """
        activity = create_activity(title="Future activity",
                                   start_date=days_from_now(1),
                                   end_date=days_from_now(2)
                                   )
        create_activity(title="Past activity",
                        start_date=days_from_now(-2),
                        end_date=days_from_now(-1)
                        )
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_activity_list'],
            [activity],
        )

    def test_current_activity_and_future_activity(self):
        """
        The activities index page may display multiple activities.
        """
        activity1 = create_activity(title="Currnet activity",
                                    start_date=days_from_now(-5),
                                    end_date=days_from_now(15)
                                    )
        activity2 = create_activity(title="Future activity",
                                    start_date=days_from_now(5),
                                    end_date=days_from_now(12)
                                    )
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_activity_list'],
            [activity2, activity1],
        )
